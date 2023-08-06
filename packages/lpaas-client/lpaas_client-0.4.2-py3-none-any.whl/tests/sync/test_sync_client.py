from unittest import TestCase

import httpx
import respx
from httpx import URL, Request

from lpaas_client.sync.sync_client import SyncClient


base_url = URL('http://localhost:8080/lpaas')


class TestSyncClient(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.client = SyncClient(base_url)

    def test_get_client(self):
        self.assertIsInstance(self.client.get_client(), httpx.Client)

    def test_get_client_with_context_manager(self):
        with self.client:
            self.assertIsInstance(self.client, SyncClient)
            # In the context manager of the client the actual client is not usable
            # you have to use `send` and `build_request` wrapper method
            self.assertEqual(self.client.get_client(), self.client)

    @respx.mock
    def test_send(self):
        request = respx.get(base_url) % 204
        with self.client:
            response = self.client.send(Request('GET', base_url))
        self.assertTrue(request.called)
        self.assertEqual(response.status_code, 204)

    @respx.mock
    def test_send_raise_exception(self):
        request = respx.get(base_url) % 204
        with self.assertRaises(ValueError):
            self.client.send(Request('GET', base_url))
        self.assertFalse(request.called)

    def test_build_request(self):
        with self.client:
            request = self.client.build_request('GET', base_url)
        self.assertEqual(request.url, base_url)
        self.assertEqual(request.method, 'GET')

    def test_build_request_raise_exception(self):
        with self.assertRaises(ValueError):
            self.client.build_request('GET', base_url)
