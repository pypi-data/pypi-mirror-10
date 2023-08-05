from __future__ import absolute_import, print_function

import zmq
from itertools import chain
from bisect import bisect
from operator import add
from time import sleep, time
from toolz import accumulate, topk, pluck, merge, keymap
import uuid
from collections import defaultdict
from contextlib import contextmanager
from threading import Thread, Lock
from datetime import datetime
from multiprocessing import Process
from . import core
from .compatibility import Queue, Empty


tuple_sep = '-|-'

def log(*args):
    with open('log', 'a') as f:
        print(datetime.now(), *args, file=f)


log('Import zmq')

@contextmanager
def logduration(message, nbytes=None):
    start = time()
    try:
        yield
    finally:
        end = time()
        log(message, end - start)
        if nbytes:
            log("MB/s:", nbytes / (end - start) / 1e6)

@contextmanager
def logerrors():
    try:
        yield
    except Exception as e:
        log('Error!', str(e))
        raise


class Server(object):
    def __init__(self, path=None, address=None, available_memory=1e9,
                 n_outstanding_writes=10, start=True, block=False):
        self.context = zmq.Context()
        self.file = File(path)
        self.inmem = defaultdict(list)
        self.lengths = defaultdict(lambda: 0)
        self.socket = self.context.socket(zmq.ROUTER)

        if address is None:
            address = 'ipc://server-%s' % str(uuid.uuid1())
        self.address = address
        self.socket.bind(self.address)

        self.available_memory=available_memory
        self.memory_usage = 0
        self.status = 'created'
        self._out_disk_buffer = Queue(maxsize=n_outstanding_writes)
        self._frozen_sockets = Queue()

        self.file.lock.acquire()
        self._lock = Lock()
        self._socket_lock = Lock()

        if start:
            self.start()

        if block:
            self.block()

    def start(self):
        if self.status != 'run':
            self.status = 'run'
            self._listen_thread = Thread(target=self.listen)
            self._listen_thread.start()
            self._write_to_disk_thread = Thread(target=self._write_to_disk)
            self._write_to_disk_thread.start()
            self._free_frozen_sockets_thread = Thread(target=self._free_frozen_sockets)
            self._free_frozen_sockets_thread.start()
            log('Start server at', self.address)

    def block(self):
        """ Block until all threads close """
        try:
            self._listen_thread.join()
            self._free_frozen_sockets_thread.join()
            self._write_to_disk_thread.join()
        except AttributeError:
            pass

    def listen(self):
        with logerrors():
            log(self.address, 'start listening')
            while self.status != 'closed':
                if not self.socket.poll(100):
                    continue

                with self._socket_lock:
                    payload = self.socket.recv_multipart()

                address, command, payload = payload[0], payload[1], payload[2:]
                log('Server receives', address, command)
                if command == b'close':
                    log('Server closes')
                    self.ack(address)
                    self.status = 'closed'
                    break
                    # self.close()

                elif command == b'append':
                    keys, values = payload[::2], payload[1::2]
                    keys = list(map(deserialize_key, keys))
                    data = dict(zip(keys, values))
                    self.append(data)
                    self.ack(address)

                elif command == b'iset':
                    key, value = payload
                    key = deserialize_key(key)
                    if key not in self.inmem:
                        self.inmem[key] = value
                    self.ack(address)

                elif command == b'get':
                    keys = list(map(deserialize_key, payload))
                    log('get', keys)
                    result = self.get(keys)
                    self.send_to_client(address, result)
                    self.ack(address, flow_control=False)

                elif command == b'delete':
                    keys = list(map(deserialize_key, payload))
                    log('delete', keys)
                    self.delete(keys)
                    self.ack(address, flow_control=False)

                elif command == b'syn':
                    self.ack(address)

                elif command == b'drop':
                    self.drop()
                    self.ack(address)

                else:
                    log("Unknown command", command)
                    raise ValueError("Unknown command: " + command)

    def send_to_client(self, address, result):
        with logerrors():
            if not isinstance(result, list):
                result = [result]
            with self._socket_lock:
                self.socket.send_multipart([address] + result)

    def _write_to_disk(self):
        while self.status != 'closed':
            try:
                data = self._out_disk_buffer.get(timeout=1)
            except Empty:
                continue
            else:
                with self._lock:
                    nbytes = sum(map(len, data.values()))
                    with logduration("Write %d files %d bytes" %
                                     (len(data), nbytes),
                                     nbytes=nbytes):
                        self.file.append(data, lock=False)
                self._out_disk_buffer.task_done()

    def ack(self, address, flow_control=True):
        with logerrors():
            if flow_control and self._out_disk_buffer.full():
                log('Out disk buffer full - Flow control in effect',
                    'Freezing address', address)
                self._frozen_sockets.put(address)
            else:
                log('Server sends ack')
                self.send_to_client(address, b'ack')

    def _free_frozen_sockets(self):
        while self.status != 'closed':
            try:
                data = self._frozen_sockets.get(timeout=1)
                self._frozen_sockets.put(data)  # put back in for the moment
            except Empty:
                continue
            else:
                log('Freeing frozen sockets, waiting on disk buffer to clear')
                self._out_disk_buffer.join()
                log('Disk buffer cleared, sending acks to %d sockets' %
                        self._frozen_sockets.qsize())
                while not self._frozen_sockets.empty():
                    addr = self._frozen_sockets.get()
                    log('Free', addr)
                    self.ack(addr)

    def append(self, data):
        total_mem = 0
        for k, v in data.items():
            self.inmem[k].append(v)
            self.lengths[k] += len(v)
            total_mem += len(v)
        self.memory_usage += total_mem

        log('Server appends %d keys' % len(data), 'of %d bytes' % total_mem)

        while self.memory_usage > self.available_memory:
            keys = keys_to_flush(self.lengths, 0.1, maxcount=20)
            self.flush(keys)

    def delete(self, keys):
        released = 0
        for k in keys:
            released += sum(map(len, self.inmem[k]))
            del self.inmem[k]

        self.memory_usage -= released

        log('Server deleted %d keys' % len(keys),
            '. Released %d bytes' % released)

        # TODO: delete file from disk

    def drop(self):
        with logerrors():
            self.inmem.clear()
            self.memory_usage = 0
            self.lengths.clear()
            self.file.drop()

    def flush(self, keys=None, block=None):
        """ Flush keys to disk

        Parameters
        ----------

        keys: list or None
            list of keys to flush
        block: bool (defaults to None)
            Whether or not to block until all writing is complete

        If no keys are given then flush all keys
        """
        if keys is None:
            keys = list(self.lengths)
            if block is None:
                block = True
        assert isinstance(keys, (tuple, list))
        payload = dict((key, b''.join(self.inmem[key])) for key in keys)
        log('append data into out-disk-buffer', 'nkeys', len(keys))
        self._out_disk_buffer.put(payload)

        for key in keys:
            self.memory_usage -= self.lengths[key]
            del self.inmem[key]
            del self.lengths[key]

        if block:
            log('Blocking on out disk buffer from flush')
            self._out_disk_buffer.join()

    def get(self, keys):
        with logerrors():
            log('Server gets keys', keys)
            self._out_disk_buffer.join()  # block until everything is written
            with self._lock:
                from_disk = self.file.get(keys, lock=False)
                result = [from_disk[i] + b''.join(self.inmem[k])
                              for i, k in enumerate(keys)]
            return result

    def close(self):
        log('Server closes')
        self.status = 'closed'
        self.block()
        self.socket.close(1)
        self.context.destroy(3)
        self.file.lock.release()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.close()
        self.file.__exit__(*args)


