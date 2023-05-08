import pytest


class Test_a():
    def test_1(self):
        a = 10
        b = 20
        c = a+ b
        if c == 30:
            assert True
        else:
            assert False

    def test_2(self):
        a = 10
        b = 20
        c = a * b
        if c == 30:
            assert False
        else:
            assert True

    @pytest.mark.xfail
    def test_3(self):
        a = 100
        b = 20
        c = a - b
        if c == 80:
            assert True
        else:
            assert False
