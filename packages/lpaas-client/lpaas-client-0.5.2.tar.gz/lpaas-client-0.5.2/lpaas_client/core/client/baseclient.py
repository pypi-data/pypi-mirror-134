from abc import ABC, abstractmethod
from typing import Union

from httpx import Response, URL
from http_constants.status import HttpStatus


class BaseClient(ABC):
    """Base client for LPaaS"""

    def __init__(self, base_url: Union[str, URL]):
        self.base_url = URL(base_url)

    def get_url(self, *path: str):
        return self.base_url.join('/'.join(['lpaas', *path]))

    def _check_response(self, response: Response) -> None:
        if not HttpStatus(response.status_code).is_2xx_successful():
            raise ValueError('Unhandled error!')

    @abstractmethod
    def get_client(self):
        """Get the client that have to be used to send requests to the server"""
        pass
