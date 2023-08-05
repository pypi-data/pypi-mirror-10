"""
"""
import asyncio
import base64
import hashlib
import os

from aiohttp import (client, hdrs, DataQueue, StreamParser,
    WSServerHandshakeError, ClientSession, TCPConnector)
from aiohttp.errors import WSServerHandshakeError
from aiohttp.websocket import WS_KEY, Message
from aiohttp.websocket import WebSocketParser, WebSocketWriter, WebSocketError
from aiohttp.websocket import (MSG_BINARY, MSG_TEXT, MSG_CLOSE, MSG_PING,
    MSG_PONG)
from aiohttp.websocket_client import (MsgType, closedMessage,
    ClientWebSocketResponse)

from aiogremlin.exceptions import SocketClientError
from aiogremlin.log import INFO, logger

__all__ = ('WebSocketSession', 'GremlinFactory',
           'GremlinClientWebSocketResponse')


# Basically cut and paste from aiohttp until merge/release of #374
class WebSocketSession(ClientSession):

    def __init__(self, *, connector=None, loop=None,
                 cookies=None, headers=None, auth=None,
                 ws_response_class=None):

        super().__init__(connector=connector, loop=loop,
                         cookies=cookies, headers=headers, auth=auth)

        self._ws_response_class = ws_response_class


    @asyncio.coroutine
    def ws_connect(self, url, *,
                   protocols=(),
                   timeout=10.0,
                   autoclose=True,
                   autoping=True,
                   ws_response_class=None,
                   loop=None):
        """Initiate websocket connection."""

        sec_key = base64.b64encode(os.urandom(16))

        headers = {
            hdrs.UPGRADE: hdrs.WEBSOCKET,
            hdrs.CONNECTION: hdrs.UPGRADE,
            hdrs.SEC_WEBSOCKET_VERSION: '13',
            hdrs.SEC_WEBSOCKET_KEY: sec_key.decode(),
        }
        if protocols:
            headers[hdrs.SEC_WEBSOCKET_PROTOCOL] = ','.join(protocols)

        # send request
        resp = yield from self.request('get', url, headers=headers,
                                       read_until_eof=False)

        # check handshake
        if resp.status != 101:
            raise WSServerHandshakeError('Invalid response status')

        if resp.headers.get(hdrs.UPGRADE, '').lower() != 'websocket':
            raise WSServerHandshakeError('Invalid upgrade header')

        if resp.headers.get(hdrs.CONNECTION, '').lower() != 'upgrade':
            raise WSServerHandshakeError('Invalid connection header')

        # key calculation
        key = resp.headers.get(hdrs.SEC_WEBSOCKET_ACCEPT, '')
        match = base64.b64encode(hashlib.sha1(sec_key + WS_KEY).digest()).decode()
        if key != match:
            raise WSServerHandshakeError('Invalid challenge response')

        # websocket protocol
        protocol = None
        if protocols and hdrs.SEC_WEBSOCKET_PROTOCOL in resp.headers:
            resp_protocols = [proto.strip() for proto in
                              resp.headers[hdrs.SEC_WEBSOCKET_PROTOCOL].split(',')]

            for proto in resp_protocols:
                if proto in protocols:
                    protocol = proto
                    break

        reader = resp.connection.reader.set_parser(WebSocketParser)
        writer = WebSocketWriter(resp.connection.writer, use_mask=True)

        if ws_response_class is None:
            ws_response_class = (self._ws_response_class or
                                 ClientWebSocketResponse)

        return ws_response_class(
            reader, writer, protocol, resp, timeout, autoclose, autoping, loop)

    def detach(self):
        """Detach connector from session without closing the former.
        Session is switched to closed state anyway.
        """
        self._connector = None


# Cut and paste from aiohttp until merge/release of #374
def ws_connect(url, *, protocols=(), timeout=10.0, connector=None,
               ws_response_class=None, autoclose=True, autoping=True,
               loop=None):
    if loop is None:
        asyncio.get_event_loop()
    if connector is None:
        connector = TCPConnector(loop=loop, force_close=True)

    ws_session = WebSocketSession(loop=loop, connector=connector)
    try:
        resp = yield from ws_session.ws_connect(url,
                                                protocols=protocols,
                                                timeout=timeout,
                                                ws_response_class=ws_response_class,
                                                autoclose=autoclose,
                                                autoping=autoping,
                                                loop=loop)
        return resp

    finally:
        ws_session.detach()


