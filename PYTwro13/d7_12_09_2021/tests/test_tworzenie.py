from PYTwro13.d7_12_09_2021.tworzenie import create_dir
from unittest import mock


@mock.patch("os.mkdir")
def test_istnieje(mkdir_mock):
    dir_name = "tworzenie_dir"
    mkdir_mock: mock.MagicMock
    mkdir_mock.return_value = True
    assert create_dir(dir_name) == "success"
    mkdir_mock.side_effect = OSError("Katalog instnieje")
    assert create_dir(dir_name) is None

