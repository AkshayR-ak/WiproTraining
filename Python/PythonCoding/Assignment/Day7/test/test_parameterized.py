import pytest

from src.parameterized import Parameterized


class TestParameterized:

    para = Parameterized()

    @pytest.mark.parametrize("x, expval", [(10, 100)])
    def test_parameterized(self, x, expval):
        res = self.para.square(x)
        assert res == expval, 'Square Error'