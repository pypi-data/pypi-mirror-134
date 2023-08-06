from typing import List

from tuprolog.core import Term

from lpaas_client.asyn.routes.auth import AuthClient
from lpaas_client.core.model.goal import GoalName, GoalList
from lpaas_client.core.routes.goalBaseRoute import GoalBaseRoute


class GoalClient(AuthClient, GoalBaseRoute):
    """It manages all goals calls"""

    async def add_new_goal_list(self, goal_name: GoalName, terms: GoalList) -> None:
        """Add a new goal list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        async with self.get_client() as client:
            response = await client.send(self._build_add_new_goal_list_request(client, goal_name, terms))
        self._handle_add_new_goal_list_response(response, goal_name)

    async def get_goal_list(self, goal_name: GoalName) -> GoalList:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_get_goal_list_request(client, goal_name))
        return self._handle_get_goal_list_response(response, goal_name)

    async def get_goal_lists(self) -> List[GoalName]:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_get_goal_lists_request(client))
        return self._handle_get_goal_lists_response(response)

    async def get_sub_goal(self, goal_name: GoalName, goal_index: int) -> Term:
        """Return the i-th sub-goal of goal_name"""
        async with self.get_client() as client:
            response = await client.send(self._build_get_sub_goal_request(client, goal_name, goal_index))
        return self._handle_get_sub_goal_response(response, goal_name)

    async def remove_goal_list(self, goal_name: GoalName) -> None:
        """Remove goal_name goal list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        async with self.get_client() as client:
            response = await client.send(self._build_remove_goal_list_request(client, goal_name))
        self._handle_remove_goal_list_response(response, goal_name)

    async def replace_goal_list(self, goal_name: GoalName, new_goal_list: GoalList) -> None:
        """Replace the goal with name goal_name with new_goal_list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        async with self.get_client() as client:
            response = await client.send(self._build_replace_goal_list_request(client, goal_name, new_goal_list))
        self._handle_replace_goal_list_response(response, goal_name)

    async def add_sub_goal(self, goal_name: GoalName, sub_goal: Term) -> None:
        """Add a sub goal to the end of `goal_name` goal."""
        async with self.get_client() as client:
            response = await client.send(self._build_add_sub_goal_request(client, goal_name, sub_goal))
        self._handle_add_sub_goal_response(response, goal_name)
