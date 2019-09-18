import unittest

from py_range_parse import Range


class ComparisonTest(unittest.TestCase):

    def test_lt_int_range(self):
        int_range = Range(0, 5)
        self.assertTrue(-1 < int_range)
        self.assertFalse(0 < int_range)
        self.assertFalse(2 < int_range)
        self.assertFalse(5 < int_range)
        self.assertFalse(6 < int_range)

    def test_lt_float_range(self):
        float_range = Range(0, 5.2)
        self.assertTrue(-1 < float_range)
        self.assertFalse(0 < float_range)
        self.assertFalse(2 < float_range)
        self.assertFalse(5.2 < float_range)
        self.assertFalse(6 < float_range)

    def test_gt_int_range(self):
        int_range = Range(0, 5)
        self.assertFalse(-1 > int_range)
        self.assertFalse(0 > int_range)
        self.assertFalse(2 > int_range)
        self.assertFalse(5 > int_range)
        self.assertTrue(6 > int_range)

    def test_gt_float_range(self):
        float_range = Range(0, 5.2)
        self.assertFalse(-1 > float_range)
        self.assertFalse(0 > float_range)
        self.assertFalse(2 > float_range)
        self.assertFalse(5.2 > float_range)
        self.assertTrue(6 > float_range)
