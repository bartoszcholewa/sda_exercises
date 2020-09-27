import pytest
import random
from ..src.kalkulator import add_numbers

class TestCalculator():
    def test_add_numbers(self):
        assert add_numbers(4, 7) == 11

    def test_add_numbers_with_negative(self):
        assert add_numbers(-2, -7) == -9

    def test_add_numbers_string(self):
        with pytest.raises(Exception):
            assert add_numbers('ala', 2)

    @pytest.mark.skip(reason="Wymaga bilbioteki w wersji")
    def test_add_numbers_float(self):
        assert add_numbers(3.4, 2.1) == 5.5

    #@pytest.fixture() - fikstura ktora wykonuje sie w raz z kazdym testem
    @pytest.fixture()
    def return_number(self):
        yield random.randint(10,100)
        print("Liczba jest za duza!")

    def test_add_numbers_random(self, return_number):
        assert add_numbers(return_number, 20) < 121

    @pytest.mark.parametrize("a, b, result", [(2, 4, 6), (-1, -3, -4)])
    def test_add_numbers_all(self, a, b, result):
        assert add_numbers(a, b) == result