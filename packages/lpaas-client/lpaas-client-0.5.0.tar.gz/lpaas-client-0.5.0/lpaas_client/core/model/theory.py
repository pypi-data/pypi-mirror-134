import re
from typing import List, Union

from tuprolog.theory import Theory

full_name_regex = re.compile(r'/theories/(?P<name>\w+)/history/(?P<version>\d+)')
theory_update_fact_regex = re.compile(r'/theories/(?P<name>\w+)/facts/(?P<functor>\w+)/history/(?P<version>\d+)')


class TheoryName(str):
    """Theory base name, without version"""
    @property
    def to_url(self):
        return f'/theories/{self}'


class TheoryFullName:
    """Theory full name, with version

    Define useful methods to work with theory name.
    """
    name: TheoryName
    version: int

    def __init__(self, theory_full_name: Union[TheoryName, str]):
        """

        :param theory_full_name: should match  "/theories/(?P<name>\w+)/history/(?P<version>\d+)"
        :type theory_full_name: str
        """
        m = full_name_regex.match(theory_full_name)
        if m is None:
            raise ValueError('Invalid theory_full_name')
        self.name = TheoryName(m.group('name'))
        self.version = int(m.group('version'))

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, TheoryFullName):
            return other.name == self.name and other.version == self.version
        return False

    @property
    def url_with_version(self):
        return f'/theories/{self.name}/history/{self.version}'


class TheoryData:
    """Container for theory"""
    full_name: TheoryFullName
    theory: Theory

    def __init__(self, full_name: TheoryFullName, theory: Theory):
        """

        :param full_name: name of the theory
        :type full_name: TheoryFullName
        :param theory: actual Theory
        :type theory: Theory
        """
        self.full_name = full_name
        self.theory = theory


def build_theory_full_name(theory_name: Union[TheoryName, str], version: int) -> TheoryFullName:
    return TheoryFullName(f'/theories/{theory_name}/history/{version}')


def parse_theory_fact_update(update: str) -> TheoryFullName:
    r = theory_update_fact_regex.match(update)
    if r is None:
        raise ValueError('Invalid updated str for theory fact update')
    return build_theory_full_name(TheoryName(r.group('name')), int(r.group('version')))


def parse_get_theories_body(body: str) -> List[TheoryFullName]:
    elements = body.split('\n')
    assert elements[0] == 'Available theories:'
    return [TheoryFullName(t) for t in elements[1:]]


def _get_theory_name(theory: Union[TheoryName, TheoryFullName, str]) -> str:
    """Retrieves the theory name from different sources"""
    name = theory
    if isinstance(name, TheoryFullName):
        name = name.name
    return name
