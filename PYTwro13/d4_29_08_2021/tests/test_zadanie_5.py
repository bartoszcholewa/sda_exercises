import pytest
from PYTwro13.d4_29_08_2021.zadanie_5 import compute_average_elastic


@pytest.mark.parametrize("student, args, kwargs, result", [
    ("Ania", (1, 5), {"math": 5, "biology": 5, "polish": 4}, "Student Ania, grade avg: 4.0"),
    ("Basia", (5, 4, 3), {}, "Student Basia, grade avg: 4.0"),
    ("Krysia", (1,), {"biology": 5, "polish": 4}, "Student Krysia, grade avg: 3.3333333333333335"),
])
def test_compute_avarage_elastic(student, args, kwargs, result):
    assert compute_average_elastic(student, *args, **kwargs) == result
