import pytest
from ..src.fizzbuzz import fizz_buzz

@pytest.mark.parametrize("x, result", [(0, 0), (1,1), (-3,0),
                                       (15, "FizzBuzz"), (45, "FizzBuzz"),
                                       (9, "Fizz"), (27, "Fizz"), (25, "Buzz"),
                                       (55, "Buzz"), (100, "Buzz"), (101,0), (3,"Fizz")])
def test_fizz_buzz_one(x, result):
    assert fizz_buzz(x) == result
