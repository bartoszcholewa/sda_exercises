import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
from unittest.mock import patch, MagicMock
from src.api import API, get_only_numbers


def test_read_only_numbers():

    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  mockowanie metody get_data
    with patch('src.api.API', fake_api):
        # patch podmienia obiekt oryginalny a context manager określa zakres używania mocka
        result = get_only_numbers()
        assert result == expected