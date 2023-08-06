from lpaas_client.sync.routes.goals import GoalClient as __GoalClient
from lpaas_client.sync.routes.theories import TheoriesClient as __TheoriesClient
from lpaas_client.sync.routes.solutions import SolutionsClient as __SolutionsClient


class LPClient(__GoalClient, __TheoriesClient, __SolutionsClient):
    """Logical Programming Client

    Implements all the utilities to communicate with LPaaS

    This is the synchronous version of the client

    Every time you call a method the client will create a new transport layer
    to reuse the same session and optimize performance you can use the context manager `with`
    like this

    >>> client = LPClient('url')
    >>> with client:
    >>>     client.authenticate(...)
    >>>     result = client.operation(...)
    >>>     ...

    In this way all the operations will use the same client
    and reduce the time required to send a request to the server.
    """
