import typing
from typing import Union

import httpx
from httpx import Request, Response
from httpx._client import UseClientDefault, USE_CLIENT_DEFAULT
from httpx._types import URLTypes, RequestContent, RequestData, RequestFiles, QueryParamTypes, HeaderTypes, CookieTypes, \
    TimeoutTypes

from lpaas_client.core.client.baseclient import BaseClient


class SyncClient(BaseClient):
    """TODO add doc

    how to use?

    """
    __curr_client: Union[httpx.Client, None] = None
    __latch_count: int = 0

    def get_client(self):
        if self.__latch_count > 0:
            if self.__curr_client is None or self.__curr_client.is_closed:
                raise ValueError('Client already closed')
            return self
        return httpx.Client(base_url=self.base_url)

    def __enter__(self):
        self.__latch_count += 1
        if self.__latch_count == 1:
            self.__curr_client = httpx.Client(base_url=self.base_url)
            self.__curr_client.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__latch_count > 1:
            self.__latch_count -= 1
            return
        if self.__latch_count <= 0 or self.__curr_client is None or self.__curr_client.is_closed:
            raise ValueError('Can not close the client, it is already closed')
        self.__latch_count -= 1
        self.__curr_client.close()
        del self.__curr_client

    def send(self, request: Request) -> Response:
        """This method is the equivalent of `httpx.Client.send`"""
        if self.__curr_client is None or self.__curr_client.is_closed:
            raise ValueError('No available client, ensure to call this inside a with statement'
                             'e.g'
                             'with SyncClient as c:'
                             '\tc.send(request)')
        return self.__curr_client.send(request)

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
