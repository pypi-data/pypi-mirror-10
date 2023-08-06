import unittest
import random
import json
from cStringIO import StringIO
from contextlib import contextmanager

from mock import MagicMock as Mock

import oiopy
from oiopy import utils
from oiopy import fakes
from oiopy import exceptions
from oiopy.object_storage import container_headers, object_headers
from oiopy.object_storage import handle_object_not_found
from oiopy.object_storage import handle_container_not_found
from oiopy.object_storage import _sort_chunks


@contextmanager
def set_http_connect(*args, **kwargs):
    old = oiopy.object_storage.http_connect

    new = fakes.fake_http_connect(*args, **kwargs)
    try:
        oiopy.object_storage.http_connect = new
        yield new
        unused_status = list(new.status_iter)
        if unused_status:
            raise AssertionError('unused status %r' % unused_status)

    finally:
        oiopy.object_storage.http_connect = old


def empty_stream():
    return StringIO("")


class ObjectStorageTest(unittest.TestCase):
    def setUp(self):
        self.api = fakes.FakeStorageAPI("NS", "http://1.2.3.4:8000")
        self.account = "test"
        self.container = "fake"
        self.headers = {"x-req-id": utils.random_string()}
        self.uri_base = "m2/NS/%s" % self.account

    def test_handle_container_not_found(self):
        @handle_container_not_found
        def test(self, account, container):
            raise exceptions.NotFound("No container")

        container = utils.random_string()
        self.assertRaises(exceptions.NoSuchContainer, test, self, self.account,
                          container)

    def test_handle_object_not_found(self):
        @handle_object_not_found
        def test(self, account, container, obj):
            raise exceptions.NotFound("No object")

        obj = utils.random_string()
        self.assertRaises(exceptions.NoSuchObject, test, self, self.account,
                          self.container, obj)

    def test_container_list(self):
        resp = fakes.FakeResponse()
        name = utils.random_string()
        marker = utils.random_string()
        delimiter = utils.random_string()
        end_marker = utils.random_string()
        prefix = utils.random_string()
        limit = random.randint(1, 1000)
        body = {"listing": [[name, 0, 0, 0]]}
        self.api._request = Mock(return_value=(resp, body))
        self.api._get_account_url = Mock(return_value='fake_endpoint')
        containers, meta = self.api.container_list(self.account, limit=limit,
                                                   marker=marker,
                                                   prefix=prefix,
                                                   delimiter=delimiter,
                                                   end_marker=end_marker,
                                                   headers=self.headers)
        params = {"id": self.account, "prefix": prefix, "delimiter": delimiter,
                  "marker": marker, "end_marker": end_marker, "limit": limit}
        uri = "v1.0/account/containers"
        self.api._request.assert_called_once_with('GET', uri,
                                                  endpoint='fake_endpoint',
                                                  params=params,
                                                  headers=self.headers)
        self.assertEqual(len(containers), 1)

    def test_object_list(self):
        api = self.api
        marker = utils.random_string()
        delimiter = utils.random_string()
        end_marker = utils.random_string()
        prefix = utils.random_string()
        limit = random.randint(1, 1000)
        qs = "marker=%s&max=%s&delimiter=%s&prefix=%s&end_marker=%s" % (
            marker, limit, delimiter, prefix, end_marker)
        uri = "%s/%s?%s" % (self.uri_base, self.container, qs)
        name0 = utils.random_string()
        name1 = utils.random_string()
        resp_body = {"objects": [{"name": name0}, {"name": name1}]}
        api._request = Mock(return_value=(None, resp_body))
        l = api.object_list(self.account, self.container, limit=limit,
                            marker=marker, prefix=prefix,
                            delimiter=delimiter, end_marker=end_marker,
                            headers=None)
        api._request.assert_called_once_with('GET', uri, headers=None)
        self.assertEqual(len(l['objects']), 2)

    def test_container_show(self):
        api = self.api
        resp = fakes.FakeResponse()
        name = utils.random_string()
        cont_size = random.randint(1, 1000)
        resp.headers = {
            container_headers["size"]: cont_size
        }
        api._request = Mock(return_value=(resp, None))
        uri = "%s/%s/action" % (self.uri_base, name)
        info = api.container_show(self.account, name)
        data = json.dumps({'args': None, 'action': 'GetProperties'})
        api._request.assert_called_once_with('POST', uri, data=data,
                                             headers=None)

    def test_container_show_not_found(self):
        api = self.api
        api._request = Mock(side_effect=exceptions.NotFound("No container"))
        name = utils.random_string()
        self.assertRaises(exceptions.NoSuchContainer, api.container_show,
                          self.account, name)

    def test_container_create(self):
        api = self.api
        resp = fakes.FakeResponse()
        resp.status_code = 201
        api._request = Mock(return_value=(resp, None))
        api.directory.link = Mock(return_value=None)

        name = utils.random_string()
        api.container_create(self.account, name)
        uri = "%s/%s" % (self.uri_base, name)

        api.directory.link.assert_called_once_with(self.account, name, "meta2",
                                                   headers=None)
        api._request.assert_called_once_with('PUT', uri, headers=None)

    def test_container_delete(self):
        api = self.api

        resp = fakes.FakeResponse()
        resp.status_code = 204
        api._request = Mock(return_value=(resp, None))
        api.directory.unlink = Mock(return_value=None)
        name = utils.random_string()
        api.container_delete(self.account, name)

        uri = "%s/%s" % (self.uri_base, name)
        api.directory.unlink.assert_called_once_with(self.account, name,
                                                     "meta2",
                                                     headers=None)
        api._request.assert_called_once_with('DELETE', uri, headers=None)

    def test_container_delete_not_empty(self):
        api = self.api

        api._request = Mock(side_effect=exceptions.Conflict(""))
        api.directory.unlink = Mock(return_value=None)
        name = utils.random_string()

        self.assertRaises(exceptions.ContainerNotEmpty, api.container_delete,
                          self.account, name)

    def test_container_update(self):
        api = self.api

        name = utils.random_string()
        key = utils.random_string()
        value = utils.random_string()
        meta = {key: value}
        resp = fakes.FakeResponse()
        api._request = Mock(return_value=(resp, None))
        api.container_update(self.account, name, meta)

        uri = "%s/%s/action" % (self.uri_base, name)
        data = json.dumps({"action": "SetProperties", "args": meta})
        api._request.assert_called_once_with('POST', uri, data=data,
                                             headers=None)

    def test_object_show(self):
        api = self.api
        name = utils.random_string()
        size = random.randint(1, 1000)
        content_hash = utils.random_string()
        content_type = utils.random_string()
        resp = fakes.FakeResponse()
        resp.headers = {object_headers["name"]: name,
                        object_headers["size"]: size,
                        object_headers["hash"]: content_hash,
                        object_headers["content_type"]: content_type}
        api._request = Mock(return_value=(resp, {}))
        obj = api.object_show(self.account, self.container, name)

        uri = "%s/%s/%s/action" % (self.uri_base, self.container, utils.quote(
            name))

        data = json.dumps({"action": "GetProperties", "args": None})
        api._request.assert_called_once_with('POST', uri, data=data,
                                             headers=None)

    def test_object_create_no_data(self):
        api = self.api
        name = utils.random_string()
        self.assertRaises(exceptions.MissingData, api.object_create,
                          self.account, self.container, obj_name=name)

    def test_object_create_no_name(self):
        api = self.api
        self.assertRaises(exceptions.MissingName, api.object_create,
                          self.account, self.container, data="x")

    def test_object_create_no_content_length(self):
        api = self.api
        name = utils.random_string()
        f = Mock()
        self.assertRaises(exceptions.MissingContentLength, api.object_create,
                          self.account, self.container, f, obj_name=name)

    def test_object_create_missing_file(self):
        api = self.api
        name = utils.random_string()
        self.assertRaises(exceptions.FileNotFound, api.object_create,
                          self.account, self.container, name)

    def test_object_update(self):
        api = self.api

        name = utils.random_string()
        key = utils.random_string()
        value = utils.random_string()
        meta = {key: value}
        resp = fakes.FakeResponse()
        api._request = Mock(return_value=(resp, None))
        api.object_update(self.account, self.container, name, meta)

        uri = "%s/%s/%s/action" % (self.uri_base, self.container, name)
        data = json.dumps({'action': 'SetProperties', 'args': meta})
        api._request.assert_called_once_with('POST', uri, data=data,
                                             headers=None)

    def test_object_delete(self):
        api = self.api
        name = utils.random_string()
        resp_body = [
            {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
            {"url": "http://1.2.3.4:6000/BBBB", "pos": "1", "size": 32},
            {"url": "http://1.2.3.4:6000/CCCC", "pos": "2", "size": 32}
        ]
        api._request = Mock(return_value=(None, resp_body))

        api.object_delete(self.account, self.container, name)

        uri = "%s/%s/%s" % (self.uri_base, self.container, utils.quote(name))
        api._request.assert_called_once_with('DELETE', uri, headers=None)

    def test_object_delete_not_found(self):
        api = self.api
        name = utils.random_string()
        api._request = Mock(side_effect=exceptions.NotFound("No object"))
        self.assertRaises(exceptions.NoSuchObject, api.object_delete,
                          self.account, self.container, name)

    def test_object_store(self):
        api = self.api
        name = utils.random_string()
        raw_chunks = [
            {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
            {"url": "http://1.2.3.4:6000/BBBB", "pos": "1", "size": 32},
            {"url": "http://1.2.3.4:6000/CCCC", "pos": "2", "size": 32}
        ]
        api._request = Mock(return_value=(None, raw_chunks))
        with set_http_connect(201, 201, 201):
            api.object_create(self.account, self.container, obj_name=name,
                              data="x")

    def test_sort_chunks(self):
        raw_chunks = [
            {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
            {"url": "http://1.2.3.4:6000/BBBB", "pos": "0", "size": 32},
            {"url": "http://1.2.3.4:6000/CCCC", "pos": "1", "size": 32},
            {"url": "http://1.2.3.4:6000/DDDD", "pos": "1", "size": 32},
            {"url": "http://1.2.3.4:6000/EEEE", "pos": "2", "size": 32},
            {"url": "http://1.2.3.4:6000/FFFF", "pos": "2", "size": 32},
        ]
        chunks = _sort_chunks(raw_chunks, False)
        sorted_chunks = {
            0: [
                {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
                {"url": "http://1.2.3.4:6000/BBBB", "pos": "0", "size": 32}],
            1: [
                {"url": "http://1.2.3.4:6000/CCCC", "pos": "1", "size": 32},
                {"url": "http://1.2.3.4:6000/DDDD", "pos": "1", "size": 32}],
            2: [
                {"url": "http://1.2.3.4:6000/EEEE", "pos": "2", "size": 32},
                {"url": "http://1.2.3.4:6000/FFFF", "pos": "2", "size": 32}
            ]}
        self.assertEqual(chunks, sorted_chunks)
        raw_chunks = [
            {"url": "http://1.2.3.4:6000/AAAA", "pos": "0.0", "size": 32},
            {"url": "http://1.2.3.4:6000/BBBB", "pos": "0.1", "size": 32},
            {"url": "http://1.2.3.4:6000/CCCC", "pos": "0.p0", "size": 32},
            {"url": "http://1.2.3.4:6000/DDDD", "pos": "1.0", "size": 32},
            {"url": "http://1.2.3.4:6000/EEEE", "pos": "1.1", "size": 32},
            {"url": "http://1.2.3.4:6000/FFFF", "pos": "1.p0", "size": 32},
        ]
        chunks = _sort_chunks(raw_chunks, True)
        sorted_chunks = {
            0: {
                "0":
                    {"url": "http://1.2.3.4:6000/AAAA", "pos": "0.0",
                     "size": 32},
                "1":
                    {"url": "http://1.2.3.4:6000/BBBB", "pos": "0.1",
                     "size": 32},
                "p0":
                    {"url": "http://1.2.3.4:6000/CCCC", "pos": "0.p0",
                     "size": 32}
            },
            1: {
                "0":
                    {"url": "http://1.2.3.4:6000/DDDD", "pos": "1.0",
                     "size": 32},
                "1":
                    {"url": "http://1.2.3.4:6000/EEEE", "pos": "1.1",
                     "size": 32},
                "p0":
                    {"url": "http://1.2.3.4:6000/FFFF", "pos": "1.p0",
                     "size": 32}
            }}
        self.assertEqual(chunks, sorted_chunks)

    def test_put_stream_empty(self):
        api = self.api
        name = utils.random_string()
        chunks = {
            0: [
                {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
                {"url": "http://1.2.3.4:6000/BBBB", "pos": "0", "size": 32},
                {"url": "http://1.2.3.4:6000/CCCC", "pos": "0", "size": 32}
            ]
        }
        src = empty_stream()

        with set_http_connect(201, 201, 201):
            chunks, bytes_transferred, content_checksum = api._put_stream(
                name, src, {"content_length": 0}, chunks)

        final_chunks = [
            {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 0,
             "hash": "d41d8cd98f00b204e9800998ecf8427e"},
            {"url": "http://1.2.3.4:6000/BBBB", "pos": "0", "size": 0,
             "hash": "d41d8cd98f00b204e9800998ecf8427e"},
            {"url": "http://1.2.3.4:6000/CCCC", "pos": "0", "size": 0,
             "hash": "d41d8cd98f00b204e9800998ecf8427e"}
        ]
        self.assertEqual(final_chunks, chunks)
        self.assertEqual(bytes_transferred, 0)
        self.assertEqual(content_checksum, "d41d8cd98f00b204e9800998ecf8427e")

    def test_put_stream_connect_exception(self):
        api = self.api
        name = utils.random_string()
        chunks = {
            0: [
                {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32},
                {"url": "http://1.2.3.4:6000/BBBB", "pos": "0", "size": 32},
                {"url": "http://1.2.3.4:6000/CCCC", "pos": "0", "size": 32}
            ]
        }
        src = empty_stream()

        with set_http_connect(201, Exception(), Exception()):
            chunks, bytes_transferred, content_checksum = api._put_stream(
                name, src, {"content_length": 0}, chunks)
        self.assertEqual(len(chunks), 1)
        chunk = {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 0,
                 "hash": "d41d8cd98f00b204e9800998ecf8427e"}
        self.assertEqual(chunk, chunks[0])

    def test_put_stream_connect_timeout(self):
        api = self.api
        name = utils.random_string()
        chunks = {
            0: [
                {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32}
            ]
        }
        src = empty_stream()

        with set_http_connect(200, slow_connect=True):
            chunks, bytes_transferred, content_checksum = api. \
                _put_stream(name, src, {"content_length": 0}, chunks)

    def test_put_stream_client_timeout(self):
        api = self.api
        name = utils.random_string()
        chunks = {
            0: [
                {"url": "http://1.2.3.4:6000/AAAA", "pos": "0", "size": 32}
            ]
        }

        src = fakes.FakeTimeoutStream(5)

        with set_http_connect(200):
            self.assertRaises(exceptions.ClientReadTimeout, api._put_stream,
                              name, src, {"content_length": 1}, chunks)








