import datetime
import json
from unittest import TestCase
import respx
from http_constants.headers import HttpHeaders
from httpx import Response, URL, Request

from lpaas_client.core.model.goal import GoalName
from lpaas_client.core.model.solution import Solution
from lpaas_client.core.model.theory import TheoryName, build_theory_full_name
from lpaas_client.sync.routes.solutions import SolutionsClient

base_url = URL('https://localhost:8080')
str_GTM_format = '%d %b %Y %H:%M:%S GMT'  # this is the standard used by server


class TestSolutionsClient(TestCase):
    client: SolutionsClient

    @classmethod
    def setUp(cls) -> None:
        cls.client = SolutionsClient(base_url)

    @respx.mock
    def test_add_new_solution(self):
        time_now = datetime.datetime.now().replace(microsecond=0)

        def elaborate_new_solution_response(_request: Request) -> Response:
            time_now_GTM = time_now.strftime(str_GTM_format)
            req_json = json.loads(_request.content)
            return Response(status_code=200,
                            headers={HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json},
                            json={
                                'hook'     : '/solutions/' + _request.url.params['hook'],
                                # in test we always want an hook
                                'theory'   : req_json['theory'] + '/history/0',
                                'goalList' : req_json['goals'],
                                'solutions': [
                                    {
                                        'success' : True,
                                        'solution': 'p(a)'
                                    }
                                ],
                                'timestamp': time_now_GTM,
                                'version'  : 0
                            })

        request = respx.post(base_url.join('/lpaas/solutions')).mock(side_effect=elaborate_new_solution_response)

        result = self.client.add_new_solution(TheoryName('th'),
                                              GoalName('gn'),
                                              hook='hook')

        self.assertTrue(request.called)
        self.assertEqual(result.goal, GoalName('gn'))
        self.assertEqual(result.theory, build_theory_full_name(TheoryName('th'), 0))
        self.assertEqual(result.hook, 'hook')
        self.assertEqual(result.timestamp, time_now)

    @respx.mock
    def test_get_hook(self):
        request = respx.get(base_url.join('/lpaas/solutions/a')).mock(
                return_value=Response(200, content="""
            {
                "hook": "/solutions/a",
                "version": 213,
                "theory": "/theories/default/history/0",
                "goalList": "/goals/default",
                "timestamp": "3 Jan 2022 09:06:41 GMT",
                "solutions": [{"success": false}]
            }
        """))
        hook = self.client.get_hook('a')

        self.assertEqual(hook, Solution(
                theory=build_theory_full_name('default', 0),
                goal_name=GoalName('default'),
                version=213,
                timestamp=datetime.datetime.strptime('3 Jan 2022 09:06:41 GMT', str_GTM_format),
                hook='/solutions/a'
        ))

    @respx.mock
    def test_get_hooks(self):
        request = respx.get(base_url.join('/lpaas/solutions')).mock(
                return_value=Response(200, content="""[
        {
            "hook": "/solutions/a",
            "version": 213,
            "theory": "/theories/default/history/0",
            "goalList": "/goals/default",
            "timestamp": "3 Jan 2022 09:06:41 GMT",
            "solutions": [{"success": false}]
        },
        {
            "hook": "/solutions/acab",
            "version": 0,
            "theory": "/theories/default/history/0",
            "goalList": "/goals/default",
            "timestamp": "3 Jan 2022 09:06:47 GMT",
            "solutions": [{"success": false}]
        }
    ]"""))
        hooks = self.client.get_hooks()

        self.assertEqual(hooks[0], Solution(
                theory=build_theory_full_name('default', 0),
                goal_name=GoalName('default'),
                version=213,
                timestamp=datetime.datetime.strptime('3 Jan 2022 09:06:41 GMT', str_GTM_format),
                hook='/solutions/a'
        ))
        self.assertEqual(hooks[1].theory, build_theory_full_name(TheoryName('default'), 0))

    @respx.mock
    def test_get_hook_version(self):
        request = respx.get(base_url.join('/lpaas/solutions/a/history/12')).mock(
                return_value=Response(200, content="""
            {
                "hook": "/solutions/a",
                "version": 12,
                "theory": "/theories/default/history/0",
                "goalList": "/goals/default",
                "timestamp": "3 Jan 2022 09:06:41 GMT",
                "solutions": [{"success": false}]
            }
        """))
        hook = self.client.get_hook('a', 12)

        self.assertEqual(hook, Solution(
                theory=build_theory_full_name('default', 0),
                goal_name=GoalName('default'),
                version=12,
                timestamp=datetime.datetime.strptime('3 Jan 2022 09:06:41 GMT', str_GTM_format),
                hook='/solutions/a'
        ))

    @respx.mock
    def test_remove_all(self):
        request = respx.delete(base_url.join('lpaas/solutions')) % 204
        self.client.remove_all()

        self.assertTrue(request.called)

    @respx.mock
    def test_remove_hook(self):
        request = respx.delete(base_url.join('lpaas/solutions/a')) % 204
        self.client.remove_hook('a')

        self.assertTrue(request.called)

    @respx.mock
    def test_remove_hook_version(self):
        request = respx.delete(base_url.join('lpaas/solutions/a/history/12')) % 204
        self.client.remove_hook('a', 12)

        self.assertTrue(request.called)
