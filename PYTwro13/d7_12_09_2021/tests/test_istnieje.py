from PYTwro13.d7_12_09_2021.istnieje import istnieje
from unittest import mock


@mock.patch("os.path.exists")
def test_istnieje(exist_mock):
    exist_mock: mock.MagicMock
    exist_mock.return_value = True
    assert istnieje("") == 50

    exist_mock.return_value = False
    assert istnieje("") == 200

