import datetime
from abc import ABC
from typing import Union, List

import isodate
from http_constants.headers import HttpHeaders
from http_constants.status import HttpStatus
from httpx import Client, AsyncClient, Request, Response

from lpaas_client.core.exception.exception import SolutionAlreadyExistsException, NotFoundException, \
    SolutionNotFoundException
from lpaas_client.core.model.goal import GoalName
from lpaas_client.core.model.solution import Hook, Solution, build_solution_from_json
from lpaas_client.core.model.theory import TheoryName
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute


class SolutionsBaseRoute(AuthBaseRoute, ABC):
    """Declare all the useful method to contact LPaaS /solutions route.

    Give method to build request and handle response for:

    - add a new solution
    - get solution by hook
    - get solution specific version by hook
    - get all the available solution
    - remove all solutions
    - remove a specific solution

    It make use of `AuthBaseRoute` for the authentication.
    """

    def __solutions_route(self, *path: str) -> str:
        return self.get_url('solutions', *path)

    # region add methods

    def _build_add_new_solution_request(self,
                                        client: Union[Client, AsyncClient],
                                        theory_name: TheoryName,
                                        goal_name: GoalName,
                                        hook: Union[Hook, None] = None,
                                        skip: Union[int, None] = None,
                                        limit: Union[int, None] = None,
                                        within: Union[datetime.timedelta, None] = None,
                                        every: Union[datetime.timedelta, None] = None,
                                        ) -> Request:
        params_values = [('hook', hook),
                         ('skip', skip),
                         ('limit', limit)]
        params = {v: k for v, k in params_values if k is not None}

        if within is not None:
            params['within'] = isodate.duration_isoformat(within)
        if every is not None:
            params['every'] = isodate.duration_isoformat(every)

        return client.build_request('POST',
                                    self.__solutions_route(),
                                    headers={
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.json
                                    },
                                    params=params,
                                    json={
                                        'goals' : goal_name.to_url,
                                        'theory': theory_name.to_url
                                    })

    def _handle_add_new_solution_response(self,
                                          response: Response,
                                          theory_name: TheoryName,
                                          goal_name: GoalName,
                                          ) -> Solution:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.CONFLICT:
            raise SolutionAlreadyExistsException()
        elif response.status_code == HttpStatus.BAD_REQUEST:
            raise ValueError('Invalid solution format')
        elif response.status_code == HttpStatus.NOT_FOUND:
            raise NotFoundException(f'Goal {goal_name} and/or theory {theory_name}')
        elif response.status_code == HttpStatus.INTERNAL_SERVER_ERROR:
            raise ValueError('Invalid theory')
        self._check_response(response)
        return build_solution_from_json(response.json())

    # endregion

    # region get methods
    def _build_get_hook_request(self,
                                client: Union[Client, AsyncClient],
                                hook: Hook,
                                version: Union[int, None] = None) -> Request:
        if version is not None:
            url = self.__solutions_route(hook, 'history', str(version))
        else:
            url = self.__solutions_route(hook)
        return client.build_request('GET',
                                    url,
                                    headers={
                                        HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.json
                                    })

    def _build_get_hooks_request(self, client: Union[Client, AsyncClient]) -> Request:
        return client.build_request('GET',
                                    self.__solutions_route(),
                                    headers={
                                        HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.json
                                    })

    def _handle_get_hook_response(self, response: Response, hook: Union[Hook, None] = None) -> Solution:
        if response.status_code == HttpStatus.NOT_FOUND:
            raise SolutionNotFoundException(hook)
        self._check_response(response)
        return build_solution_from_json(response.json())

    def _handle_get_hooks_response(self, response: Response) -> List[Solution]:
        self._check_response(response)
        return [build_solution_from_json(s) for s in response.json()]

    # endregion

    # region remove methods
    def _build_remove_all_request(self, client: Client) -> Request:
        return client.build_request('DELETE', self.__solutions_route())

    def _build_remove_hook_request(self,
                                   client: Client,
                                   hook: Hook,
                                   version: Union[int, None] = None) -> Request:
        if version is not None:
            url = self.__solutions_route(hook, 'history', str(version))
        else:
            url = self.__solutions_route(hook)
        return client.build_request('DELETE', url)

    def _handle_remove_all_response(self, response: Response) -> None:
        self._check_auth_response(response)
        self._check_response(response)

    def _handle_remove_hook_response(self, response: Response, hook: Hook) -> None:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise SolutionNotFoundException()
        self._check_response(response)
    # endregion