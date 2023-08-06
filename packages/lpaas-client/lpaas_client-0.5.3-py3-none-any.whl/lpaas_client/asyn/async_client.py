import typing
from typing import Union

import httpx
from httpx import Request, Response, USE_CLIENT_DEFAULT
from httpx._client import UseClientDefault
from httpx._types import URLTypes, RequestData, RequestContent, RequestFiles, QueryParamTypes, HeaderTypes, CookieTypes, \
    TimeoutTypes

from lpaas_client.core.client.baseclient import BaseClient


class AsyncClient(BaseClient):
    """Asynchronous client manager

    allows user to reuse the same client throw context-manager

    e.g.

    >>> c = AsyncClient()
    >>> async with c:
    >>>     request = c.build_request('GET', 'some_url')
    >>>     await c.send(request)
    >>>     await c.send(request)

    both requests reuse the same client

    """
    __curr_client: Union[httpx.AsyncClient, None] = None
    __latch_count: int = 0

    def _get_client(self):
        """Return the preexisting client if called inside a context manager
            otherwise it creates a fresh client
        """
        if self.__latch_count > 0:
            if self.__curr_client is None or self.__curr_client.is_closed:
                raise ValueError('Client already closed')
            return self
        return httpx.AsyncClient(base_url=self.base_url)

    async def __aenter__(self):
        self.__latch_count += 1
        if self.__latch_count == 1:
            self.__curr_client = httpx.AsyncClient(base_url=self.base_url)
            await self.__curr_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.__latch_count > 1:
            self.__latch_count -= 1
            return
        if self.__latch_count <= 0 or self.__curr_client is None or self.__curr_client.is_closed:
            raise ValueError('Can not close the client, it is already closed')
        self.__latch_count -= 1
        await self.__curr_client.aclose()
        del self.__curr_client

    async def send(self, request: Request) -> Response:
        """This method is the equivalent of `httpx.Client.send`"""
        if self.__curr_client is None or self.__curr_client.is_closed:
            raise ValueError('No available client, ensure to call this inside a with statement'
                             'e.g'
                             'with SyncClient as c:'
                             '\tc.send(request)')
        return await self.__curr_client.send(request)

    def build_request(self,
                      method: str,
                      url: URLTypes,
                      *,
                      content: RequestContent = None,
                      data: RequestData = None,
                      files: RequestFiles = None,
                      json: typing.Any = None,
                      params: QueryParamTypes = None,
                      headers: HeaderTypes = None,
                      cookies: CookieTypes = None,
                      timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
                      extensions: dict = None,
                      ) -> Request:
        """This method is the equivalent of `httpx.Client.build_request`"""
        if self.__curr_client is None or self.__curr_client.is_closed:
            raise ValueError('No available client, ensure to call this inside a with statement'
                             'e.g'
                             'with SyncClient as c:'
                             '\tc.build_request(request)')
        return self.__curr_client.build_request(method, url,
                                                content=content,
                                                data=data,
                                                files=files,
                                                json=json,
                                                params=params,
                                                headers=headers,
                                                cookies=cookies,
                                                timeout=timeout,
                                                extensions=extensions)
