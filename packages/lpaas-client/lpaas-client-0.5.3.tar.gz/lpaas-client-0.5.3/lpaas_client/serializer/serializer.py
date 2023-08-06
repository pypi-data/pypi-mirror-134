from typing import List

from tuprolog.core import Term, EmptyList
from tuprolog.core.operators import DEFAULT_OPERATORS
from tuprolog.theory import Theory

excluded_operators = [':-']
prolog_operators = list(
    filter(lambda o: o not in excluded_operators,
           map(lambda x: str(x.functor),
               list(DEFAULT_OPERATORS))))


def serialize_term(term: Term) -> str:
    """Convert Term to str

    Keyword arguments:
    term: Term -- the term to serialize.

    You can look at :class:`tests.serializer.test_serializer.Test` for example.

    return the serialized term
    """

    if not isinstance(term, Term):
        raise TypeError('Can not serialize non Term type.')

    if term.isVar():
        return str(term.name)
    elif term.isConstant():
        return str(term)
    elif term.isTuple():
        def explore_tuple(_tuple, acc=None):
            if _tuple.right.isTuple() and acc is None:
                return explore_tuple(_tuple.right, acc=serialize_term(_tuple.left))
            if _tuple.right.isTuple():
                return explore_tuple(_tuple.right, acc=f"{acc}, {serialize_term(_tuple.left)}")
            if acc is None:
                return f'{serialize_term(_tuple.left)}, {serialize_term(_tuple.right)}'
            return f'{acc}, {serialize_term(_tuple.left)}, {serialize_term(_tuple.right)}'

        return f'{explore_tuple(term)}'

    elif term.isList():
        def explore_tail(_list, acc=None):
            if isinstance(_list, EmptyList):
                # case empty list
                return ''
            if acc is None:
                # case first invocation
                if isinstance(_list.tail, EmptyList):
                    # case only one element in the tail
                    return serialize_term(_list.head)
                # case begin of the tail
                return explore_tail(_list.tail, serialize_term(_list.head))
            curr_acc = f'{acc}, {serialize_term(_list.head)}'
            if isinstance(_list.tail, EmptyList):
                # case end of the recursion
                return curr_acc
            # case base recursion
            return explore_tail(_list.tail, curr_acc)

        if len(term.args) == 0:
            # empty list
            return '[]'
        if isinstance(term.tail, EmptyList):
            return f'[{serialize_term(term.head)}]'
        if term.tail.isVar():
            return f'[{serialize_term(term.head)}|{serialize_term(term.tail)}]'
        return f'[{serialize_term(term.head)}|[{explore_tail(term.tail)}]]'

    elif term.isClause():
        # head functor body.
        head = serialize_term(term.head)
        functor = str(term.functor)
        functor = functor if functor not in prolog_operators else f"'{functor}'"
        body = serialize_term(term.body)
        return f'{head} {functor} {body}.'
    elif term.isStruct():
        # functor(args*,)
        args = list(map(serialize_term, term.args))
        functor = str(term.functor)
        functor = functor if functor not in prolog_operators else f"'{functor}'"
        if len(args) == 0:
            return functor
        return f'{functor}({", ".join(args)})'

    raise ValueError(f'Invalid input {term} with type {type(term)}')


def serialize_term_list(terms: List[Term]):
    return list(map(serialize_term, terms))


def serialize_theory(_theory: Theory) -> str:
    """
        Serialize a theory to str.

        Look #serialize_term for more information.
    """
    return ''.join(map(lambda x: serialize_term(x) + '\n', list(_theory)))
