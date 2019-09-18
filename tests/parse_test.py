import math
import unittest

from py_range_parse import parse_range


class ParseTest(unittest.TestCase):

    def test_parse_equal_values(self):
        parsed_range = parse_range("[-inf..-inf]")
        self.assertIn(-math.inf, parsed_range)

    def test_parse_spaces(self):
        parsed_range = parse_range("[ -8.3 .. +18.3 ]")
        self.assertIn(-8.3, parsed_range)
        self.assertIn(18.3, parsed_range)

    def test_parse_all_values(self):
        parsed_range = parse_range("[-inf..∞]")
        self.assertIn(-math.inf, parsed_range)
        self.assertIn(math.inf, parsed_range)

    def test_parse_range_negative(self):
        parsed_range = parse_range("[-5..-2]")
        self.assertEqual(parsed_range.start, -5)
        self.assertEqual(parsed_range.end, -2)

    def test_parse_range_negative_inverted(self):
        parsed_range = parse_range("[5..-2]")
        self.assertEqual(parsed_range.start, -2)
        self.assertEqual(parsed_range.end, 5)

    def test_float_range_contains(self):
        parsed_range = parse_range("[1.0..4.3]")

        self.assertIn(1, parsed_range)
        self.assertIn(1.0, parsed_range)

        self.assertIn(2, parsed_range)
        self.assertIn(2.0, parsed_range)
        self.assertIn(2.1, parsed_range)

        self.assertIn(4, parsed_range)
        self.assertIn(4.3, parsed_range)

    def test_int_range_contains(self):
        parsed_range = parse_range("[1..4]")

        self.assertIn(1, parsed_range)
        self.assertIn(1.0, parsed_range)

        self.assertIn(2, parsed_range)
        self.assertIn(2.0, parsed_range)
        self.assertNotIn(2.1, parsed_range)

        self.assertIn(4, parsed_range)
        self.assertIn(4.0, parsed_range)

    def test_int_range_exclude(self):
        parsed_range = parse_range("]1..4[")
        assert parsed_range is not None

    def test_int_range_inf(self):
        parsed_range = parse_range("]-inf..4[")
        self.assertNotIn(-math.inf, parsed_range)
        self.assertIn(-10000000, parsed_range)

    def test_int_range_inf_inverted(self):
        parsed_range = parse_range("]inf..4[")
        self.assertNotIn(-math.inf, parsed_range)
        self.assertNotIn(3, parsed_range)
        self.assertNotIn(4, parsed_range)
        self.assertIn(4.000000001, parsed_range)
        self.assertIn(10000000, parsed_range)

    def test_int_inclusion_inverted(self):
        parsed_range = parse_range("]2..1]")
        self.assertNotIn(0, parsed_range)
        self.assertIn(1, parsed_range)
        self.assertNotIn(2, parsed_range)
        self.assertNotIn(3, parsed_range)
