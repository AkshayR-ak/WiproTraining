import sys
import unittest

from src.calculations import add, sub, mul, div, equal

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(15, res, msg='Addition Error')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5,res, msg='Subtraction Error')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50, res, msg='Multiplication Error')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2, res, msg='Division Error')

    def test_div(self):
        res = div(10, 5)
        self.assertRaises(ZeroDivisionError, msg='No Exception')

    @unittest.skipIf(condition=sys.version_info < (3, 13),reason='Not implemented yet' )
    def test_equal(self):
        res = equal(10, 10)
        self.assertTrue(res, msg='Equal error')