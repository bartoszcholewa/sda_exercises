from PYTwro13.d7_12_09_2021.fun import fun
from unittest import mock


@mock.patch("os.path.exists")
def test_fun(exists_mock):
    exists_mock: mock.MagicMock
    exists_mock.return_value = True
    assert fun() is None

    exists_mock.side_effect = NameError("NameError")
    assert fun() == "A"

    exists_mock.side_effect = ValueError("ValueError")
    assert fun() == "B"

    exists_mock.side_effect = KeyError("KeyError")
    assert fun() == "C"

    exists_mock.side_effect = IndexError("IndexError")
    assert fun() == "D"
