import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..',))
import pytest
from unittest.mock import patch, MagicMock
from src.mock import User

def test_return_available_funds():
    fake_account1 = MagicMock()
    fake_account1.get_balance.return_value = 50
    fake_account2 = MagicMock()
    fake_account2.get_balance.return_value = 40
    user = User("Kowalski", 35, [fake_account1, fake_account2])
    assert user.return_available_funds() == 90
