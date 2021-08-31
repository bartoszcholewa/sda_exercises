import pytest
from PYTwro13.d4_29_08_2021.zadanie_3 import sum_all, sum_all_2


class TestSumFunctions:
    @pytest.mark.parametrize("x, result", [
        ((1,), 1), ((1, 5, 35, 3.32, 1.42), 45.74)
    ])
    def test_add_numbers(self, x, result):
        assert sum_all(*x) == result

    @pytest.mark.parametrize("x, result", [
        ((1,), 1), ((1, 5, 35, 3.32, 1.42), 45.74)
    ])
    def test_add_numbers_2(self, x, result):
        assert sum_all_2(*x) == result
