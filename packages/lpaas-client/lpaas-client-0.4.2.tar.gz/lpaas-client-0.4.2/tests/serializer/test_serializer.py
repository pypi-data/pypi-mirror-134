from unittest import TestCase

from tuprolog.theory import Theory
from tuprolog.theory.parsing import parse_theory

from lpaas_client.serializer import serialize_theory, serialize_term
from tuprolog.core.parsing import parse_var, parse_struct, parse_clause


class Test(TestCase):

    def __serialize_term_test(self, term, expected_output, msg=''):
        serialized_term = serialize_term(term)
        self.assertEqual(serialized_term.strip(), expected_output.strip(),
                         f'Serializer must correctly serialize {msg if len(msg) > 0 else str(term)}')

    def test_serialize_terms(self):
        # test var
        self.__serialize_term_test(parse_var('X'), 'X', 'var')

        # test struct
        self.__serialize_term_test(parse_struct('p'), 'p', 'term')
        self.__serialize_term_test(parse_struct('p(a, X)'), 'p(a, X)', 'term with var')

        # test clause
        self.__serialize_term_test(parse_clause('p'), 'p :- true.', 'clause')
        self.__serialize_term_test(parse_clause('p(a, X)'), 'p(a, X) :- true.', 'clause with var')

        # test list
        self.__serialize_term_test(parse_struct('[1]'), '[1]', 'list')
        self.__serialize_term_test(parse_struct('p([1]) :- true.'), 'p([1]) :- true.', 'list')
        self.__serialize_term_test(parse_clause('p([1]).'), 'p([1]) :- true.', 'list clause')
        self.__serialize_term_test(parse_clause('p([1, X]).'), 'p([1|[X]]) :- true.', 'list clause with var')
        self.__serialize_term_test(parse_clause('p([1 | [X]]).'), 'p([1|[X]]) :- true.', 'list clause with var')
        self.__serialize_term_test(parse_clause('p([1, 2, 3]).'), 'p([1|[2, 3]]) :- true.', 'list clause with var')
        self.__serialize_term_test(parse_clause('p([H|T]) :- p(T).'), 'p([H|T]) :- p(T).', 'list clause with var')

    def test_serialize_terms_should_raise_type_error(self):
        with self.assertRaises(TypeError):
            serialize_term('invalid term')

    def test_serialize_theory(self):
        base_theory = """
        a.
        p(a, b).
        p(X) :- p(b).
        """

        t: Theory = parse_theory(base_theory)
        serialized_t = serialize_theory(t)
        self.assertEqual(serialized_t.strip(),
                         "a :- true.\np(a, b) :- true.\np(X) :- p(b).\n".strip(),
                         f'Serializer must correctly serialize theory')

        advanced_theory = """
        % TicTacToe with [[_,_,_],[_,_,x],[o,_,x]] representation

        % test
        % next([[_,_,_],[_,_,_],[_,_,_]], x, R, T).
        % game([[_,_,_],[_,_,_],[_,_,_]], x, even, T).
        % game([[E,_,_],
        %			  [E,_,_],
        %       [E,_,_]], x, R, T).
        
        % utils
        
        % opponent(+-Player, -+Opponent).
        opponent(o, x).
        opponent(x, o).
        
        % player(-Player).
        player(P) :- member(P, [x, o]).
        
        % nth(+List, +Position, -Element).
        nth([H|_], 0, E):- copy_term(H, E), !.
        nth([_|T], P, E):- P > 0, NP is P - 1, nth(T, NP, E).
        
        % nthn(+Table, +Position, -Element)
        nthn(T, P, E) :- copy_term(T, LL), member(R, LL), nth(R, P, E), ground(E).
        
        % interval(+Start, +End, -Actual)
        interval(A, B, A).
        interval(A, B, X):- A2 is A + 1, A2 < B, interval(A2, B, X).
        
        % end-utils
        
        % next(+Table, +Player, -Result, -NewTable).
        next(T, P, R, NT):-
            copy_term(T, NT),
            member(L, NT),
            member(E, L),
            not(ground(E)),
            P = E,
            result(NT, R).
        
        % game(+Table, +Player, -Result, -NewTable).
        game(T, P, R, T):- 
            result(T, R),
            R \= nothing, !.
        
        game(T, P, R, NT):-
          next(T, P, R2, Y),
          opponent(P, O),
          game(Y, O, R, NT).
        
        % result(+Table, -Result).
        result(T, win(P)) :- player(P), check(T, P), !.
        result(T, even) :- ground(T), !.
        result(T, nothing).
        
        % check(+Table, +Player).
        check(T, P) :- lane_check(T, P), !.
        check(T, P) :- column_check(T, P), !.
        check(T, P) :- diagonal_check1(T, P), !.
        check(T, P) :- diagonal_check2(T, P), !.
        
        % check_tris(+Tris, +Player).
        check_tris(Tris, P):-
            ground(Tris),
            Tris = [P, P, P].
        
        % lane_check(+Table, +Player).
        lane_check(T, P) :- 
            member(L, T),
            check_tris(L, P).
        
        
        % column_check(+Table, +Player).
        column_check(T, P) :-
            copy_term(T, NT),
            interval(0, 3, N),
            workaround(NT, N, L),
            check_tris(L, P), !.
        
        workaround(T, N, L):- findall(E, nthn(T, N, E), L).
        
        % column_check(T, P) :-
        %		copy_term(T, NT),
        %		interval(0, 3, N),
        %		findall(E, nthn(T, N, E), L),
        %		check_tris(L, P), !.
        
        % diagonal_check1(+Table, +Player).
        diagonal_check1([[E0|_],[_,E1,_],[_,_,E2]], P) :- 
            check_tris([E0, E1, E2], P).
        
        % diagonal_check2(+Table, +Player).
        diagonal_check2(T, P):- reverse(T, TR), diagonal_check1(TR, P).

        """

        t: Theory = parse_theory(advanced_theory)
        serialized_t = serialize_theory(t)
        self.assertEqual(serialized_t.strip().replace(' ', ''),
                         "opponent(o, x) :- true.\n"
                         "opponent(x, o) :- true.\n"
                         "player(P) :- member(P, [x|[o]]).\n"
                         "nth([H|_], 0, E):- copy_term(H, E), '!'.\n"
                         "nth([_|T], P, E):- '>'(P, 0), 'is'(NP,'-'(P,1)), nth(T, NP, E).\n"
                         "nthn(T, P, E) :- copy_term(T, LL), member(R, LL), nth(R, P, E), ground(E).\n"
                         "interval(A, B, A) :- true.\n"
                         "interval(A, B, X):- 'is'(A2,'+'(A,1)),'<'(A2,B), interval(A2, B, X).\n"
                         "next(T, P, R, NT):-copy_term(T, NT),member(L, NT),member(E, L),not(ground(E)),'='(P,E),result(NT, R).\n"
                         "game(T, P, R, T):- result(T, R), '\\='(R,nothing), '!'.\n"
                         "game(T, P, R, NT):- next(T, P, R2, Y), opponent(P, O),  game(Y, O, R, NT).\n"
                         "result(T, win(P)) :- player(P), check(T, P), '!'.\n"
                         "result(T, even) :- ground(T), '!'.\n"
                         "result(T, nothing) :- true.\n"
                         "check(T, P) :- lane_check(T, P), '!'.\n"
                         "check(T, P) :- column_check(T, P), '!'.\n"
                         "check(T, P) :- diagonal_check1(T, P), '!'.\n"
                         "check(T, P) :- diagonal_check2(T, P), '!'.\n"
                         "check_tris(Tris, P):- ground(Tris), '='(Tris,[P|[P,P]]).\n"
                         "lane_check(T, P) :- member(L, T), check_tris(L, P).\n"
                         "column_check(T, P) :- copy_term(T, NT), interval(0, 3, N), workaround(NT, N, L), check_tris(L, P), '!'.\n"
                         "workaround(T, N, L):- findall(E, nthn(T, N, E), L).\n"
                         "diagonal_check1([[E0|_]|[[_|[E1,_]],[_|[_,E2]]]], P) :- check_tris([E0 | [E1, E2]], P).\n"
                         "diagonal_check2(T, P):- reverse(T, TR), diagonal_check1(TR, P).\n"
                         .strip().replace(' ', ''),
                         f'Serializer must correctly serialize theory')