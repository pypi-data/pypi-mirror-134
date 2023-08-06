from datetime import timedelta
from typing import Union

from lpaas_client.asyn.routes.auth import AuthClient
from lpaas_client.core.model.goal import GoalName
from lpaas_client.core.model.solution import Hook, Solution
from lpaas_client.core.routes.solutionBaseRoute import SolutionsBaseRoute
from lpaas_client.core.model.theory import TheoryName


class SolutionsClient(AuthClient, SolutionsBaseRoute):

    async def add_new_solution(self,
                         theory_name: TheoryName,
                         goal_name: GoalName,
                         hook: Union[Hook, None] = None,
                         skip: Union[int, None] = None,
                         limit: Union[int, None] = None,
                         within: Union[timedelta, None] = None,
                         every: Union[timedelta, None] = None,
                         ) -> Solution:
        async with self.get_client() as client:
            response = await client.send(
                self._build_add_new_solution_request(client, theory_name, goal_name, hook, skip, limit, within, every))
        return self._handle_add_new_solution_response(response, theory_name, goal_name)

    async def get_hook(self, hook: Hook, version: Union[int, None] = None) -> Solution:
        async with self.get_client() as client:
            response = await client.send(self._build_get_hook_request(client, hook, version))
        return self._handle_get_hook_response(response)

    async def get_hooks(self):
        async with self.get_client() as client:
            response = await client.send(self._build_get_hooks_request(client))
        return self._handle_get_hooks_response(response)

    async def remove_all(self) -> None:
        async with self.get_client() as client:
            response = await client.send(self._build_remove_all_request(client))
        return self._handle_remove_all_response(response)

    async def remove_hook(self, hook: Hook, version: Union[int, None] = None) -> None:
        async with self.get_client() as client:
            response = await client.send(self._build_remove_hook_request(client, hook, version))
        return self._handle_remove_hook_response(response, hook)
