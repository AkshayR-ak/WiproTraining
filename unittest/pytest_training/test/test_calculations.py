import pytest

from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    @pytest.mark.parametrize("n1, n2, expval",[(10, 5, 15), (10, 15, 25), (-10, 5, -5), (10, 7, 17)])

    def test_add(self, n1, n2, expval):
        result = self.calc.add(n1, n2)
        assert result == expval, 'Addition Error'

    @pytest.mark.parametrize("n1, n2, expval", [(10, 5, 5), (10, 15, -5), (-10, 5, -15), (10, 7, 3)])

    def test_sub(self, n1, n2, expval):
        result = self.calc.sub(n1, n2)
        assert result == expval, 'Subtraction Error'

    def test_mul(self):
        result = self.calc.mul(10,5)
        assert result == 50, 'Multiplication Error'

    def test_div(self):
        result = self.calc.div(10, 5)
        assert result == 2, 'Division Error'

    @pytest.mark.skip(reason='NA')
    def test_equal(self):
        result = self.calc.equal(10, 10)
        assert result == True, 'NE'

    @pytest.mark.xfail(reason='Exception not handled')
    def test_driver(self):
       # with pytest.raises(ZeroDivisionError):
            result = self.calc.div(10, 0)
            assert result == 0
