import unittest

from ..src.Math import add

class TestMath(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(5, result,msg='Addition Error')
