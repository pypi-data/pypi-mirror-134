import asyncio
from typing import Union, List

from tuprolog.core import Clause, Term
from tuprolog.theory import Theory

from lpaas_client.asyn.routes.auth import AuthClient
from lpaas_client.core.model.theory import TheoryData, TheoryFullName, TheoryName, build_theory_full_name
from lpaas_client.core.routes.theoryBaseRoute import TheoryBaseRoute


class TheoriesClient(AuthClient, TheoryBaseRoute):

    async def add_new_fact_to_theory(self,
                               theory_name: Union[TheoryName, TheoryFullName, str],
                               fact: Clause,
                               on_top: Union[bool, None] = None) -> TheoryFullName:
        """Add fact to Theory with name theory_name

        This method require an authentication with SENSOR role or superior.
        """

        async with self.get_client() as client:
            response = await client.send(self._build_add_new_fact_to_theory_request(client, theory_name, fact, on_top))

        return self._handle_add_new_fact_to_theory_response(response, theory_name)

    async def add_new_theory(self, theory_name: TheoryName, theory: Theory) -> TheoryFullName:
        """Add a new theory
        if the theory already exists this method will updated its version.

        This method require an authentication with CONFIGURATOR role or superior.
        """
        async with self.get_client() as client:
            response = await client.send(self._build_add_new_theory_request(client, theory_name, theory))
        return self._handle_add_new_theory_response(response, theory_name)

    async def add_new_theory_version(self,
                               theory_name: Union[TheoryName, TheoryFullName],
                               new_theory: Theory) -> TheoryFullName:
        """Add a new theory
        if the theory already exists this method will updated its version.

        This method require an authentication with CONFIGURATOR role or superior.
        """
        async with self.get_client() as client:
            response = await client.send(self._build_add_new_theory_version_request(client, theory_name, new_theory))
        return self._handle_add_new_theory_version_response(response)

    async def get_theories(self) -> List[TheoryFullName]:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_get_theories_request(client))
        return self._handle_get_theories_response(response)

    async def get_theory(self, theory_name: Union[TheoryName, TheoryFullName]) -> TheoryData:
        """TODO add doc"""
        async with self.get_client() as client:
            response = client.send(self._build_get_theory_request(client, theory_name))
            theories_response = client.send(self._build_get_theories_request(client))
            response, theories_response = await asyncio.gather(response, theories_response)
        theory_full_name = self._handle_get_theory_response_to_last_theory_version(theories_response, theory_name)
        return self._handle_get_theory_response(response, theory_full_name)

    async def get_theory_version(self, theory_name: TheoryName, version: int) -> TheoryData:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_get_theory_version_request(client, theory_name, version))
        return self._handle_get_theory_response(response, build_theory_full_name(theory_name, version))

    async def get_theory_facts(self,
                         theory_name: Union[TheoryName, TheoryFullName],
                         functor_name: str,
                         arity: Union[int, None] = None,
                         limit: Union[int, None] = None) -> List[Term]:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(
                self._build_get_theory_facts_request(client, theory_name, functor_name, arity, limit))
        return self._handle_get_theory_facts_response(response, theory_name)

    async def get_theory_facts_version(self, theory_name: TheoryFullName,
                                 functor_name: str,
                                 arity: Union[int, None] = None,
                                 limit: Union[int, None] = None) -> List[Term]:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(
                self._build_get_theory_facts_version_request(client, theory_name, functor_name, arity, limit))
        return self._handle_get_theory_facts_response(response, str(theory_name.name))

    async def remove_theory(self, theory_name: Union[TheoryName, TheoryFullName]) -> None:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_remove_theory_request(client, theory_name))
        self._handle_remove_theory_response(response, theory_name)

    async def update_fact_in_theory(self,
                              theory_name: Union[TheoryName, TheoryFullName],
                              functor: str,
                              fact: Term,
                              on_top: Union[bool, None] = None) -> TheoryFullName:
        """TODO add doc"""
        async with self.get_client() as client:
            response = await client.send(self._build_update_fact_in_theory_request(client, theory_name, functor, fact, on_top))
        return self._handle_update_fact_in_theory_response(response, theory_name)
