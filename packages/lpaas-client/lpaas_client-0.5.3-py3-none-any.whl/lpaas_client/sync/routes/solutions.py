from datetime import timedelta
from typing import Union

from lpaas_client.core.model.goal import GoalName
from lpaas_client.core.model.solution import Hook, Solution
from lpaas_client.core.routes.solutionBaseRoute import SolutionsBaseRoute
from lpaas_client.core.model.theory import TheoryName
from lpaas_client.sync.routes.auth import AuthClient, repeat_on_unauthorized


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
        """Creates a new solution-set request.

        :param theory_name: the name of the theory to be used for the solution
        :param goal_name: the name of the goal list to be used for the solution
        :param hook: a hook for this solution, useful to retrieve results in the future
        :param skip: The resolution process skips the first `skip` solutions
            providing as a result the other ones respecting their oder.
        :param limit: The produced solution-set will contain no more than limit solutions.
        :param within: The produced solution-set will contain no more than limit solutions.
        :param every: Optional parameter defining whether this request should create
            a time-related stream of solutions or not.
        :return: the first solution created
        """
        with self._get_client() as client:
            response = client.send(
                self._build_add_new_solution_request(client, TheoryName(theory_name), GoalName(goal_name), hook, skip, limit, within, every))
        return self._handle_add_new_solution_response(response, TheoryName(theory_name), GoalName(goal_name))

    def get_hook(self, hook: Hook, version: Union[int, None] = None) -> Solution:
        """Retrieves a version of a solution-set

        :param hook: the hook of the solution
        :param version: optional version number, None means the last available solution
        :return: the corresponding solution
        """
        with self._get_client() as client:
            response = client.send(self._build_get_hook_request(client, hook, version))
        return self._handle_get_hook_response(response)

    def get_hooks(self):
        """Retrieves the list of available hooks"""
        with self._get_client() as client:
            response = client.send(self._build_get_hooks_request(client))
        return self._handle_get_hooks_response(response)

    @repeat_on_unauthorized
    def remove_all_solutions(self) -> None:
        """Remove all the solutions, and cancel all remote executions

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        with self._get_client() as client:
            response = client.send(self._build_remove_all_request(client))
        return self._handle_remove_all_response(response)

    @repeat_on_unauthorized
    def remove_hook(self, hook: Hook, version: Union[int, None] = None) -> None:
        """Remove a solution

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param hook: the hook referring to the solution
        :param version: optional version number, if no version is specify all versions are removed
        """
        with self._get_client() as client:
            response = client.send(self._build_remove_hook_request(client, hook, version))
        return self._handle_remove_hook_response(response, hook)
