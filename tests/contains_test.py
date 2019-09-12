import math
import unittest

from py_range_parse import Range


class ContainsTest(unittest.TestCase):

    @staticmethod
    def test_contains_int_range():
        int_range = Range(0, 5)
        assert -1 not in int_range
        assert 0 in int_range
        assert 3 in int_range
        assert 3.3 not in int_range
        assert 3.0 in int_range
        assert 5 in int_range
        assert 6 not in int_range

    @staticmethod
    def test_contains_int_range_exclusive():
        int_range = Range(0, 2, False, False)
        assert 0 not in int_range
        assert 1 in int_range
        assert 2 not in int_range

    @staticmethod
    def test_contains_int_range_inverted():
        int_range = Range(2, 0)
        assert -1 not in int_range
        assert 0 in int_range
        assert 1 in int_range
        assert 2 in int_range
        assert 3 not in int_range

    @staticmethod
    def test_contains_int_range_negative():
        int_range = Range(-5, -2)
        assert -6 not in int_range
        assert -3 in int_range
        assert -2 in int_range
        assert -1 not in int_range

    @staticmethod
    def test_contains_int_range_over_zero():
        int_range = Range(-5, 5)
        assert -6 not in int_range
        assert -5 in int_range
        assert 0 in int_range
        assert 5 in int_range
        assert 6 not in int_range

    @staticmethod
    def test_contains_float_range():
        float_range = Range(0.0, 5.2)
        assert -1.0 not in float_range
        assert -0.0 in float_range
        assert 0.0 in float_range
        assert 0 in float_range
        assert 3 in float_range
        assert 3.0 in float_range
        assert 3.3 in float_range
        assert 5 in float_range
        assert 5.2 in float_range
        assert 5.3 not in float_range

    @staticmethod
    def test_contains_float_range_exclusive():
        float_range = Range(0.0, 2, False, False)
        assert 0 not in float_range
        assert 0.1 in float_range
        assert 1 in float_range
        assert 2 not in float_range

    @staticmethod
    def test_contains_float_range_inverted():
        float_range = Range(2, 0)
        assert -1 not in float_range
        assert 0 in float_range
        assert 1 in float_range
        assert 2 in float_range
        assert 3 not in float_range

    @staticmethod
    def test_contains_float_range_negative():
        float_range = Range(-5, -2)
        assert -6 not in float_range
        assert -3 in float_range
        assert -2 in float_range
        assert -1 not in float_range

    @staticmethod
    def test_contains_float_range_over_zero():
        float_range = Range(-5, 5)
        assert -6 not in float_range
        assert -5 in float_range
        assert 0 in float_range
        assert 5 in float_range
        assert 6 not in float_range

    @staticmethod
    def test_contains_float_infinity():
        float_range = Range(-math.inf, 5)
        assert -math.inf in float_range
        assert -10000 in float_range
        assert -6 in float_range
        assert -5 in float_range
        assert 0 in float_range
        assert 5 in float_range
        assert 6 not in float_range
