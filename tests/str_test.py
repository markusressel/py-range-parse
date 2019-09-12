import math
import unittest

from py_range_parse import Range


class StrTest(unittest.TestCase):

    @staticmethod
    def test_str_inf():
        int_range = Range(-math.inf, math.inf)
        assert str(int_range) == "[-inf..inf]"

    @staticmethod
    def test_str_float():
        int_range = Range(-4.2123, 123.4324)
        assert str(int_range) == "[-4.2123..123.4324]"

    @staticmethod
    def test_str_int():
        int_range = Range(-4, 123)
        assert str(int_range) == "[-4..123]"

    @staticmethod
    def test_str_exclusive():
        int_range = Range(123, -4, False, False)
        assert str(int_range) == "]-4..123["
