from typing import Union

from httpx import URL

from lpaas_client.asyn.routes.goals import GoalClient as __GoalClient
from lpaas_client.asyn.routes.theories import TheoriesClient as __TheoriesClient
from lpaas_client.asyn.routes.solutions import SolutionsClient as __SolutionsClient

class LPClient(__GoalClient, __TheoriesClient, __SolutionsClient):
    """Logical Programming Client

    Implements all the utilities to communicate with LPaaS

    This is an async version of :class:`lpaas_client.sync.LPClient`
    """
