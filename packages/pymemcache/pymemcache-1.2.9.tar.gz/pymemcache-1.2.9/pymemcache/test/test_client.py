# Copyright 2012 Pinterest.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
import json
import socket
import unittest

from nose import tools
from pymemcache.client import PooledClient
from pymemcache.client import Client, MemcacheUnknownCommandError
from pymemcache.client import MemcacheClientError, MemcacheServerError
from pymemcache.client import MemcacheUnknownError, MemcacheIllegalInputError
from pymemcache import pool
from pymemcache.test.utils import MockMemcacheClient


class MockSocket(object):
    def __init__(self, recv_bufs):
        self.recv_bufs = collections.deque(recv_bufs)
        self.send_bufs = []
        self.closed = False
        self.timeouts = []
        self.connections = []
        self.socket_options = []

    def sendall(self, value):
        self.send_bufs.append(value)

    def close(self):
        self.closed = True

    def recv(self, size):
        value = self.recv_bufs.popleft()
        if isinstance(value, Exception):
            raise value
        return value

    def settimeout(self, timeout):
        self.timeouts.append(timeout)

    def connect(self, server):
        self.connections.append(server)

    def setsockopt(self, level, option, value):
        self.socket_options.append((level, option, value))


class MockSocketModule(object):
    def socket(self, family, type):
        return MockSocket([])

    def __getattr__(self, name):
        return getattr(socket, name)


class ClientTestMixin(object):
    def make_client(self, mock_socket_values, serializer=None):
        client = Client(None, serializer=serializer)
        client.sock = MockSocket(list(mock_socket_values))
        return client

    def test_set_success(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.set(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)

    def test_set_unicode_key(self):
        client = self.make_client([b''])

        def _set():
            client.set(u'\u0FFF', b'value', noreply=False)

        tools.assert_raises(MemcacheIllegalInputError, _set)

    def test_set_unicode_value(self):
        client = self.make_client([b''])

        def _set():
            client.set(b'key', u'\u0FFF', noreply=False)

        tools.assert_raises(MemcacheIllegalInputError, _set)

    def test_set_noreply(self):
        client = self.make_client([])
        result = client.set(b'key', b'value', noreply=True)
        tools.assert_equal(result, True)

    def test_set_many_success(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.set_many({b'key' : b'value'}, noreply=False)
        tools.assert_equal(result, True)

    def test_add_stored(self):
        client = self.make_client([b'STORED\r', b'\n'])
        result = client.add(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)

    def test_add_not_stored(self):
        client = self.make_client([b'STORED\r', b'\n',
                                   b'NOT_', b'STOR', b'ED', b'\r\n'])
        result = client.add(b'key', b'value', noreply=False)
        result = client.add(b'key', b'value', noreply=False)
        tools.assert_equal(result, False)

    def test_get_not_found(self):
        client = self.make_client([b'END\r\n'])
        result = client.get(b'key')
        tools.assert_equal(result, None)

    def test_get_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'VALUE key 0 5\r\nvalue\r\nEND\r\n',
        ])
        result = client.set(b'key', b'value', noreply=False)
        result = client.get(b'key')
        tools.assert_equal(result, b'value')

    def test_get_many_none_found(self):
        client = self.make_client([b'END\r\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equal(result, {})

    def test_get_many_some_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'VALUE key1 0 6\r\nvalue1\r\nEND\r\n',
        ])
        result = client.set(b'key1', b'value1', noreply=False)
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equal(result, {b'key1': b'value1'})

    def test_get_many_all_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'STORED\r\n',
            b'VALUE key1 0 6\r\nvalue1\r\n',
            b'VALUE key2 0 6\r\nvalue2\r\nEND\r\n',
        ])
        result = client.set(b'key1', b'value1', noreply=False)
        result = client.set(b'key2', b'value2', noreply=False)
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equal(result, {b'key1': b'value1', b'key2': b'value2'})

    def test_get_unicode_key(self):
        client = self.make_client([b''])

        def _get():
            client.get(u'\u0FFF')

        tools.assert_raises(MemcacheIllegalInputError, _get)

    def test_delete_not_found(self):
        client = self.make_client([b'NOT_FOUND\r\n'])
        result = client.delete(b'key', noreply=False)
        tools.assert_equal(result, False)

    def test_delete_found(self):
        client = self.make_client([b'STORED\r', b'\n', b'DELETED\r\n'])
        result = client.add(b'key', b'value', noreply=False)
        result = client.delete(b'key', noreply=False)
        tools.assert_equal(result, True)

    def test_delete_noreply(self):
        client = self.make_client([])
        result = client.delete(b'key', noreply=True)
        tools.assert_equal(result, True)

    def test_incr_not_found(self):
        client = self.make_client([b'NOT_FOUND\r\n'])
        result = client.incr(b'key', 1, noreply=False)
        tools.assert_equal(result, None)

    def test_incr_found(self):
        client = self.make_client([b'STORED\r\n', b'1\r\n'])
        client.set(b'key', 0, noreply=False)
        result = client.incr(b'key', 1, noreply=False)
        tools.assert_equal(result, 1)

    def test_incr_noreply(self):
        client = self.make_client([b'STORED\r\n'])
        client.set(b'key', 0, noreply=False)

        client = self.make_client([])
        result = client.incr(b'key', 1, noreply=True)
        tools.assert_equal(result, None)

    def test_decr_not_found(self):
        client = self.make_client([b'NOT_FOUND\r\n'])
        result = client.decr(b'key', 1, noreply=False)
        tools.assert_equal(result, None)

    def test_decr_found(self):
        client = self.make_client([b'STORED\r\n', b'1\r\n'])
        client.set(b'key', 2, noreply=False)
        result = client.decr(b'key', 1, noreply=False)
        tools.assert_equal(result, 1)


