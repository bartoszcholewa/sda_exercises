import pytest
from PYTwro11.d8_27_09_2020_tdd.func import func

@pytest.mark.parametrize("number, result", [(12, 2), (11, 2), (2, 4),
                                            (123, 26), (92, 18), (79, 14),
                                            (19023, 206)])
def test_func(number, result):
    assert func(number) == result