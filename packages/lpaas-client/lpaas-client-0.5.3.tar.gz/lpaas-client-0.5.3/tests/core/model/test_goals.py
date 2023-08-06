from unittest import TestCase

from tuprolog.core.parsing import parse_struct

from lpaas_client.core.model.goal import parse_goal_lists_body, parse_goal_body, parse_goal_index_body, GoalName
from lpaas_client.serializer import serialize_term


class GoalTests(TestCase):
    def test_parse_goal_list_body(self):
        goal_name = GoalName('default')
        body = f'Available goals:\n{goal_name.to_url}'
        result = parse_goal_lists_body(body)
        self.assertListEqual([goal_name], result)

        goal_name_2 = GoalName('default2')
        body = f'Available goals:\n{goal_name.to_url}\n{goal_name_2.to_url}'
        result = parse_goal_lists_body(body)
        self.assertListEqual([goal_name, goal_name_2], result)

    def test_parse_goal_body(self):
        body = 'is_default, p(X)'
        correct_result = [parse_struct('is_default'), parse_struct('p(X)')]
        parsed_result = parse_goal_body(body)

        # Note that in this case the serialize_term function help us to evaluate as equal two
        # variable with the same name, even if this two variable do not unify.
        self.assertEqual(', '.join(list(map(serialize_term, correct_result))), serialize_term(parsed_result))

    def test_parse_goal_index_body(self):
        body = 'is_default'
        self.assertEqual(serialize_term(parse_struct(body)), serialize_term(parse_goal_index_body(body)))
