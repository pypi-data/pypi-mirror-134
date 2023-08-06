import asyncio

import asynctest

import respx
from httpx import URL, Response
from tuprolog.core.parsing import parse_term, parse_clause
from tuprolog.theory.parsing import parse_theory

from lpaas_client.core.model.auth import AuthData
from lpaas_client.core.model.theory import build_theory_full_name, TheoryName
from lpaas_client.serializer import serialize_term, serialize_theory
from lpaas_client.asyn.routes.theories import TheoriesClient

base_url = URL('http://localhost8080')
jwt_token = 'token!1'
theory_name = TheoryName('theory_name')
theory_version = 0
theory_str = 'a.\np(a).\np(a, b).\n'
theory = parse_theory(theory_str)
facts_p_str = ['p(a)', 'p(a, b)']
facts_p = [parse_term(t) for t in facts_p_str]
functor = 'p'


class TestTheoriesClient(asynctest.TestCase):

    @classmethod
    @respx.mock
    async def setUp(cls) -> None:
        cls.client = TheoriesClient(base_url=base_url)

        # authentication
        respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': jwt_token}))

        await cls.client.authenticate(AuthData('user', 'password'))

    @respx.mock
    async def test_add_new_fact_to_theory(self):
        request = respx.post(base_url.join(f'/lpaas/theories/{theory_name}/facts')).mock(
                return_value=Response(200, content=f'/theories/{theory_name}/facts/{functor}/history/{theory_version}')
        )

        response = await self.client.add_new_fact_to_theory(theory_name, parse_clause(facts_p_str[0]))

        self.assertTrue(request.called)
        self.assertEqual(response, build_theory_full_name(theory_name, theory_version))

    @respx.mock
    async def test_create_theory(self):
        request = respx.post(base_url.join('/lpaas/theories')).mock(
                return_value=Response(status_code=200, content=f'/theories/{theory_name}/history/{theory_version}')
        )

        response = await self.client.add_new_theory(theory_name, theory)

        self.assertTrue(request.called)
        self.assertEqual(response, build_theory_full_name(theory_name, theory_version))
        self.assertEqual(request.calls.last.request.headers['Authorization'], jwt_token)

    @respx.mock
    async def test_update_theory(self):
        theory_version_updated = 2
        request = respx.post(base_url.join(f'/lpaas/theories/{theory_name}')).mock(
                return_value=Response(status_code=200,
                                      content=f'/theories/{theory_name}/history/{theory_version_updated}')
        )

        response = await self.client.add_new_theory_version(
                build_theory_full_name(theory_name, theory_version_updated - 1), theory)

        self.assertTrue(request.called)
        self.assertEqual(build_theory_full_name(theory_name, theory_version_updated), response)
        self.assertEqual(request.calls.last.request.headers['Authorization'], jwt_token)

    @respx.mock
    async def test_get_theories(self):
        requests = respx.get(base_url.join(f'/lpaas/theories')).mock(
                return_value=Response(status_code=200,
                                      content=f'Available theories:\n/theories/{theory_name}/history/{theory_version}\n'
                                              f'/theories/{theory_name}_2/history/2')
        )

        response = await self.client.get_theories()

        self.assertTrue(requests.called)
        self.assertListEqual(response, [build_theory_full_name(theory_name, theory_version),
                                        build_theory_full_name(theory_name + '_2', 2)])

    @respx.mock
    async def test_get_theory(self):
        request_theory = respx.get(base_url.join(f'/lpaas/theories/{theory_name}')).mock(
                return_value=Response(status_code=200, content=serialize_theory(theory))
        )
        request_theories = respx.get(base_url.join(f'/lpaas/theories')).mock(
                return_value=Response(status_code=200,
                                      content=f'Available theories:\n'
                                              f'{build_theory_full_name(theory_name, theory_version).url_with_version}')
        )

        response = await self.client.get_theory(theory_name)

        self.assertTrue(request_theory.called)
        self.assertTrue(request_theories.called)
        self.assertEqual(serialize_theory(response.theory), serialize_theory(theory))
        self.assertEqual(response.full_name, build_theory_full_name(theory_name, theory_version))

    @respx.mock
    async def test_get_theory_facts(self):
        request_arity_limit = respx.get(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}'),
                                        params={'arity': 2, 'limit': 1}).mock(
                return_value=Response(status_code=200, content=f'{serialize_term(facts_p[1])}')
        )

        request_arity = respx.get(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}'),
                                  params={'arity': 2}).mock(
                return_value=Response(status_code=200, content=f'{serialize_term(facts_p[1])}')
        )

        request_limit = respx.get(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}'),
                                  params={'limit': 1}).mock(
                return_value=Response(status_code=200, content=f'{serialize_term(facts_p[0])}')
        )

        request = respx.get(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}')).mock(
                return_value=Response(status_code=200,
                                      content=f'{serialize_term(facts_p[0])}\n{serialize_term(facts_p[1])}')
        )

        async with self.client:
            # use the same client for both the request
            response_arity_limit = self.client.get_theory_facts(theory_name, functor, arity=2, limit=1)
            response_arity = self.client.get_theory_facts(theory_name, functor, arity=2)
            response_limit = self.client.get_theory_facts(theory_name, functor, limit=1)
            response = self.client.get_theory_facts(theory_name, functor)
            response_arity_limit, response_arity, response_limit, response = await asyncio.gather(
                    response_arity_limit, response_arity, response_limit, response)

        self.assertTrue(request_arity_limit.called)
        self.assertListEqual(response_arity_limit, facts_p[1:])
        self.assertTrue(request_arity.called)
        self.assertListEqual(response_arity, facts_p[1:])
        self.assertTrue(request_limit.called)
        self.assertListEqual(response_limit, facts_p[:1])
        self.assertTrue(request.called)
        self.assertListEqual(response, facts_p)

    @respx.mock
    async def test_remove_theory(self):
        requests = respx.delete(base_url.join(f'/lpaas/theories/{theory_name}')) % 204

        await self.client.remove_theory(theory_name)

        self.assertTrue(requests.called)
        self.assertEqual(requests.calls.last.request.headers['Authorization'], jwt_token)

    @respx.mock
    async def test_update_fact_in_theory(self):
        request_on_top_false = respx.put(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}'),
                                         params={'beginning': 'false'}).mock(
                return_value=Response(200, content=f'/theories/{theory_name}/facts/{functor}/history/{theory_version}')
        )

        request = respx.put(base_url.join(f'/lpaas/theories/{theory_name}/facts/{functor}')).mock(
                return_value=Response(200, content=f'/theories/{theory_name}/facts/{functor}/history/{theory_version}')
        )

        async with self.client:
            # use the same client for both the request
            response_on_top_false = self.client.update_fact_in_theory(theory_name, functor, facts_p[0], on_top=False)
            response = self.client.update_fact_in_theory(theory_name, functor, facts_p[0])
            response_on_top_false, response = await asyncio.gather(response_on_top_false, response)

        self.assertTrue(request_on_top_false.called)
        self.assertEqual(response_on_top_false, build_theory_full_name(theory_name, theory_version))
        self.assertEqual(request_on_top_false.calls.last.request.headers['Authorization'], jwt_token)

        self.assertTrue(request.called)
        self.assertEqual(response, build_theory_full_name(theory_name, theory_version))
        self.assertEqual(request.calls.last.request.headers['Authorization'], jwt_token)
