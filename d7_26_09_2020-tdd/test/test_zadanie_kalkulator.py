import pytest
from ..src.zadanie_kalkulator import ZadanieKalkulator

class TestZadanieKalkulator():

    @pytest.fixture()
    def return_kalkulator(self):
        return ZadanieKalkulator(4,5)

    @pytest.fixture()
    def return_kalkulator2(self):
        return ZadanieKalkulator(6,7)

    def test_dodaj(self, return_kalkulator, return_kalkulator2):
        assert return_kalkulator.dodaj() == 9
        assert return_kalkulator2.dodaj() == 13

    def test_odejmij(selfs, return_kalkulator, return_kalkulator2):
        assert return_kalkulator.odejmij(True) == 1
        assert return_kalkulator2.odejmij() == -1