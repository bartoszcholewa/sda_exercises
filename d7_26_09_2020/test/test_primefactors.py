from ..src.primefactors import prime_factors

def test_one():
    assert prime_factors(1) == []

def test_two():
    assert prime_factors(2) == [2]

def test_three():
    assert prime_factors(3) == [3]

def test_four():
    assert prime_factors(4) == [2, 2]

def test_six():
    assert prime_factors(6) == [2, 3]

def test_eight():
    assert prime_factors(8) == [2, 2, 2]

def test_fourtyeight():
    assert prime_factors(48) == [2, 2, 2, 2, 3]
