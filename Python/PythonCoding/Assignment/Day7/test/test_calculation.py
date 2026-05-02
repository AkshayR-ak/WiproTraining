import pytest

from src.calculation import Calculation

class TestSum:

    calc = Calculation()

    def test_sum(self):
        res = self.calc.sum(5, 3)
        assert res == 8, 'Sum Error'