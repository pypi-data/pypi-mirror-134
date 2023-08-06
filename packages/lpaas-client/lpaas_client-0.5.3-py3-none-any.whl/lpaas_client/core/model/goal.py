import re
from typing import List

from tuprolog.core import Term
from tuprolog.core.parsing import parse_term

from lpaas_client.serializer import serialize_term

GOALS_PATH = '/goals'
goal_name_regex = re.compile(r'/goals/(?P<name>\w+)')


class GoalName(str):
    """The name of a goal"""
    @property
    def to_url(self):
        return GoalUrlName(f'{GOALS_PATH}/{self}')


class GoalUrlName(str):
    """The complete name of a goal in the form of '/goals/<goal name>'"""
    @property
    def to_name(self) -> GoalName:
        try:
            return GoalName(goal_name_regex.match(self).group('name'))
        except AttributeError:
            raise ValueError('Invalid goal_full_name')


GoalList = List[Term]


def parse_goal_lists_body(body: str) -> List[GoalName]:
    values = body.split('\n')
    assert values[0] == 'Available goals:'

    return [GoalUrlName(f_n).to_name for f_n in values[1:]]


def parse_goal_body(body: str) -> Term:
    return parse_term(body)


def parse_goal_index_body(body: str) -> Term:
    return parse_term(body)


def get_serialized_goals(goal: GoalList) -> str:
    return ', '.join([serialize_term(t) for t in goal])