class GremlinFactory:

    def __init__(self, connector=None):
        self._connector = connector

    @asyncio.coroutine
    def ws_connect(self, url='ws://localhost:8182/', protocols=(),
                   connector=None, autoclose=False, autoping=True,
                   ws_response_class=None, loop=None):
        if connector is None:
            connector = self._connector
        if ws_response_class is None:
            ws_response_class = GremlinClientWebSocketResponse
        try:
            return (yield from ws_connect(
                url, protocols=protocols, connector=connector,
                ws_response_class=ws_response_class, autoclose=True, autoping=True,
                loop=loop))
        except WSServerHandshakeError as e:
            raise SocketClientError(e.message)


class GremlinClientWebSocketResponse(ClientWebSocketResponse):

    def __init__(self, reader, writer, protocol, response, timeout, autoclose,
                 autoping, loop):
        ClientWebSocketResponse.__init__(self, reader, writer, protocol,
            response, timeout, autoclose, autoping, loop)
        self._parser = StreamParser(buf=DataQueue(loop=loop), loop=loop)

    @property
    def parser(self):
        return self._parser

    @property
    def closed(self):
        """Required by ABC."""
        return self._closed

    @asyncio.coroutine
    def close(self, *, code=1000, message=b''):
        if not self._closed:
            do_close = self._close()
            if do_close:
                return True
            while True:
                try:
                    msg = yield from asyncio.wait_for(
                        self._reader.read(), self._timeout, loop=self._loop)
                except asyncio.CancelledError:
                    self._close_code = 1006
                    self._response.close(force=True)
                    raise
                except Exception as exc:
                    self._close_code = 1006
                    self._exception = exc
                    self._response.close(force=True)
                    return True

                if msg.tp == MsgType.close:
                    self._close_code = msg.data
                    self._response.close(force=True)
                    return True
        else:
            return False

    def _close(self, code=1000, message=b''):
        self._closed = True
        try:
            self._writer.close(code, message)
        except asyncio.CancelledError:
            self._close_code = 1006
            self._response.close(force=True)
            raise
        except Exception as exc:
            self._close_code = 1006
            self._exception = exc
            self._response.close(force=True)
            return True

        if self._closing:
            self._response.close(force=True)
            return True

    def send(self, message, binary=True):
        if binary:
            method = self.send_bytes
        else:
            method = self.send_str
        try:
            method(message)
        except RuntimeError:
            # Socket closed.
            raise
        except TypeError:
            # Bytes/string input error.
            raise

    @asyncio.coroutine
    def receive(self):
        if self._waiting:
            raise RuntimeError('Concurrent call to receive() is not allowed')

        self._waiting = True
        try:
            while True:
                if self._closed:
                    return closedMessage

                try:
                    msg = yield from self._reader.read()
                except (asyncio.CancelledError, asyncio.TimeoutError):
                    raise
                except WebSocketError as exc:
                    self._close_code = exc.code
                    yield from self.close(code=exc.code)
                    raise
                except Exception as exc:
                    self._exception = exc
                    self._closing = True
                    self._close_code = 1006
                    yield from self.close()
                    raise
                if msg.tp == MsgType.close:
                    self._closing = True
                    self._close_code = msg.data
                    if not self._closed and self._autoclose:
                        yield from self.close()
                    raise RuntimeError("Socket connection closed by server.")
                elif not self._closed:
                    if msg.tp == MsgType.ping and self._autoping:
                        self._writer.pong(msg.data)
                    elif msg.tp == MsgType.pong and self._autoping:
                        continue
                    else:
                        if msg.tp == MsgType.binary:
                            self.parser.feed_data(msg.data.decode())
                        elif msg.tp == MsgType.text:
                            self.parser.feed_data(msg.data.strip())
                        else:
                            raise RuntimeError("Unknown message type.")
                        break
        finally:
            self._waiting = False
