import pytest
from PYTwro13.d4_29_08_2021.zadanie_4 import compute_average


@pytest.mark.parametrize("x, y, result", [
    ("Ania", {"math": 5, "biology": 5, "polish": 4, "physics": 1, "history": 5}, "Student Ania, grade avg: 4.0"),
    ("Basia", {"math": 5}, "Student Basia, grade avg: 5.0"),
    ("Krysia", {"physics": 1, "history": 5}, "Student Krysia, grade avg: 3.0"),

])
def test_compute_avarage(x, y, result):
    assert compute_average(x, **y) == result
