from typing import List

from tuprolog.core import Term

from lpaas_client.asyn.routes.auth import AuthClient, repeat_on_unauthorized_async
from lpaas_client.core.model.goal import GoalName, GoalList
from lpaas_client.core.routes.goalBaseRoute import GoalBaseRoute


class GoalClient(AuthClient, GoalBaseRoute):
    """It manages all goals calls"""

    @repeat_on_unauthorized_async
    async def add_new_goal_list(self, goal_name: GoalName, terms: GoalList) -> None:
        """Creates a new composed-goal having the provided goal_name

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        :param terms: the goal list
        """
        async with self._get_client() as client:
            response = await client.send(self._build_add_new_goal_list_request(client, goal_name, terms))
        self._handle_add_new_goal_list_response(response, goal_name)

    async def get_goal_list(self, goal_name: GoalName) -> GoalList:
        """Retrieves the goal list with name goal_name

        :param goal_name: the goal name
        :return: a goal list
        """
        async with self._get_client() as client:
            response = await client.send(self._build_get_goal_list_request(client, goal_name))
        return self._handle_get_goal_list_response(response, goal_name)

    async def get_goal_lists(self) -> List[GoalName]:
        """Retrieves the list of composed-goal currently existing on the server side"""
        async with self._get_client() as client:
            response = await client.send(self._build_get_goal_lists_request(client))
        return self._handle_get_goal_lists_response(response)

    async def get_sub_goal(self, goal_name: GoalName, goal_index: int) -> Term:
        """Retrieves the sub-goal having the selected index

        :param goal_name: the goal name
        :param goal_index: the index of the sub goal
        :return: the i-th term of goal_name
        """
        async with self._get_client() as client:
            response = await client.send(self._build_get_sub_goal_request(client, goal_name, goal_index))
        return self._handle_get_sub_goal_response(response, goal_name)

    @repeat_on_unauthorized_async
    async def remove_goal_list(self, goal_name: GoalName) -> None:
        """Deletes the selected composed-goal and all its sub-goals

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        """
        async with self._get_client() as client:
            response = await client.send(self._build_remove_goal_list_request(client, goal_name))
        self._handle_remove_goal_list_response(response, goal_name)

    @repeat_on_unauthorized_async
    async def replace_goal_list(self, goal_name: GoalName, new_goal_list: GoalList) -> None:
        """Replaces the selected composed-goal with the provided one

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name to be replaced
        :param new_goal_list: the new goal list
        """
        async with self._get_client() as client:
            response = await client.send(self._build_replace_goal_list_request(client, goal_name, new_goal_list))
        self._handle_replace_goal_list_response(response, goal_name)

    @repeat_on_unauthorized_async
    async def add_sub_goal(self, goal_name: GoalName, sub_goal: Term) -> None:
        """Appends a sub-goal to the selected composed-goal

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param goal_name: the goal name
        :param sub_goal: the sub goal to be added
        """
        async with self._get_client() as client:
            response = await client.send(self._build_add_sub_goal_request(client, goal_name, sub_goal))
        self._handle_add_sub_goal_response(response, goal_name)
