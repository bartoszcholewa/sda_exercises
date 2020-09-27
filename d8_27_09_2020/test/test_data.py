import pytest
from ..src.data import Data
from unittest import TestCase

# @pytest.fixture()
# def my_fixture(): #przygotowanie testu
#     print("Przed testem")
#     yield #placeholder testu
#     print("Po tescie")
#
# def test_fixutre(my_fixture):
#     print("W trakcie testu")
#     assert 1 == 0

# FIXTURE wykonuje tylko przed testem, a nie przed assertem
# flaga ktora pomija najblisza funkcje, i wykonuje ja przy wywolaniu
# @pytest.fixture()
# def prepare_objects():
#     data = Data()
#     data.prepare("Marek", "lekarz")
#     yield data
#     #data.prepare(None, None)
#
# def test_data_first(prepare_objects):
#     assert prepare_objects.name == "Marek"
#     prepare_objects.prepare("Marek", "Test")
#     assert prepare_objects.info == "Test"
#
# def test_data_second():
#     assert prepare_objects.info == "Test"

# FIXTURA GLOBALNA ==========================

class TestData(TestCase): #dziedziczenie po module TestCase
    # TestCase zawsze sie wykonuje, ale ma puste setUp i tearDown.
    # Dodajemy do tych metod funkcjonalnosc ktora nas interesuje, aby wykonywaly sie
    # dla wszystkich testow (globalnie)
    def setUp(self):
        self.data = Data()
        self.data.prepare("Marek", "lekarz")

    def test_data_first(self):
        assert self.data.name == "Marek"
        self.data.prepare("Marek", "Test")
        assert self.data.info == "Test"

    def test_data_second(self):
        assert self.data.info == "lekarz"

    def tearDown(self):
        self.data.prepare(None, None)


