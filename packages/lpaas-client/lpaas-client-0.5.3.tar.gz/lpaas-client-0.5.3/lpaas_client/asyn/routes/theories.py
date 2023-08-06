import asyncio
from typing import Union, List

from tuprolog.core import Clause, Term
from tuprolog.theory import Theory

from lpaas_client.asyn.routes.auth import AuthClient, repeat_on_unauthorized_async
from lpaas_client.core.model.theory import TheoryData, TheoryFullName, TheoryName, build_theory_full_name
from lpaas_client.core.routes.theoryBaseRoute import TheoryBaseRoute


class TheoriesClient(AuthClient, TheoryBaseRoute):

    @repeat_on_unauthorized_async
    async def add_new_fact_to_theory(self,
                                     theory_name: Union[TheoryName, TheoryFullName, str],
                                     fact: Clause,
                                     on_top: Union[bool, None] = None) -> TheoryFullName:
        """Asserts a new fact on the theory referenced by theory_name,
        thus creating a new version of such a theory where a fact has been added

        You need to be authenticated as a SENSOR or an higher role.

        :param theory_name: the theory name
        :param fact: the new fact
        :param on_top: if or not this fact should be placed on top
        :return: the theory full name with the new version number
        """

        async with self._get_client() as client:
            response = await client.send(self._build_add_new_fact_to_theory_request(client, theory_name, fact, on_top))

        return self._handle_add_new_fact_to_theory_response(response, theory_name)

    @repeat_on_unauthorized_async
    async def add_new_theory(self, theory_name: TheoryName, theory: Theory) -> TheoryFullName:
        """Creates a new theory identified by the provided theory_name
        if the theory already exists this method will raise an exception.

        This method require an authentication with CONFIGURATOR role or superior.

        :param theory_name: the theory name
        :param theory: the theory
        :return: the theory full name with the new version number
        """
        async with self._get_client() as client:
            response = await client.send(self._build_add_new_theory_request(client, theory_name, theory))
        return self._handle_add_new_theory_response(response, theory_name)

    @repeat_on_unauthorized_async
    async def add_new_theory_version(self,
                                     theory_name: Union[TheoryName, TheoryFullName],
                                     new_theory: Theory) -> TheoryFullName:
        """Creates a new version of the theory referenced by theory_name.
        The theory have to exists or this method will raise an exception.

        This method require an authentication with CONFIGURATOR role or superior.

        :param theory_name: the theory name
        :param new_theory: the new theory version
        :return: the theory full name with the new version number
        """
        async with self._get_client() as client:
            response = await client.send(self._build_add_new_theory_version_request(client, theory_name, new_theory))
        return self._handle_add_new_theory_version_response(response)

    async def get_theories(self) -> List[TheoryFullName]:
        """Retrieves the list of theories currently existing on the server side

        :return: a list of theory name
        """
        async with self._get_client() as client:
            response = await client.send(self._build_get_theories_request(client))
        return self._handle_get_theories_response(response)

    async def get_theory(self, theory_name: Union[TheoryName, TheoryFullName]) -> TheoryData:
        """Retrieves the last version of the theory referenced by theory_name
        The theory have to exists or this method will raise an exception.

        :param theory_name: the theory name
        :return: A TheoryData containing the theory information
        """
        async with self._get_client() as client:
            response = client.send(self._build_get_theory_request(client, theory_name))
            theories_response = client.send(self._build_get_theories_request(client))
            response, theories_response = await asyncio.gather(response, theories_response)
        theory_full_name = self._handle_get_theory_response_to_last_theory_version(theories_response, theory_name)
        return self._handle_get_theory_response(response, theory_full_name)

    async def get_theory_version(self, theory_name: TheoryName, version: int) -> TheoryData:
        """Retrieves the selected version of the selected theory.
        The theory have to exists or this method will raise an exception.

        :param theory_name: the theory name
        :param version: the version of the theory
        :return: A TheoryData containing the theory information
        """
        async with self._get_client() as client:
            response = await client.send(self._build_get_theory_version_request(client, theory_name, version))
        return self._handle_get_theory_response(response, build_theory_full_name(theory_name, version))

    async def get_theory_facts(self,
                               theory_name: Union[TheoryName, TheoryFullName],
                               functor_name: str,
                               arity: Union[int, None] = None,
                               limit: Union[int, None] = None) -> List[Term]:
        """Retrieves the last version of the fact referenced by functor within the theory referenced by name
        The theory have to exists or this method will raise an exception.
        The fact have to exists or this method will raise an exception.

        :param theory_name: the theory name
        :param functor_name: the functor
        :param arity: arity of the functor
        :param limit: limit of elements to retrieve
        :return: a list of ordered Term
        """
        async with self._get_client() as client:
            response = await client.send(
                    self._build_get_theory_facts_request(client, theory_name, functor_name, arity, limit))
        return self._handle_get_theory_facts_response(response, theory_name)

    async def get_theory_facts_version(self, theory_name: TheoryFullName,
                                       functor_name: str,
                                       arity: Union[int, None] = None,
                                       limit: Union[int, None] = None) -> List[Term]:
        """Retrieves the specified version of the fact referenced by functor within the theory referenced by name
        The theory have to exists or this method will raise an exception.
        The fact have to exists or this method will raise an exception.

        :param theory_name: the theory full name with the desired version
        :param functor_name: the functor
        :param arity: arity of the functor
        :param limit: limit of elements to retrieve
        :return: a list of ordered Term
        """
        async with self._get_client() as client:
            response = await client.send(
                    self._build_get_theory_facts_version_request(client, theory_name, functor_name, arity, limit))
        return self._handle_get_theory_facts_response(response, str(theory_name.name))

    @repeat_on_unauthorized_async
    async def remove_theory(self, theory_name: Union[TheoryName, TheoryFullName]) -> None:
        """Deletes the selected theory with all its versions
        The theory have to exists or this method will raise an exception.

        You need to be authenticated as a CONFIGURATOR or an higher role.

        :param theory_name: the theory name
        """
        async with self._get_client() as client:
            response = await client.send(self._build_remove_theory_request(client, theory_name))
        self._handle_remove_theory_response(response, theory_name)

    @repeat_on_unauthorized_async
    async def update_fact_in_theory(self,
                                    theory_name: Union[TheoryName, TheoryFullName],
                                    functor: str,
                                    fact: Term,
                                    on_top: Union[bool, None] = None) -> TheoryFullName:
        """Asserts a new fact on the theory referenced by name after retracting its predecessor,
        thus creating a new version of such a theory where a fact has been replaced
        The theory have to exists or this method will raise an exception.

        You need to be authenticated as a SENSOR or an higher role.

        :param theory_name: the theory name
        :param functor: the functor
        :param fact: the fact
        :param on_top: if or not the new fact have to be placed on top
        :return: the new theory version as a TheoryFullName
        """
        async with self._get_client() as client:
            response = await client.send(
                    self._build_update_fact_in_theory_request(client, theory_name, functor, fact, on_top))
        return self._handle_update_fact_in_theory_response(response, theory_name)
