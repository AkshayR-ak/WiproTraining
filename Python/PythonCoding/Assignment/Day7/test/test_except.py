import pytest

from src.zero import Zero

class TestExcept:
    ex = Zero()

    def test_div(self):
        with pytest.raises(ZeroDivisionError):
            self.ex.div()

