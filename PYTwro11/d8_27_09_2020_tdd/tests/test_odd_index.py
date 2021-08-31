from PYTwro11.d8_27_09_2020_tdd.odd_index import odd_indexes

def test_odd_index_string():
    assert odd_indexes("Komputer") == "optr"

def test_odd_index_string2():
    assert odd_indexes("teleturniej") == "eeune"

def test_odd_index_string3():
    assert odd_indexes(12345678) == "2468"
