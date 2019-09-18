import math
import unittest

from py_range_parse import Range


class StrTest(unittest.TestCase):

    def test_str_inf(self):
        int_range = Range(-math.inf, math.inf)
        self.assertEqual(str(int_range), "[-inf..inf]")

    def test_str_float(self):
        int_range = Range(-4.2123, 123.4324)
        self.assertEqual(str(int_range), "[-4.2123..123.4324]")

    def test_str_int(self):
        int_range = Range(-4, 123)
        self.assertEqual(str(int_range), "[-4..123]")

    def test_str_exclusive(self):
        int_range = Range(123, -4, False, False)
        self.assertEqual(str(int_range), "]-4..123[")
