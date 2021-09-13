"""
Test for calculator
"""
from PYTwro13.d7_12_09_2021.calculator import dodawanie, odejmowanie, mnozenie, dzielenie


def test_dodawanie():
    """ Test for calculator function 'dodawanie' """
    assert dodawanie(4, 5) == 9
    assert dodawanie(3, 2) == 5
    assert dodawanie(5, 5) == 10


def test_odejmowanie():
    """ Test for calculator function 'odejmowanie' """
    assert odejmowanie(5, 5) == 0
    assert odejmowanie(19, 9) == 10
    assert odejmowanie(0, 5) == -5
    assert odejmowanie(10, 2) == 8


def test_mnozenie():
    """ Test for calculator function 'mnozenie' """
    assert mnozenie(5, 5) == 25
    assert mnozenie(1, 1) == 1
    assert mnozenie(3, 3) == 9
    assert mnozenie(10, -1) == -10
    assert mnozenie(23, 0) == 0


def test_dzielenie():
    """ Test for calculator function 'dzielenie' """
    assert dzielenie(10, 2) == 5
    assert dzielenie(9, 3) == 3
    assert dzielenie(10, 1) == 10
    assert dzielenie(100, 100) == 1
