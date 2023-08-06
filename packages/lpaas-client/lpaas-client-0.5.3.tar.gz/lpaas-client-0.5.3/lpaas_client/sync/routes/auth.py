from typing import Union

from lpaas_client.core.exception.exception import Unauthorized
from lpaas_client.sync.sync_client import SyncClient
from lpaas_client.core.model.auth import AuthData, TOKEN
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute


def repeat_on_unauthorized(methods):
    """A decorator to repeat a request on an Unauthorized error

    :param methods: Should be a valid method of a class the extend AuthClient
    """
    def _repeat_on_unauthorized(*args, **kwargs):
        try:
            return methods(*args, **kwargs)
        except Unauthorized:
            self = args[0]
            self.authenticate()
            return methods(*args, **kwargs)

    return _repeat_on_unauthorized


class AuthClient(SyncClient, AuthBaseRoute):
    """Extend synchronous client to support authentication"""

    user_data: Union[AuthData, None] = None
    token: Union[str, None] = None

    def authenticate(self, data: Union[AuthData, None] = None) -> TOKEN:
        """ Authenticate the user with the server.

        You can call this method with `data = None`
        and it will use the previous used credential, if any.

        :param data: optional, the authentication data to use
        :return: the token
        """
        with self._get_client() as client:
            response = client.send(self._build_auth_request(client, data))
        return self._handle_auth_response(response)

    def get_or_create_token(self, data: Union[AuthData, None] = None) -> TOKEN:
        """Create the token if it did not exists and return it."""
        if self.token is None:
            self.authenticate(data)
        return self.get_token()
