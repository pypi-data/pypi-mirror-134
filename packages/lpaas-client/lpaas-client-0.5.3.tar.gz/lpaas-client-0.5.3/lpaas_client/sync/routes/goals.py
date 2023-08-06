from typing import List, Union

from tuprolog.core import Term

from lpaas_client.sync.routes.auth import AuthClient, repeat_on_unauthorized
from lpaas_client.core.model.goal import GoalName, GoalList
from lpaas_client.core.routes.goalBaseRoute import GoalBaseRoute


class GoalClient(AuthClient, GoalBaseRoute):
    """It manages all goals calls"""

    @repeat_on_unauthorized
    def add_new_goal_list(self, goal_name: Union[GoalName, str], terms: GoalList) -> None:
        """Creates a new composed-goal having the provided goal_name

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        :param terms: the goal list
        """
        with self._get_client() as client:
            response = client.send(self._build_add_new_goal_list_request(client, GoalName(goal_name), terms))
        self._handle_add_new_goal_list_response(response, GoalName(goal_name))

    def get_goal_list(self, goal_name: Union[GoalName, str]) -> GoalList:
        """Retrieves the goal list with name goal_name

        :param goal_name: the goal name
        :return: a goal list
        """
        with self._get_client() as client:
            response = client.send(self._build_get_goal_list_request(client, goal_name))
        return self._handle_get_goal_list_response(response, GoalName(goal_name))

    def get_goal_lists(self) -> List[Union[GoalName, str]]:
        """Retrieves the list of composed-goal currently existing on the server side"""
        with self._get_client() as client:
            response = client.send(self._build_get_goal_lists_request(client))
        return self._handle_get_goal_lists_response(response)

    def get_sub_goal(self, goal_name: Union[GoalName, str], goal_index: int) -> Term:
        """Retrieves the sub-goal having the selected index

        :param goal_name: the goal name
        :param goal_index: the index of the sub goal
        :return: the i-th term of goal_name
        """
        with self._get_client() as client:
            response = client.send(self._build_get_sub_goal_request(client, GoalName(goal_name), goal_index))
        return self._handle_get_sub_goal_response(response, GoalName(goal_name))

    @repeat_on_unauthorized
    def remove_goal_list(self, goal_name: Union[GoalName, str]) -> None:
        """Deletes the selected composed-goal and all its sub-goals

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        """
        with self._get_client() as client:
            response = client.send(self._build_remove_goal_list_request(client, goal_name))
        self._handle_remove_goal_list_response(response, GoalName(goal_name))

    @repeat_on_unauthorized
    def replace_goal_list(self, goal_name: Union[GoalName, str], new_goal_list: GoalList) -> None:
        """Replaces the selected composed-goal with the provided one

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name to be replaced
        :param new_goal_list: the new goal list
        """
        with self._get_client() as client:
            response = client.send(self._build_replace_goal_list_request(client, GoalName(goal_name), new_goal_list))
        self._handle_replace_goal_list_response(response, GoalName(goal_name))

    @repeat_on_unauthorized
    def add_sub_goal(self, goal_name: Union[GoalName, str], sub_goal: Term) -> None:
        """Appends a sub-goal to the selected composed-goal

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        :param sub_goal: the sub goal to be added
        """
        with self._get_client() as client:
            response = client.send(self._build_add_sub_goal_request(client, GoalName(goal_name), sub_goal))
        self._handle_add_sub_goal_response(response, GoalName(goal_name))
