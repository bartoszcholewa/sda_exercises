import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
import pytest
from unittest.mock import patch, MagicMock
from src.zadanie1 import Produkt, Magazyn

@pytest.fixture()
def products():
    return [Produkt("Koty", 26.33), Produkt("Psy", 33.22), Produkt("Szczury", 55.87)]

@pytest.mark.parametrize("capacity, results", [(100,-1), (150, 34.58), (200.50, 85.08)])
def test_magazyn(capacity, results, products):
    m = Magazyn(capacity)
    last_result = None
    for product in products:
        last_result = m.add(product)
    assert round(last_result, 2) == results
