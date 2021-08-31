from unittest.mock import patch, MagicMock
from PYTwro11.d8_27_09_2020_tdd.api import API, get_only_numbers


def test_read_only_numbers():

    test_data = ["1,4,5,25,aa,bb,23,4", "324,24,234www,1,23", "545,3w,32"]

    expected = "1|4|5|25|23|4|324|24|1|23|545|32"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data #  mockowanie metody get_data
    with patch('PYTwro11.d8_27_09_2020_tdd.api.API', fake_api):
        # patch podmienia obiekt oryginalny a context manager określa zakres używania mocka
        result = get_only_numbers()
        assert result == expected