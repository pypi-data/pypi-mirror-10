import os
import struct
import asyncio

from pickle import loads, dumps


@asyncio.coroutine
def pipe(loop=None):
    loop = loop or asyncio.get_event_loop()

    reader_handle, writer_handle = os.pipe()

    reader = asyncio.StreamReader(loop=loop)
    reader_protocol = asyncio.StreamReaderProtocol(reader, loop=loop)
    reader_transport, _ = yield from loop.connect_read_pipe(
        lambda: reader_protocol, os.fdopen(reader, 'rb', 0))

    writer_transport, writer_protocol = yield from loop.connect_write_pipe(
        asyncio.Protocol, os.fdopen(writer, 'wb', 0))
    writer = asyncio.StreamWriter(writer_transport, writer_protocol,
                                  reader, loop)

    return reader, writer


class WritePipeProtocol(asynctio.Protocol):
    def __init__(self, handler):
        self.pipe = None
        self.handler = handler

    def connection_made(self, transport):
        self.pipe = transport

    def __repr__(self):
        return ('<%s fd=%s pipe=%r>'
                % (self.__class__.__name__, self.fd, self.pipe))

    def connection_lost(self, exc):
        self.disconnected = True
        self.proc._pipe_connection_lost(self.fd, exc)

    def pause_writing(self):
        self.proc._protocol.pause_writing()

    def resume_writing(self):
        self.proc._protocol.resume_writing()


class ReadSubprocessPipeProto(WritePipeProtocol, asyncio.Protocol):
    def data_received(self, data):
        self.proc._pipe_data_received(self.fd, data)


@asyncio.coroutine
def recv(reader, size):
    """Waits until size bytes are received."""
    data = bytearray()

    while len(data) < size:
        if reader.at_eof():
            raise EOFError("End Of File")
        data += yield from reader.read(size - len(data))

    return data


class Connection(object):
    def __init__(self, handle):
        self._reader = None
        self._writer = None
        self._handle = handle

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    @asyncio.coroutine
    def _recv(self):
        """Receives data from the other side of the connection
        and deserializes it.

        """
        data = yield from recv(self._reader, 4)
        size, = struct.unpack('!i', data)
        data = yield from recv(self._reader, size)

        return loads(data)

    def _closed(self):
        if self.closed:
            raise OSError("handle is closed")

    def _readable(self):
        if not self.readable:
            raise OSError("connection is not readable")

    def _writable(self):
        if not self.writable:
            raise OSError("connection is not writable")

    @property
    def closed(self):
        """True if the Connection is closed"""
        return self._handle is None

    @property
    def readable(self):
        """True if the connection is readable"""
        if self._handle is not None:
            return self._reader is not None
        else:
            return False

    @property
    def writable(self):
        """True if the connection is writable"""
        if self._handle is not None:
            return self._writer is not None
        else:
            return False

    @asyncio.coroutine
    def connect(self, loop=None):

    @asyncio.coroutine
    def recv(self):
        self._closed()
        self._readable()

        return (yield from self._recv())

    def fileno(self):
        """File descriptor or handle of the connection"""
        self._closed()

        return self._handle

    def close(self):
        """Close the connection"""
        if self._handle is not None:
            try:
                self._handle.close()
            finally:
                self._handle = None

    def send(self, obj):
        self._closed()
        self._writable()

        data = dumps(obj)
        size = struct.pack('!i', len(data))

        self._writer.write(size)
        self._writer.write(data)
