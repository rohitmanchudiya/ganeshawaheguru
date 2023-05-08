import pytest


class Test_c():
        def test_c1(self):
            a = 1000
            b = 20
            c = a - b
            if c == 980:
                assert True
            else:
                assert False

        @pytest.mark.skip
        def test_c2(self):
            a = 1000
            b = 20
            c = a - b
            if c == 980:
                assert True
            else:
                assert False