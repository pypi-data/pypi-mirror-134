from abc import ABC
from typing import Union, List

from http_constants.headers import HttpHeaders
from http_constants.status import HttpStatus
from httpx import Client, AsyncClient, Request, Response
from tuprolog.core import Term
from tuprolog.core.parsing import parse_term

from lpaas_client.core.exception.exception import GoalAlreadyExistsException, GoalNotFoundException
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute
from lpaas_client.core.model.goal import GoalName, GoalList, parse_goal_body, parse_goal_lists_body, get_serialized_goals
from lpaas_client.serializer import serialize_term
from lpaas_client.serializer.serializer import serialize_term_list


class GoalBaseRoute(AuthBaseRoute, ABC):
    """Declare all the useful method to contact LPaaS /goals route.

    Give method to build request and handle response for:

    - add new goal list
    - get a goal list
    - get all the goal lists
    - get a sub goal of a gaol list
    - remove a goal list
    - remove all the goal list
    - remove a sub goal in a goal list
    - replace a goal list

    It make use of `AuthBaseRoute` for the authentication.
    """

    def __goal_route(self, *path: str) -> str:
        return self.get_url('goals', *path)

    # region add_new_goal methods
    def _build_add_new_goal_list_request(self,
                                         client: Union[Client, AsyncClient],
                                         goal_name: GoalName,
                                         terms: GoalList) -> Request:
        return client.build_request('POST',
                                    self.__goal_route(),
                                    params={
                                        'name': goal_name
                                    },
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt
                                    }),
                                    content=', '.join(serialize_term_list(terms)))

    def _handle_add_new_goal_list_response(self, response: Response, goal_name: GoalName) -> None:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.CONFLICT:
            raise GoalAlreadyExistsException(f'Goal {goal_name} is already present')
        elif response.status_code == HttpStatus.BAD_REQUEST:
            raise ValueError('Invalid goal list')  # this should never be raised
        self._check_response(response)

    # endregion

    # region get_goal_list methods
    def _build_get_goal_list_request(self, client: Client, goal_name: GoalName) -> Request:
        return client.build_request('GET',
                                    self.__goal_route(goal_name),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt})

    def _handle_get_goal_list_response(self, response: Response, goal_name: GoalName) -> Term:
        if response.status_code == HttpStatus.NOT_FOUND:
            raise GoalNotFoundException(goal_name)
        self._check_response(response)
        return parse_goal_body(response.text)

    # endregion

    # region get_goal_lists methods
    def _build_get_goal_lists_request(self, client: Client) -> Request:
        return client.build_request('GET',
                                    self.__goal_route(),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt})

    def _handle_get_goal_lists_response(self, response: Response) -> List[GoalName]:
        self._check_response(response)
        return parse_goal_lists_body(response.text)

    # endregion

    # region get_sub_goal methods
    def _build_get_sub_goal_request(self, client: Union[Client, AsyncClient], goal_name: GoalName,
                                    goal_index: int) -> Request:
        """Return the i-th sub-goal of goal_name"""
        assert goal_index >= 0, "index should be greater than zero"

        return client.build_request('GET',
                                    self.__goal_route(goal_name, str(goal_index)),
                                    headers={
                                        HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt
                                    })

    def _handle_get_sub_goal_response(self, response: Response, goal_name: GoalName) -> List[Term]:
        if response.status_code == HttpStatus.NOT_FOUND:
            raise GoalNotFoundException(goal_name)
        self._check_response(response)
        return parse_term(response.text)

    # endregion

    # region remove_goal_list methods
    def _build_remove_goal_list_request(self, client: Union[Client, AsyncClient], goal_name: GoalName) -> Request:
        """Remove goal_name goal list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        return client.build_request('DELETE',
                                    self.__goal_route(goal_name),
                                    headers=self._add_jwt_token())

    def _handle_remove_goal_list_response(self, response: Response, goal_name: GoalName) -> None:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise GoalNotFoundException(goal_name)
        self._check_response(response)

    # endregion

    # region replace_goal_list methods
    def _build_replace_goal_list_request(self,
                                         client: Union[Client, AsyncClient],
                                         goal_name: GoalName,
                                         new_goal_list: GoalList) -> Request:
        """Replace the goal with name goal_name with new_goal_list

        You need to be authenticated as a CONFIGURATOR or an higher role.
        """
        return client.build_request('PUT', self.__goal_route(goal_name),
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                    }),
                                    content=get_serialized_goals(new_goal_list)
                                    )

    def _handle_replace_goal_list_response(self, response: Response, goal_name: GoalName) -> None:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise GoalNotFoundException(goal_name)
        elif response.status_code == HttpStatus.BAD_REQUEST:
            raise ValueError('Invalid goal list')
        self._check_response(response)

    # endregion

    # region add_sub_goal methods
    def _build_add_sub_goal_request(self, client: Union[Client, AsyncClient], goal_name: GoalName,
                                    sub_goal: Term) -> Request:
        """Add a sub goal to the end of `goal_name` goal."""
        return client.build_request('POST', self.__goal_route(goal_name),
                                    headers=self._add_jwt_token(),
                                    content=serialize_term(sub_goal))

    def _handle_add_sub_goal_response(self, response: Response, goal_name: GoalName) -> None:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise GoalNotFoundException(goal_name)
        self._check_response(response)
    # endregion