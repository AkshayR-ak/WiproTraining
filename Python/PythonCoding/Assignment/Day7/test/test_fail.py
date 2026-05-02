import pytest

from src.fail import Fail


class TestFail:

    isfail = Fail()

    def test_fail(self):
        res = self.isfail.assert_fail('hello')
        assert res == True, 'Intentionally failed'