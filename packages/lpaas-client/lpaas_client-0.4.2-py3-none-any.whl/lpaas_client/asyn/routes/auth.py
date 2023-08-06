from typing import Union

from lpaas_client.asyn.async_client import AsyncClient
from lpaas_client.core.model.auth import AuthData, TOKEN
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute


class AuthClient(AsyncClient, AuthBaseRoute):
    """Extend synchronous client to support authentication"""

    user_data: Union[AuthData, None] = None
    token: Union[str, None] = None

    async def authenticate(self, data: Union[AuthData, None] = None) -> TOKEN:
        """ Authenticate the user with the server.

        You can call this method with `data = None`
        and it will use the previous used credential, if any.

        :param data: optional, the authentication data to use
        :type data: AuthData
        :return: the token
        :rtype: str
        """
        async with self.get_client() as client:
            response = await client.send(self._build_auth_request(client, data))
        return self._handle_auth_response(response)

    async def get_or_create_token(self, data: Union[AuthData, None] = None) -> TOKEN:
        """Create the token if it did not exists and return it."""
        if self.token is None:
            await self.authenticate(data)
        return self.get_token()
