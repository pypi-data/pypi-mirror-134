import datetime
import re
from typing import Any, List

from tuprolog.core.parsing import parse_term

from lpaas_client.core.model.goal import GoalName, GoalUrlName
from lpaas_client.core.model.theory import TheoryFullName
from lpaas_client.serializer import serialize_term

hook_regex = re.compile(r'/solutions/(?P<hook>\w+)')

Hook = str


class SolutionItem:
    """A single solution

    if success is False then solution is None
    """
    def __init__(self, success: bool, solution: str = None) -> None:
        """

        Note that you can use `tuprolog.unify` module, to unify the solution with your goals.

        e.g.

        >>> from tuprolog import unify
        >>> your_goal = Any
        >>> si: SolutionItem = Any
        >>> variables_value = unify.mgu(si.solution, your_goal)

        :param success: whether or not the solution is present
        :type success: bool
        :param solution: actual solution, have to be a valid term
        :type solution: str
        """
        self.success = success
        self.solution = parse_term(solution) if solution is not None else None

    def __repr__(self) -> str:
        return serialize_term(self.solution) + " | Yes." if self.success and self.solution is not None else "No."


class Solution:
    """A solution generated from the server"""

    def __init__(self,
                 theory: TheoryFullName,
                 goal_name: GoalName,
                 hook: Hook,
                 timestamp: datetime.datetime,
                 version: int,
                 solutions: List[Any] = None):
        """

        :param theory:  used in this solution
        :type theory: TheoryFullName
        :param goal_name: in this solution
        :type goal_name: GoalName
        :param hook: hook that point to this solution
        :type hook: Hook
        :param timestamp: of the creation of the solution
        :type timestamp: datetime.datetime
        :param version: sequential number of the solution
        :type version: int
        :param solutions: list of `SolutionItem` in json format
        :type solutions: List[Any]
        """
        self.theory = theory
        self.goal = goal_name
        hm = hook_regex.match(hook)
        if hm is None or hm.group('hook') is None:
            raise ValueError('Invalid hook')
        self.hook = hm.group('hook')
        self.version = version
        self.timestamp = timestamp
        self.solutions = solutions if solutions is None else [SolutionItem(**s) for s in solutions]

    def __eq__(self, other):
        if isinstance(other, Solution):
            return self.theory == other.theory \
                   and self.goal == other.goal \
                   and self.hook == other.hook \
                   and self.version == other.version
        return False

    def __repr__(self) -> str:
        return f'theory: {self.theory}\ngoal: {self.goal}\nhook: {self.hook}\nsolutions: {self.solutions}\nversion: {self.version}\ntimestamp: {self.timestamp}'


def build_solution_from_json(solution_json) -> Solution:
    str_GTM_format = '%d %b %Y %H:%M:%S GMT'
    return Solution(theory=TheoryFullName(solution_json['theory']),
                    goal_name=GoalUrlName(solution_json['goalList']).to_name,
                    hook=solution_json['hook'],
                    version=solution_json['version'],
                    timestamp=datetime.datetime.strptime(solution_json['timestamp'], str_GTM_format),
                    solutions=solution_json['solutions'] if 'solutions' in solution_json else None)
