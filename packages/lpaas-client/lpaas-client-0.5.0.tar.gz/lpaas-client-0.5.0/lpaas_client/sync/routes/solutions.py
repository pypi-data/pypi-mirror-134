from datetime import timedelta
from typing import Union

from lpaas_client.core.model.goal import GoalName
from lpaas_client.core.model.solution import Hook, Solution
from lpaas_client.core.routes.solutionBaseRoute import SolutionsBaseRoute
from lpaas_client.core.model.theory import TheoryName
from lpaas_client.sync.routes.auth import AuthClient


class SolutionsClient(AuthClient, SolutionsBaseRoute):

    def add_new_solution(self,
                         theory_name: Union[TheoryName, str],
                         goal_name: Union[GoalName, str],
                         hook: Union[Hook, None] = None,
                         skip: Union[int, None] = None,
                         limit: Union[int, None] = None,
                         within: Union[timedelta, None] = None,
                         every: Union[timedelta, None] = None,
                         ) -> Solution:
        with self.get_client() as client:
            response = client.send(
                self._build_add_new_solution_request(client, TheoryName(theory_name), GoalName(goal_name), hook, skip, limit, within, every))
        return self._handle_add_new_solution_response(response, TheoryName(theory_name), GoalName(goal_name))

    def get_hook(self, hook: Hook, version: Union[int, None] = None) -> Solution:
        with self.get_client() as client:
            response = client.send(self._build_get_hook_request(client, hook, version))
        return self._handle_get_hook_response(response)

    def get_hooks(self):
        with self.get_client() as client:
            response = client.send(self._build_get_hooks_request(client))
        return self._handle_get_hooks_response(response)

    def remove_all(self) -> None:
        with self.get_client() as client:
            response = client.send(self._build_remove_all_request(client))
        return self._handle_remove_all_response(response)

    def remove_hook(self, hook: Hook, version: Union[int, None] = None) -> None:
        with self.get_client() as client:
            response = client.send(self._build_remove_hook_request(client, hook, version))
        return self._handle_remove_hook_response(response, hook)
