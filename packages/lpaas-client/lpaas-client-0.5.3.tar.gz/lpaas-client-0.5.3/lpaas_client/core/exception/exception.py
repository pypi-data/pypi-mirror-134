from typing import Union


def _get_or_empty(s: str = None) -> str:
    return "" if s is None else s


class Unauthorized(Exception):
    """Unauthorized, username and/or password are incorrect"""
    pass


class NotFoundException(Exception):
    def __init__(self, what: str, *args):
        super(NotFoundException, self).__init__(f'{_get_or_empty(what)} not found!', *args)


class GoalNotFoundException(NotFoundException):
    def __init__(self, goal_name: str, *args):
        super(GoalNotFoundException, self).__init__(f"Goal {_get_or_empty(goal_name)}", *args)


class SolutionNotFoundException(NotFoundException):
    def __init__(self, solution_hook: str = None, *args):
        super(SolutionNotFoundException, self).__init__(f'solution {_get_or_empty(solution_hook)}', *args)


class TheoryNotFoundException(NotFoundException):
    def __init__(self, theory_name: str, *args):
        super(TheoryNotFoundException, self).__init__(f'Theory {_get_or_empty(theory_name)}', *args)


class GoalAlreadyExistsException(Exception):
    pass


class TheoryAlreadyExistsException(Exception):
    pass


class SolutionAlreadyExistsException(Exception):
    pass


class MissingFactsException(Exception):
    pass
