from PYTwro13.d7_12_09_2021.odwrotnie import OdwrotnieClass


def test_init():
    """ Test should create instance"""
    a = OdwrotnieClass(name='bartosz')
    assert a._name == 'bartosz'
    assert isinstance(a._name, str)


def test_reverse():
    """ Test should reverse object name """
    a = OdwrotnieClass(name='bartosz')
    assert a.reverse() == 'zsotrab'
