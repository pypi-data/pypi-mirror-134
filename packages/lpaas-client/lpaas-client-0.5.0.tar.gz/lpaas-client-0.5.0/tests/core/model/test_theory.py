from unittest import TestCase

from lpaas_client.core.model.theory import *
from lpaas_client.core.model.theory import _get_theory_name


class TestTheoryFunctions(TestCase):
    def test_build_theory_full_name(self):
        tfn = build_theory_full_name('name', 1)
        self.assertEqual(tfn, TheoryFullName('/theories/name/history/1'))

    def test_parse_theory_fact_update(self):
        update = '/theories/name/facts/p/history/3'
        parsed = parse_theory_fact_update(update)
        self.assertEqual(parsed, TheoryFullName('/theories/name/history/3'))

    def test_parse_get_theories_body(self):
        update = "Available theories:\n" \
                 "/theories/name1/history/12\n" \
                 "/theories/name2/history/7"
        lst_tfn: List[TheoryFullName] = parse_get_theories_body(update)
        self.assertListEqual(lst_tfn, [
            TheoryFullName("/theories/name1/history/12"),
            TheoryFullName("/theories/name2/history/7"),
        ])

    def test_get_theory_name(self):
        theory_full_name = TheoryFullName("/theories/some_name/history/12")
        theory_name = _get_theory_name(theory_full_name)
        self.assertEqual(theory_name, 'some_name')
        self.assertEqual(_get_theory_name('a_name'), 'a_name')

    def test_theory_name(self):
        tn = TheoryName('a_name')
        self.assertEqual(tn.to_url, '/theories/a_name')

    def test_theory_full_name(self):
        tfn = TheoryFullName("/theories/name2/history/7")
        self.assertEqual(tfn.name, 'name2')
        self.assertEqual(tfn.version, 7)
        self.assertEqual(tfn.url_with_version, '/theories/name2/history/7')

        with self.assertRaises(ValueError):
            # the theory name is invalid
            TheoryFullName('/theory/name2/history/7')

        self.assertFalse(
                TheoryFullName('/theories/name2/history/7') == TheoryFullName('/theories/name2/history/8')
        )
