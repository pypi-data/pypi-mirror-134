from typing import Union

from lpaas_client.asyn.async_client import AsyncClient
from lpaas_client.core.exception.exception import Unauthorized
from lpaas_client.core.model.auth import AuthData, TOKEN
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute


def repeat_on_unauthorized_async(methods):
    """A decorator to repeat a request on an Unauthorized error

    :param methods: Should be a valid method of a class the extend AuthClient in the async version
    """

    async def _repeat_on_unauthorized(*args, **kwargs):
        try:
            return await methods(*args, **kwargs)
        except Unauthorized:
            self = args[0]
            await self.authenticate()
            return await methods(*args, **kwargs)

    return _repeat_on_unauthorized


class AuthClient(AsyncClient, AuthBaseRoute):
    """Extend synchronous client to support authentication"""

    user_data: Union[AuthData, None] = None
    token: Union[str, None] = None

    async def authenticate(self, data: Union[AuthData, None] = None) -> TOKEN:
        """ Authenticate the user with the server.

        You can call this method with `data = None`
        and it will use the previous used credential, if any.

        :param data: optional, the authentication data to use
        :return: the token
        """
        async with self._get_client() as client:
            response = await client.send(self._build_auth_request(client, data))
        return self._handle_auth_response(response)

    async def get_or_create_token(self, data: Union[AuthData, None] = None) -> TOKEN:
        """Create the token if it did not exists and return it."""
        if self.token is None:
            await self.authenticate(data)
        return self.get_token()
