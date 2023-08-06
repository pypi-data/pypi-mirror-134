from abc import ABC
from typing import Union

from http_constants.headers import HttpHeaders
from http_constants.status import HttpStatus
from httpx import Response, Request

from lpaas_client.core.client.baseclient import BaseClient
from lpaas_client.core.exception.exception import Unauthorized
from lpaas_client.core.model.auth import AuthData, TOKEN


class AuthBaseRoute(BaseClient, ABC):
    """Extend BaseClient

    Represents the core of the Authentication route giving all the methods to:

    - build all the `httpx.Request`
    - handle all the `httpx.Response`

    of the '/lpaas/auth' path for LPaaS
    """
    user_data: Union[AuthData, None] = None
    token: Union[str, None] = None

    def __get_user_data(self, data: Union[AuthData, None] = None) -> AuthData:
        if data is not None:
            self.user_data = data
            return data
        if self.user_data is not None:
            return self.user_data
        raise ValueError('Missing user name and password')

    @staticmethod
    def _check_auth_response(response: Response) -> None:
        """Check if the response fail due to auth purpose"""
        if response.status_code == HttpStatus.UNAUTHORIZED:
            raise Unauthorized('Invalid username and/or password')
        if response.status_code == HttpStatus.FORBIDDEN:
            raise Unauthorized('The server refuse the authentication')

    def _build_auth_request(self, client, data: AuthData) -> Request:
        """Build a Request for server authentication

        :param client: that support `build_request` method
        :type client: httpx.Client or any other class that support a `build_request` method
        :param data: to be add to the content of the request
        :return: a new request
        :rtype: :ref:`Request<httpx.Request>`
        """
        curr_data = self.__get_user_data(data)
        body = {
            'username': curr_data.username,
            'password': curr_data.password
        }
        return client.build_request("POST",
                                    self.get_url('auth'),
                                    headers={HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json},
                                    json=body)

    def _handle_auth_response(self, response: Response) -> TOKEN:
        """

        :param response: to an auth_request
        :type response: Response
        :return: the token
        :rtype: TOKEN
        """
        self._check_auth_response(response)
        self._check_response(response)
        if 'token' in response.json():
            self.token = response.json()['token']
        else:
            raise ValueError('Unable to authenticate')
        return self.token

    def get_token(self) -> TOKEN:
        """Return the current token, or raise an exception if it is not present."""
        if self.token is None:
            raise ValueError('No available token')
        return self.token

    def _add_jwt_token(self, header: Union[dict, None] = None) -> dict:
        """Create/add JWT token to a dict

        :param header: the current header or None if no header is present
        :type header: dict
        :return: a dict with filed 'Authorization' filled
        :rtype: dict
        """
        if header is None:
            header = {}
        header['Authorization'] = self.get_token()
        return header