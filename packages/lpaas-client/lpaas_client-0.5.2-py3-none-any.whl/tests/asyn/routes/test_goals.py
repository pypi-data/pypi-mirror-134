import asyncio

import asynctest

import respx
from httpx import URL, Response, QueryParams
from tuprolog.core.parsing import parse_struct

from lpaas_client.core.model.auth import AuthData
from lpaas_client.core.model.goal import GoalName
from lpaas_client.serializer import serialize_term
from lpaas_client.asyn.routes.goals import GoalClient
from tests.serializer.utils import compare_terms_with_var

base_url = URL('http://localhost8080')
jwt_token = 'token!1'
goal_struct_1 = parse_struct('a')
goal_struct_2 = parse_struct('p(X, a)')
goal_list = [goal_struct_1, goal_struct_2]
goal_name = GoalName('default')


class TestGoalClient(asynctest.TestCase):
    client: GoalClient

    @classmethod
    @respx.mock
    async def setUp(cls) -> None:
        cls.client = GoalClient(base_url=base_url)

        respx.post(base_url.join('/lpaas/auth')).mock(
                return_value=Response(status_code=200, json={'token': jwt_token}))

        await cls.client.authenticate(AuthData('user', 'password'))

    def test_can_create_client(self):
        self.assertIsInstance(self.client, GoalClient)

    @respx.mock
    async def test_can_add_new_goal_list(self):
        request = respx.post(base_url.join(f'/lpaas/goals')).mock(
                return_value=Response(status_code=200, content=f'/goals/{goal_name}'))

        await self.client.add_new_goal_list(goal_name, goal_list)

        self.assertTrue(request.called)
        self.assertTrue(request.calls.last.request.url.params, QueryParams({'name': goal_name}))
        self.assertEqual(request.calls.last.request.content.decode('utf-8'),
                         f'{serialize_term(goal_struct_1)}, {serialize_term(goal_struct_2)}')

    @respx.mock
    async def test_get_goal_list(self):
        requests = respx.get(base_url.join(f'/lpaas/goals/{goal_name}')).mock(
                return_value=Response(status_code=200,
                                      content=f'{serialize_term(goal_struct_1)}, {serialize_term(goal_struct_2)}')
        )

        goal_list_response = await self.client.get_goal_list(goal_name)
        self.assertTrue(requests.called)
        for correct, response in zip(goal_list, goal_list_response):
            self.assertTrue(compare_terms_with_var(correct, response))

    @respx.mock
    async def test_get_goal_lists(self):
        requests = respx.get(base_url.join(f'/lpaas/goals')).mock(
                return_value=Response(status_code=200,
                                      content='Available goals:\n/goals/default1\n/goals/test2')
        )

        response = await self.client.get_goal_lists()
        self.assertTrue(requests.called)
        self.assertEqual(response, [GoalName('default1'),
                                    GoalName('test2')])

    @respx.mock
    async def test_get_sub_goal(self):
        index = 0
        requests = respx.get(base_url.join(f'/lpaas/goals/{goal_name}/{index}')).mock(
                return_value=Response(status_code=200,
                                      content='goal_a')
        )

        response = await self.client.get_sub_goal(goal_name, index)
        self.assertTrue(requests.called)
        self.assertEqual(response, parse_struct('goal_a'))

    @respx.mock
    async def test_remove_goal_list(self):
        requests = respx.delete(base_url.join(f'/lpaas/goals/{goal_name}')) % 204

        await self.client.remove_goal_list(goal_name)

        self.assertTrue(requests.called)

    @respx.mock
    async def test_replace_goal_list(self):
        requests = respx.put(base_url.join(f'/lpaas/goals/{goal_name}')) % 204

        await self.client.replace_goal_list(GoalName(goal_name), goal_list)

        self.assertTrue(requests.called)
        self.assertEqual(requests.calls.last.request.content.decode('utf-8'),
                         f'{serialize_term(goal_struct_1)}, {serialize_term(goal_struct_2)}')

    @respx.mock
    async def test_add_new_sub_goal(self):
        requests = respx.post(base_url.join(f'/lpaas/goals/{goal_name}')) % 200

        await self.client.add_sub_goal(goal_name, parse_struct('term'))

        self.assertTrue(requests.called)

    @respx.mock
    async def test_add_new_sub_goal_with_context(self):
        requests = respx.post(base_url.join(f'/lpaas/goals/{goal_name}')) % 200
        async with self.client:
            await self.client.add_sub_goal(goal_name, parse_struct('term'))

        self.assertTrue(requests.called)

    @respx.mock
    async def test_multiple_call_in_with_statement(self):
        request = respx.post(base_url.join(f'/lpaas/goals')).mock(
                return_value=Response(status_code=200, content=f'/goals/{goal_name}'))

        async with self.client:
            # make more requests with the same client
            r1 = self.client.add_new_goal_list(goal_name, goal_list)
            r2 = self.client.add_new_goal_list(goal_name, goal_list)
            r3 = self.client.add_new_goal_list(goal_name, goal_list)

            await asyncio.gather(r1, r2, r3)
        self.assertTrue(request.called)
        self.assertEqual(len(request.calls), 3)
