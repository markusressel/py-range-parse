import math
import unittest

from py_range_parse import Range


class ContainsTest(unittest.TestCase):

    def test_contains_int_range(self):
        int_range = Range(0, 5)
        self.assertNotIn(-1, int_range)
        self.assertIn(0, int_range)
        self.assertIn(3, int_range)
        self.assertNotIn(3.3, int_range)
        self.assertIn(3.0, int_range)
        self.assertIn(5, int_range)
        self.assertNotIn(6, int_range)

    def test_contains_int_range_exclusive(self):
        int_range = Range(0, 2, False, False)
        self.assertNotIn(0, int_range)
        self.assertIn(1, int_range)
        self.assertNotIn(2, int_range)

    def test_contains_int_range_inverted(self):
        int_range = Range(2, 0)
        self.assertNotIn(-1, int_range)
        self.assertIn(0, int_range)
        self.assertIn(1, int_range)
        self.assertIn(2, int_range)
        self.assertNotIn(3, int_range)

    def test_contains_int_range_negative(self):
        int_range = Range(-5, -2)
        self.assertNotIn(-6, int_range)
        self.assertIn(-3, int_range)
        self.assertIn(-2, int_range)
        self.assertNotIn(-1, int_range)

    def test_contains_int_range_over_zero(self):
        int_range = Range(-5, 5)
        self.assertNotIn(-6, int_range)
        self.assertIn(-5, int_range)
        self.assertIn(0, int_range)
        self.assertIn(5, int_range)
        self.assertNotIn(6, int_range)

    def test_contains_float_range(self):
        float_range = Range(0.0, 5.2)
        self.assertNotIn(-1.0, float_range)
        self.assertIn(-0.0, float_range)
        self.assertIn(0.0, float_range)
        self.assertIn(0, float_range)
        self.assertIn(3, float_range)
        self.assertIn(3.0, float_range)
        self.assertIn(3.3, float_range)
        self.assertIn(5, float_range)
        self.assertIn(5.2, float_range)
        self.assertNotIn(5.3, float_range)

    def test_contains_float_range_exclusive(self):
        float_range = Range(0.0, 2, False, False)
        self.assertNotIn(0, float_range)
        self.assertIn(0.1, float_range)
        self.assertIn(1, float_range)
        self.assertNotIn(2, float_range)

    def test_contains_float_range_inverted(self):
        float_range = Range(2, 0)
        self.assertNotIn(-1, float_range)
        self.assertIn(0, float_range)
        self.assertIn(1, float_range)
        self.assertIn(2, float_range)
        self.assertNotIn(3, float_range)

    def test_contains_float_range_negative(self):
        float_range = Range(-5, -2)
        self.assertNotIn(-6, float_range)
        self.assertIn(-3, float_range)
        self.assertIn(-2, float_range)
        self.assertNotIn(-1, float_range)

    def test_contains_float_range_over_zero(self):
        float_range = Range(-5, 5)
        self.assertNotIn(-6, float_range)
        self.assertIn(-5, float_range)
        self.assertIn(0, float_range)
        self.assertIn(5, float_range)
        self.assertNotIn(6, float_range)

    def test_contains_float_infinity(self):
        float_range = Range(-math.inf, 5)
        self.assertIn(-math.inf, float_range)
        self.assertIn(-10000, float_range)
        self.assertIn(-6, float_range)
        self.assertIn(-5, float_range)
        self.assertIn(0, float_range)
        self.assertIn(5, float_range)
        self.assertNotIn(6, float_range)
