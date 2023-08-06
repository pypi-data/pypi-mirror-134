from typing import List, Union

from tuprolog.core import Term

from lpaas_client.sync.routes.auth import AuthClient
from lpaas_client.core.model.goal import GoalName, GoalList
from lpaas_client.core.routes.goalBaseRoute import GoalBaseRoute


class GoalClient(AuthClient, GoalBaseRoute):
    """It manages all goals calls"""

    def add_new_goal_list(self, goal_name: Union[GoalName, str], terms: GoalList) -> None:
        """Add a new goal list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        with self.get_client() as client:
            response = client.send(self._build_add_new_goal_list_request(client, GoalName(goal_name), terms))
        self._handle_add_new_goal_list_response(response, GoalName(goal_name))

    def get_goal_list(self, goal_name: Union[GoalName, str]) -> GoalList:
        """TODO add doc"""
        with self.get_client() as client:
            response = client.send(self._build_get_goal_list_request(client, goal_name))
        return self._handle_get_goal_list_response(response, GoalName(goal_name))

    def get_goal_lists(self) -> List[Union[GoalName, str]]:
        """TODO add doc"""
        with self.get_client() as client:
            response = client.send(self._build_get_goal_lists_request(client))
        return self._handle_get_goal_lists_response(response)

    def get_sub_goal(self, goal_name: Union[GoalName, str], goal_index: int) -> Term:
        """Return the i-th sub-goal of goal_name"""
        with self.get_client() as client:
            response = client.send(self._build_get_sub_goal_request(client, GoalName(goal_name), goal_index))
        return self._handle_get_sub_goal_response(response, GoalName(goal_name))

    def remove_goal_list(self, goal_name: Union[GoalName, str]) -> None:
        """Remove goal_name goal list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        with self.get_client() as client:
            response = client.send(self._build_remove_goal_list_request(client, goal_name))
        self._handle_remove_goal_list_response(response, GoalName(goal_name))

    def replace_goal_list(self, goal_name: Union[GoalName, str], new_goal_list: GoalList) -> None:
        """Replace the goal with name goal_name with new_goal_list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        with self.get_client() as client:
            response = client.send(self._build_replace_goal_list_request(client, GoalName(goal_name), new_goal_list))
        self._handle_replace_goal_list_response(response, GoalName(goal_name))

    def add_sub_goal(self, goal_name: Union[GoalName, str], sub_goal: Term) -> None:
        """Add a sub goal to the end of `goal_name` goal."""
        with self.get_client() as client:
            response = client.send(self._build_add_sub_goal_request(client, GoalName(goal_name), sub_goal))
        self._handle_add_sub_goal_response(response, GoalName(goal_name))
