import pytest
from src.sum_args import sum_arguments, capital_case

class TestSumArgs():
    def test_sum_below_max(self):
        assert sum_arguments(10, [2,4,5,6,7,8]) == 32

    def test_sum_above_max(self):
        assert sum_arguments(5, [2, 3, 4, 5, 6, 7, 8]) == 9

    def test_sum_with_string_elem(self):
        assert sum_arguments(10, [2, 4, 5, 6, 7, 8, "cos"]) == 32

    def test_sum_with_string_max(self):
        assert sum_arguments("costam", [2, 4, 5, 6, 7, 8]) == 32

    def test_sum_with_string_elem_and_max(selfs):
        assert sum_arguments("cos", [2, 4, 5, 6, 7, 8, "test"]) == 32

    def test_capitalize_1(selfs):
        assert capital_case('ala') == "Ala"

    def test_capitalize_2(selfs):
        assert capital_case('babcia') == "Babcia"

    def test_capitalize_exception(self):
        with pytest.raises(TypeError):
            capital_case(2432423235234)