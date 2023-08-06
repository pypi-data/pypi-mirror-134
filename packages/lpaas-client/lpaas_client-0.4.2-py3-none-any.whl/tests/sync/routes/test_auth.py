import json
from unittest import TestCase

import respx
from httpx import URL, Response

from lpaas_client.core.exception.exception import Unauthorized
from lpaas_client.sync.routes.auth import AuthClient
from lpaas_client.core.model.auth import AuthData

base_url = URL('http://localhost:8080')


class TestAuthClient(TestCase):
    client: AuthClient

    @classmethod
    def setUp(cls) -> None:
        cls.client = AuthClient(base_url)

    def test_can_create_client(self):
        self.assertIsInstance(self.client, AuthClient)

    @respx.mock
    def test_authenticate_with_context(self):
        request = respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': 'jwt token value'}))

        with self.client:
            token = self.client.authenticate(AuthData('User', 'pass'))

        # token = self.client.authenticate(AuthData('User', 'pass'))
        self.assertTrue(request.called)
        self.assertEqual(json.loads(request.calls.last.request.content.decode('utf-8')),
                         {'username': 'User', 'password': 'pass'})
        self.assertEqual('jwt token value', token)

    @respx.mock
    def test_authenticate(self):
        request = respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': 'jwt token value'}))
        token = self.client.authenticate(AuthData('User', 'pass'))
        self.assertTrue(request.called)
        self.assertEqual(json.loads(request.calls.last.request.content.decode('utf-8')),
                         {'username': 'User', 'password': 'pass'})
        self.assertEqual('jwt token value', token)

    @respx.mock
    def test_get_token(self):
        token = 'jwt token value'
        respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': token}))
        self.client.authenticate(AuthData('User', 'pass'))
        self.assertEqual(self.client.get_token(), token)

    @respx.mock
    def test_get_or_create_token(self):
        token = 'jwt token value'
        respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': token}))
        self.assertEqual(self.client.get_or_create_token(AuthData('User', 'pass')), token)

    @respx.mock
    def test_add_jwt_token(self):
        token = 'jwt token value'
        respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': token}))
        self.client.authenticate(AuthData('User', 'pass'))
        self.assertEqual(self.client._add_jwt_token(), {'Authorization': token})

    @respx.mock
    def test_raise_exception_with_no_user_data(self):
        with self.assertRaises(ValueError):
            self.client.get_or_create_token()

        with self.assertRaises(ValueError):
            self.client.authenticate()

        with self.assertRaises(ValueError):
            self.client.get_token()

    @respx.mock
    def test_raise_exception_with_failed_auth(self):
        respx.post(base_url.join('/lpaas/auth')) % 401

        with self.assertRaises(Unauthorized):
            self.client.authenticate(AuthData('User', 'Pass'))
