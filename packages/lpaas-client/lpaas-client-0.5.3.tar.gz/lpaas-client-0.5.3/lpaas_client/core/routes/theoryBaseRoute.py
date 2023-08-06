from abc import ABC
from typing import Union, List

from http_constants.headers import HttpHeaders
from http_constants.status import HttpStatus
from httpx import Client, AsyncClient, Request, Response
from tuprolog.core import Clause, Term
from tuprolog.core.parsing import parse_term
from tuprolog.theory import Theory
from tuprolog.theory.parsing import parse_theory

from lpaas_client.core.exception.exception import TheoryNotFoundException, TheoryAlreadyExistsException
from lpaas_client.core.model.theory import TheoryName, TheoryFullName, _get_theory_name, parse_theory_fact_update, \
    parse_get_theories_body, TheoryData
from lpaas_client.core.routes.authBaseRoute import AuthBaseRoute
from lpaas_client.serializer import serialize_term, serialize_theory


class TheoryBaseRoute(AuthBaseRoute, ABC):
    """Declare all the useful method to contact LPaaS /theories route.

    Give method to build request and handle response for:

    - add new theory
    - add new fact to theory
    - add new theory version
    - get all the theories
    - get a specific theory
    - get a specific theory version
    - get a fact from a theory
    - get a fact version from a theory
    - remove a theory
    - update a fact in a theory

    It make use of `AuthBaseRoute` for the authentication.
    """

    def __get_theories_url(self, *path: str):
        return self.get_url('theories', *path)

    # region add_new_fact_to_theory methods
    def _build_add_new_fact_to_theory_request(self,
                                              client: Union[Client, AsyncClient],
                                              theory_name: Union[TheoryName, TheoryFullName, str],
                                              fact: Clause,
                                              on_top: Union[bool, None] = None) -> Request:
        theory_name = _get_theory_name(theory_name)

        params = {}
        if on_top is not None:
            params['beginning'] = 'true' if on_top else 'false'

        return client.build_request('POST', self.__get_theories_url(theory_name, 'facts'),
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                    }),
                                    params=params,
                                    content=serialize_term(fact))

    def _handle_add_new_fact_to_theory_response(self, response: Response, theory_name: str) -> TheoryFullName:
        self._check_auth_response(response=response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise TheoryNotFoundException(theory_name)
        elif response.status_code == HttpStatus.BAD_REQUEST:
            raise ValueError('Invalid fact')
        self._check_response(response)
        return parse_theory_fact_update(response.text.strip())

    # endregion

    # region add_new_theory methods
    def _build_add_new_theory_request(self,
                                      client: Union[Client, AsyncClient],
                                      theory_name: TheoryName,
                                      theory: Theory) -> Request:
        return client.build_request('POST',
                                    self.__get_theories_url(),
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                    }),
                                    params={'name': theory_name},
                                    content=serialize_theory(theory))

    def _handle_add_new_theory_response(self, response: Response, theory_name: str) -> TheoryFullName:
        self._check_auth_response(response=response)
        if response.status_code == HttpStatus.CONFLICT:
            raise TheoryAlreadyExistsException(theory_name)
        self._check_response(response)
        return TheoryFullName(response.text.rstrip())

    # endregion

    # region add_new_theory_version methods
    def _build_add_new_theory_version_request(self,
                                              client: Union[Client, AsyncClient],
                                              theory_name: Union[TheoryName, TheoryFullName, str],
                                              new_theory: Theory) -> Request:
        return client.build_request('POST',
                                    self.__get_theories_url(_get_theory_name(theory_name)),
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                    }),
                                    content=serialize_theory(new_theory))

    def _handle_add_new_theory_version_response(self, response: Response) -> TheoryFullName:
        self._check_auth_response(response=response)
        self._check_response(response)
        return TheoryFullName(response.text)

    # endregion

    # region get_theories methods
    def _build_get_theories_request(self, client: Union[Client, AsyncClient]) -> Request:
        return client.build_request('GET',
                                    self.__get_theories_url(),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt})

    def _handle_get_theories_response(self, response: Response) -> List[TheoryFullName]:
        self._check_auth_response(response=response)
        self._check_response(response)
        return parse_get_theories_body(response.text)

    def _handle_get_theory_response_to_last_theory_version(self,
                                                           response: Response,
                                                           theory_name: Union[TheoryName, TheoryFullName]
                                                           ) -> TheoryFullName:
        self._check_auth_response(response=response)
        self._check_response(response)
        theory_name = _get_theory_name(theory_name)
        theory_full_name, = list(
                filter(lambda x: x.name == theory_name, parse_get_theories_body(response.text)))
        return theory_full_name

    # endregion

    # region get_theory methods
    def _build_get_theory_request(self, client: Union[Client, AsyncClient],
                                  theory_name: Union[TheoryName, TheoryFullName]) -> Request:
        if isinstance(theory_name, TheoryFullName):
            return self._build_get_theory_version_request(client, theory_name.name, theory_name.version)
        return client.build_request('GET', self.__get_theories_url(_get_theory_name(theory_name)),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt})

    def _build_get_theory_version_request(self, client: Union[Client, AsyncClient],
                                          theory_name: TheoryName,
                                          version: int) -> Request:
        return client.build_request('GET', self.__get_theories_url(theory_name, 'history', str(version)),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt})

    def _handle_get_theory_response(self, response: Response, theory_full_name: TheoryFullName) -> TheoryData:
        if response.status_code == HttpStatus.NOT_FOUND:
            raise TheoryNotFoundException(str(theory_full_name))
        self._check_response(response)
        return TheoryData(theory_full_name, parse_theory(response.text))

    # endregion

    # region get_theory_facts
    def _build_get_theory_facts_request(self,
                                        client: Union[Client, AsyncClient],
                                        theory_name: Union[TheoryName, TheoryFullName, str],
                                        functor_name: str,
                                        arity: Union[int, None] = None,
                                        limit: Union[int, None] = None) -> Request:
        if isinstance(theory_name, TheoryFullName):
            return self._build_get_theory_facts_version_request(client, theory_name, functor_name, arity, limit)
        params = {}
        if arity is not None:
            params['arity'] = arity
        if limit is not None:
            params['limit'] = limit
        return client.build_request('GET',
                                    self.__get_theories_url(theory_name, 'facts', functor_name),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt},
                                    params=params
                                    )

    def _build_get_theory_facts_version_request(self,
                                                client: Union[Client, AsyncClient],
                                                theory_name: TheoryFullName,
                                                functor_name: str,
                                                arity: Union[int, None] = None,
                                                limit: Union[int, None] = None) -> Request:
        params = {}
        if arity is not None:
            params['arity'] = arity
        if limit is not None:
            params['limit'] = limit
        return client.build_request('GET',
                                    self.__get_theories_url(theory_name.name, 'facts', functor_name, 'history',
                                                            str(theory_name.version)),
                                    headers={HttpHeaders.ACCEPT: HttpHeaders.CONTENT_TYPE_VALUES.txt},
                                    params=params
                                    )

    def _handle_get_theory_facts_response(self, response: Response, theory_name: str) -> List[Term]:
        if response.status_code == HttpStatus.NOT_FOUND:
            raise TheoryNotFoundException(theory_name)
        self._check_response(response)
        return [parse_term(line) for line in response.text.split('\n') if len(line) > 0]

    # endregion

    # region remove_theory methods
    def _build_remove_theory_request(self,
                                     client: Union[Client, AsyncClient],
                                     theory_name: Union[TheoryName, TheoryFullName, str]) -> Request:
        return client.build_request('DELETE',
                                    self.__get_theories_url(_get_theory_name(theory_name)),
                                    headers=self._add_jwt_token()
                                    )

    def _handle_remove_theory_response(self, response: Response, theory_name: str) -> None:
        self._check_auth_response(response=response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise TheoryNotFoundException(theory_name)
        self._check_response(response)

    # endregion

    # region update_fact_in_theory
    def _build_update_fact_in_theory_request(self,
                                             client: Union[Client, AsyncClient],
                                             theory_name: Union[TheoryName, TheoryFullName, str],
                                             functor: str,
                                             fact: Term,
                                             on_top: Union[bool, None] = None) -> Request:

        params = {}
        if on_top is not None:
            params['beginning'] = 'true' if on_top else 'false'

        return client.build_request('PUT',
                                    self.__get_theories_url(_get_theory_name(theory_name), 'facts', functor),
                                    headers=self._add_jwt_token({
                                        HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                        HttpHeaders.ACCEPT      : HttpHeaders.CONTENT_TYPE_VALUES.txt,
                                    }),
                                    content=serialize_term(fact),
                                    params=params)

    def _handle_update_fact_in_theory_response(self, response: Response, theory_name: str) -> TheoryFullName:
        self._check_auth_response(response)
        if response.status_code == HttpStatus.NOT_FOUND:
            raise TheoryNotFoundException(theory_name)
        if response.status_code == HttpStatus.BAD_REQUEST:
            raise ValueError('Invalid update')
        self._check_response(response)
        return parse_theory_fact_update(response.text.strip())
    # endregion