class TestClient(ClientTestMixin, unittest.TestCase):

    Client = Client

    def test_append_stored(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.append(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)

    def test_prepend_stored(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.prepend(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)

    def test_cas_stored(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.cas(b'key', b'value', b'cas', noreply=False)
        tools.assert_equal(result, True)

    def test_cas_exists(self):
        client = self.make_client([b'EXISTS\r\n'])
        result = client.cas(b'key', b'value', b'cas', noreply=False)
        tools.assert_equal(result, False)

    def test_cas_not_found(self):
        client = self.make_client([b'NOT_FOUND\r\n'])
        result = client.cas(b'key', b'value', b'cas', noreply=False)
        tools.assert_equal(result, None)

    def test_cr_nl_boundaries(self):
        client = self.make_client([b'VALUE key1 0 6\r',
                                   b'\nvalue1\r\n'
                                   b'VALUE key2 0 6\r\n',
                                   b'value2\r\n'
                                   b'END\r\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})

        client = self.make_client([b'VALUE key1 0 6\r\n',
                                   b'value1\r',
                                   b'\nVALUE key2 0 6\r\n',
                                   b'value2\r\n',
                                   b'END\r\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})

        client = self.make_client([b'VALUE key1 0 6\r\n',
                                   b'value1\r\n',
                                   b'VALUE key2 0 6\r',
                                   b'\nvalue2\r\n',
                                   b'END\r\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})


        client = self.make_client([b'VALUE key1 0 6\r\n',
                                   b'value1\r\n',
                                   b'VALUE key2 0 6\r\n',
                                   b'value2\r',
                                   b'\nEND\r\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})

        client = self.make_client([b'VALUE key1 0 6\r\n',
                                   b'value1\r\n',
                                   b'VALUE key2 0 6\r\n',
                                   b'value2\r\n',
                                   b'END\r',
                                   b'\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})

        client = self.make_client([b'VALUE key1 0 6\r',
                                   b'\nvalue1\r',
                                   b'\nVALUE key2 0 6\r',
                                   b'\nvalue2\r',
                                   b'\nEND\r',
                                   b'\n'])
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equals(result, {b'key1': b'value1', b'key2': b'value2'})

    def test_delete_exception(self):
        client = self.make_client([Exception('fail')])

        def _delete():
            client.delete(b'key', noreply=False)

        tools.assert_raises(Exception, _delete)
        tools.assert_equal(client.sock, None)

    def test_flush_all(self):
        client = self.make_client([b'OK\r\n'])
        result = client.flush_all(noreply=False)
        tools.assert_equal(result, True)

    def test_incr_exception(self):
        client = self.make_client([Exception('fail')])

        def _incr():
            client.incr(b'key', 1)

        tools.assert_raises(Exception, _incr)
        tools.assert_equal(client.sock, None)

    def test_get_error(self):
        client = self.make_client([b'ERROR\r\n'])

        def _get():
            client.get(b'key')

        tools.assert_raises(MemcacheUnknownCommandError, _get)

    def test_get_recv_chunks(self):
        client = self.make_client([b'VALUE key', b' 0 5\r', b'\nvalue',
                                   b'\r\n', b'END', b'\r', b'\n'])
        result = client.get(b'key')
        tools.assert_equal(result, b'value')

    def test_get_unknown_error(self):
        client = self.make_client([b'foobarbaz\r\n'])

        def _get():
            client.get(b'key')

        tools.assert_raises(MemcacheUnknownError, _get)

    def test_gets_not_found(self):
        client = self.make_client([b'END\r\n'])
        result = client.gets(b'key')
        tools.assert_equal(result, (None, None))

    def test_gets_found(self):
        client = self.make_client([b'VALUE key 0 5 10\r\nvalue\r\nEND\r\n'])
        result = client.gets(b'key')
        tools.assert_equal(result, (b'value', b'10'))

    def test_gets_many_none_found(self):
        client = self.make_client([b'END\r\n'])
        result = client.gets_many([b'key1', b'key2'])
        tools.assert_equal(result, {})

    def test_gets_many_some_found(self):
        client = self.make_client([b'VALUE key1 0 6 11\r\nvalue1\r\nEND\r\n'])
        result = client.gets_many([b'key1', b'key2'])
        tools.assert_equal(result, {b'key1': (b'value1', b'11')})

    def test_touch_not_found(self):
        client = self.make_client([b'NOT_FOUND\r\n'])
        result = client.touch(b'key', noreply=False)
        tools.assert_equal(result, False)

    def test_touch_found(self):
        client = self.make_client([b'TOUCHED\r\n'])
        result = client.touch(b'key', noreply=False)
        tools.assert_equal(result, True)

    def test_quit(self):
        client = self.make_client([])
        result = client.quit()
        tools.assert_equal(result, None)
        tools.assert_equal(client.sock, None)

    def test_replace_stored(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.replace(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)

    def test_replace_not_stored(self):
        client = self.make_client([b'NOT_STORED\r\n'])
        result = client.replace(b'key', b'value', noreply=False)
        tools.assert_equal(result, False)

    def test_serialization(self):
        def _ser(key, value):
            return json.dumps(value), 0

        client = self.make_client([b'STORED\r\n'], serializer=_ser)
        client.set('key', {'c': 'd'})
        tools.assert_equal(client.sock.send_bufs, [
            b'set key 0 0 10 noreply\r\n{"c": "d"}\r\n'
        ])

    def test_set_socket_handling(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.set(b'key', b'value', noreply=False)
        tools.assert_equal(result, True)
        tools.assert_equal(client.sock.closed, False)
        tools.assert_equal(len(client.sock.send_bufs), 1)

    def test_set_error(self):
        client = self.make_client([b'ERROR\r\n'])

        def _set():
            client.set(b'key', b'value', noreply=False)

        tools.assert_raises(MemcacheUnknownCommandError, _set)

    def test_set_exception(self):
        client = self.make_client([Exception('fail')])

        def _set():
            client.set(b'key', b'value', noreply=False)

        tools.assert_raises(Exception, _set)
        tools.assert_equal(client.sock, None)

    def test_set_client_error(self):
        client = self.make_client([b'CLIENT_ERROR some message\r\n'])

        def _set():
            client.set('key', 'value', noreply=False)

        tools.assert_raises(MemcacheClientError, _set)

    def test_set_server_error(self):
        client = self.make_client([b'SERVER_ERROR some message\r\n'])

        def _set():
            client.set(b'key', b'value', noreply=False)

        tools.assert_raises(MemcacheServerError, _set)

    def test_set_unknown_error(self):
        client = self.make_client([b'foobarbaz\r\n'])

        def _set():
            client.set(b'key', b'value', noreply=False)

        tools.assert_raises(MemcacheUnknownError, _set)

    def test_set_many_socket_handling(self):
        client = self.make_client([b'STORED\r\n'])
        result = client.set_many({b'key': b'value'}, noreply=False)
        tools.assert_equal(result, True)
        tools.assert_equal(client.sock.closed, False)
        tools.assert_equal(len(client.sock.send_bufs), 1)

    def test_set_many_exception(self):
        client = self.make_client([b'STORED\r\n', Exception('fail')])

        def _set():
            client.set_many({b'key': b'value', b'other': b'value'},
                            noreply=False)

        tools.assert_raises(Exception, _set)
        tools.assert_equal(client.sock, None)

    def test_stats(self):
        client = self.make_client([b'STAT fake_stats 1\r\n', b'END\r\n'])
        result = client.stats()
        tools.assert_equal(client.sock.send_bufs, [
            b'stats \r\n'
        ])
        tools.assert_equal(result, {b'fake_stats': 1})

    def test_stats_with_args(self):
        client = self.make_client([b'STAT fake_stats 1\r\n', b'END\r\n'])
        result = client.stats('some_arg')
        tools.assert_equal(client.sock.send_bufs, [
            b'stats some_arg\r\n'
        ])
        tools.assert_equal(result, {b'fake_stats': 1})

    def test_stats_conversions(self):
        client = self.make_client([
            # Most stats are converted to int
            b'STAT cmd_get 2519\r\n',
            b'STAT cmd_set 3099\r\n',

            # Unless they can't be, they remain str
            b'STAT libevent 2.0.19-stable\r\n',

            # Some named stats are explicitly converted
            b'STAT hash_is_expanding 0\r\n',
            b'STAT rusage_user 0.609165\r\n',
            b'STAT rusage_system 0.852791\r\n',
            b'STAT slab_reassign_running 1\r\n',
            b'STAT version 1.4.14\r\n',
            b'END\r\n',
        ])
        result = client.stats()
        tools.assert_equal(client.sock.send_bufs, [
            b'stats \r\n'
        ])
        expected = {
            b'cmd_get': 2519,
            b'cmd_set': 3099,
            b'libevent': b'2.0.19-stable',
            b'hash_is_expanding': False,
            b'rusage_user': 0.609165,
            b'rusage_system': 0.852791,
            b'slab_reassign_running': True,
            b'version': b'1.4.14',
        }
        tools.assert_equal(result, expected)

    def test_python_dict_set_is_supported(self):
        client = self.make_client([b'STORED\r\n'])
        client[b'key'] = b'value'

    def test_python_dict_get_is_supported(self):
        client = self.make_client([b'VALUE key 0 5\r\nvalue\r\nEND\r\n'])
        tools.assert_equal(client[b'key'], b'value')

    def test_python_dict_get_not_found_is_supported(self):
        client = self.make_client([b'END\r\n'])

        def _get():
            _ = client[b'key']

        tools.assert_raises(KeyError, _get)

    def test_python_dict_del_is_supported(self):
        client = self.make_client([b'DELETED\r\n'])
        del client[b'key']

    def test_too_long_key(self):
        client = self.make_client([b'END\r\n'])
        tools.assert_raises(MemcacheClientError, client.get, b'x' * 251)

    def test_key_contains_spae(self):
        client = self.make_client([b'END\r\n'])
        tools.assert_raises(MemcacheClientError, client.get, b'abc xyz')

    def test_key_contains_nonascii(self):
        client = self.make_client([b'END\r\n'])
        tools.assert_raises(MemcacheClientError, client.get, u'\u3053\u3093\u306b\u3061\u306f')


class TestClientSocketConnect(unittest.TestCase):
    def test_socket_connect(self):
        server = ("example.com", 11211)

        client = Client(server, socket_module=MockSocketModule())
        client._connect()
        tools.assert_equal(client.sock.connections, [server])

        timeout = 2
        connect_timeout = 3
        client = Client(server, connect_timeout=connect_timeout, timeout=timeout,
                        socket_module=MockSocketModule())
        client._connect()
        tools.assert_equal(client.sock.timeouts, [connect_timeout, timeout])

        client = Client(server, socket_module=MockSocketModule())
        client._connect()
        tools.assert_equal(client.sock.socket_options, [])

        client = Client(server, socket_module=MockSocketModule(), no_delay=True)
        client._connect()
        tools.assert_equal(client.sock.socket_options, [(socket.IPPROTO_TCP,
                                                        socket.TCP_NODELAY, 1)])


class TestPooledClient(ClientTestMixin, unittest.TestCase):
    def make_client(self, mock_socket_values, serializer=None):
        mock_client = Client(None, serializer=serializer)
        mock_client.sock = MockSocket(list(mock_socket_values))
        client = PooledClient(None, serializer=serializer)
        client.client_pool = pool.ObjectPool(lambda: mock_client)
        return client


class TestMockClient(ClientTestMixin, unittest.TestCase):
    def make_client(self, mock_socket_values, serializer=None):
        client = MockMemcacheClient(None, serializer=serializer)
        client.sock = MockSocket(list(mock_socket_values))
        return client


class TestPrefixedClient(ClientTestMixin, unittest.TestCase):
    def make_client(self, mock_socket_values, serializer=None):
        client = Client(None, serializer=serializer, key_prefix=b'xyz:')
        client.sock = MockSocket(list(mock_socket_values))
        return client

    def test_get_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'VALUE xyz:key 0 5\r\nvalue\r\nEND\r\n',
        ])
        result = client.set(b'key', b'value', noreply=False)
        result = client.get(b'key')
        tools.assert_equal(result, b'value')

    def test_get_many_some_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'VALUE xyz:key1 0 6\r\nvalue1\r\nEND\r\n',
        ])
        result = client.set(b'key1', b'value1', noreply=False)
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equal(result, {b'key1': b'value1'})

    def test_get_many_all_found(self):
        client = self.make_client([
            b'STORED\r\n',
            b'STORED\r\n',
            b'VALUE xyz:key1 0 6\r\nvalue1\r\n',
            b'VALUE xyz:key2 0 6\r\nvalue2\r\nEND\r\n',
        ])
        result = client.set(b'key1', b'value1', noreply=False)
        result = client.set(b'key2', b'value2', noreply=False)
        result = client.get_many([b'key1', b'key2'])
        tools.assert_equal(result, {b'key1': b'value1', b'key2': b'value2'})

    def test_python_dict_get_is_supported(self):
        client = self.make_client([b'VALUE xyz:key 0 5\r\nvalue\r\nEND\r\n'])
        tools.assert_equal(client[b'key'], b'value')


class TestPrefixedPooledClient(TestPrefixedClient):
    def make_client(self, mock_socket_values, serializer=None):
        mock_client = Client(None, serializer=serializer, key_prefix=b'xyz:')
        mock_client.sock = MockSocket(list(mock_socket_values))
        client = PooledClient(None, serializer=serializer, key_prefix=b'xyz:')
        client.client_pool = pool.ObjectPool(lambda: mock_client)
        return client