def keys_to_flush(lengths, fraction=0.1, maxcount=100000):
    """ Which keys to remove

    >>> lengths = {'a': 20, 'b': 10, 'c': 15, 'd': 15,
    ...            'e': 10, 'f': 25, 'g': 5}
    >>> keys_to_flush(lengths, 0.5)
    ['f', 'a']
    """
    top = topk(max(len(lengths) // 2, 1),
               lengths.items(),
               key=1)
    total = sum(lengths.values())
    cutoff = min(maxcount, max(1,
                   bisect(list(accumulate(add, pluck(1, top))),
                          total * fraction)))
    result = [k for k, v in top[:cutoff]]
    assert result
    return result


def serialize_key(key):
    """

    >>> serialize_key('x')
    'x'
    >>> serialize_key(('a', 'b', 1))
    'a-|-b-|-1'
    """
    if isinstance(key, tuple):
        return tuple_sep.join(map(serialize_key, key))
    if isinstance(key, bytes):
        return key
    if isinstance(key, str):
        return key.encode()
    return str(key).encode()


def deserialize_key(text):
    """

    >>> deserialize_key('x')
    'x'
    >>> deserialize_key('a-|-b-|-1')
    ('a', 'b', '1')
    """
    if tuple_sep in text:
        return tuple(text.split(tuple_sep))
    else:
        return text


from .core import Interface
from .file import File


class Shared(Interface):
    def __init__(self, address=None, create_server=False, **kwargs):
        if create_server or address is None:
            if address is None:
                address = 'ipc://server-%s' % str(uuid.uuid1())
            self.server_process = Process(target=Server,
                                          args=(),
                                          kwargs=merge(kwargs,
                                          {'block': True, 'address': address,
                                           'start': True}))
            self.server_process.start()

        self.address = address
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.DEALER)
        log('Client connects to %s' % address)
        self.socket.connect(address)
        self.send(b'syn', [], ack_required=False)
        self.lock = NotALock()  # Server sequentializes everything
        Interface.__init__(self)

    def __getstate__(self):
        return {'address': self.address}

    def __setstate__(self, state):
        self.__init__(state['address'])
        log('Reconstruct client from pickled state')

    def send(self, command, payload, recv=False, ack_required=True):
        if ack_required:
            ack = self.socket.recv_multipart()
            assert ack == [b'ack']
        log('Client sends command', command)
        self.socket.send_multipart([command] + payload)
        if recv:
            result = self.socket.recv_multipart()
        else:
            result = None
        return result

    def _get(self, keys, lock=None):
        """

        Lock argument is ignored.  Everything is sequential (I think)
        """
        log('Client gets', self.address, keys)
        keys = list(map(serialize_key, keys))
        return self.send(b'get', keys, recv=True)

    def append(self, data, lock=None):
        log('Client appends', self.address, str(len(data)) + ' keys')
        data = keymap(serialize_key, data)
        payload = list(chain.from_iterable(data.items()))
        self.send(b'append', payload)

    def _delete(self, keys, lock=None):
        log('Client deletes', self.address, str(len(keys)) + ' keys')
        keys = map(serialize_key, keys)
        self.send(b'delete', keys)

    def _iset(self, key, value):
        self.send(b'iset', [key, value])

    def drop(self):
        self.send(b'drop', [])
        sleep(0.05)

    def close_server(self):
        self.send(b'close', [])

    def close(self):
        if hasattr(self, 'server_process'):
            self.close_server()
            self.server_process.join()
        self.socket.close(1)
        self.context.destroy(1)

    def __exit__(self, type, value, traceback):
        self.drop()
        self.close()

    def __del__(self):
        self.close()


class NotALock(object):
    def acquire(self): pass
    def release(self): pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass
