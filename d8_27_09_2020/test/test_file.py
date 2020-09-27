import pytest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
from unittest.mock import patch, MagicMock
from src.file import get_avg, get_data

print(os.path.dirname(__file__))
def test_get_avg():
    fake_file = MagicMock(return_value="987654321")
    with patch('src.file.get_data', fake_file):
        assert get_avg(3) == 5.0