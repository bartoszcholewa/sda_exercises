""" Test for my classes """
from PYTwro13.d7_12_09_2021.little_class import LittleClass


def test_my_class_init():
    a = LittleClass(name='bartosz')
    assert isinstance(a, LittleClass)
    assert a._name == 'bartosz'
    a._name = 'michal'
    assert a._name == 'michal'


def test_my_class_upper():
    a = LittleClass(name='bartosz')
    assert hasattr(a, 'big_name')
    assert a.big_name() == 'BARTOSZ'

def test_my_class_argument_type():
    a = LittleClass(name='bartosz')
    assert isinstance(a._name, str)