from PYTwro13.d7_12_09_2021.kid import Kid
from unittest import mock


def test_init():
    """ Test for class Kid initializator """
    name = ('Bartosz', 'Cholewa')
    kid_1 = Kid(first_name=name[0], second_name=name[1])
    assert isinstance(kid_1, Kid)

    """
    Check for object private arguments:
    print(dir(kid_1))
    assert False
    >>> ['_Kid__first_name', '_Kid__second_name', '__class__', ...]
    assert kid_1._Kid__first_name == name[0]
    assert kid_1._Kid__second_name == name[1]
    """

    assert getattr(kid_1, '_Kid__first_name') == name[0]
    assert getattr(kid_1, '_Kid__second_name') == name[1]
    assert getattr(kid_1, '_marks') == []


def test_str():
    """ Test for object string representation """
    name = ('Bartosz', 'Cholewa')
    kid_1 = Kid(first_name=name[0], second_name=name[1])
    assert str(kid_1) == 'Bartosz Cholewa'


def test_get_mark():
    """ Test for object assinging marks """
    name = ('Bartosz', 'Cholewa')
    kid_1 = Kid(first_name=name[0], second_name=name[1])
    assert kid_1._marks == []
    kid_1.get_mark(5)
    assert kid_1._marks == [5]
    kid_1.get_mark(1)
    assert kid_1._marks == [5, 1]

