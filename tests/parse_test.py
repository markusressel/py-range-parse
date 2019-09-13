import math
import unittest

from py_range_parse import parse_range


class ParseTest(unittest.TestCase):

    @staticmethod
    def test_parse_equal_values():
        parsed_range = parse_range("[-inf..-inf]")
        assert -math.inf in parsed_range

    @staticmethod
    def test_parse_spaces():
        parsed_range = parse_range("[ -8.3 .. +18.3 ]")
        assert -8.3 in parsed_range
        assert 18.3 in parsed_range
        
    @staticmethod
    def test_parse_all_values():
        parsed_range = parse_range("[-inf..∞]")
        assert -math.inf in parsed_range
        assert math.inf in parsed_range

    @staticmethod
    def test_parse_range_negative():
        parsed_range = parse_range("[-5..-2]")
        assert parsed_range.start == -5
        assert parsed_range.end == -2

    @staticmethod
    def test_parse_range_negative_inverted():
        parsed_range = parse_range("[5..-2]")
        assert parsed_range.start == -2
        assert parsed_range.end == 5

    @staticmethod
    def test_float_range_contains():
        parsed_range = parse_range("[1.0..4.3]")

        assert 1 in parsed_range
        assert 1.0 in parsed_range

        assert 2 in parsed_range
        assert 2.0 in parsed_range
        assert 2.1 in parsed_range

        assert 4 in parsed_range
        assert 4.3 in parsed_range

    @staticmethod
    def test_int_range_contains():
        parsed_range = parse_range("[1..4]")

        assert 1 in parsed_range
        assert 1.0 in parsed_range

        assert 2 in parsed_range
        assert 2.0 in parsed_range
        assert 2.1 not in parsed_range

        assert 4 in parsed_range
        assert 4.0 in parsed_range

    @staticmethod
    def test_int_range_exclude():
        parsed_range = parse_range("]1..4[")
        assert parsed_range is not None

    @staticmethod
    def test_int_range_inf():
        parsed_range = parse_range("]-inf..4[")
        assert -math.inf not in parsed_range
        assert -10000000 in parsed_range

    @staticmethod
    def test_int_range_inf_inverted():
        parsed_range = parse_range("]inf..4[")
        assert -math.inf not in parsed_range
        assert 3 not in parsed_range
        assert 4 not in parsed_range
        assert 4.000000001 in parsed_range
        assert 10000000 in parsed_range
