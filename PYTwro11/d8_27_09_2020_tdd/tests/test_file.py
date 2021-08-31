import pytest
from unittest.mock import patch, MagicMock
from PYTwro11.d8_27_09_2020_tdd.file import get_avg, get_data

def test_get_avg():
    fake_file = MagicMock(return_value="987654321")
    with patch('PYTwro11.d8_27_09_2020_tdd.file.get_data', fake_file):
        assert get_avg(3) == 5.0