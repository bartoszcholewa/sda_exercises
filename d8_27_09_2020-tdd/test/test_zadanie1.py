import pytest
from d8_27_09_2020.src.zadanie1 import Product, Warehouse, ProductError

#TODO:
# -check if volume is negative,
# -check isinstance(x, numbers.Number)


def test_product_have_str_name():
    test_product = Product("Rabbits", 45.55)
    assert test_product.name == "Rabbits"


def test_product_have_float_volume():
    test_product = Product("Rabbits", 45.55)
    assert test_product.volume == 45.55

def test_product_have_int_name():
    test_product = Product(12345, 45.55)
    assert test_product.name == "12345"

def test_product_have_float_name():
    test_product = Product(123.45, 45.55)
    assert test_product.name == "123.45"

def test_product_have_int_volume():
    test_product = Product("Rabbit", 45)
    assert type(test_product.volume) == float
    assert test_product.volume == 45.00

def test_product_have_numeric_str_volume():
    test_product = Product("Rabbit", "45.55")
    assert test_product.volume == 45.55
    assert type(test_product.volume) == float

def test_product_have_nonnumeric_str_volume():
    with pytest.raises(ProductError):
        test_product = Product("Rabbit", "asb--!")



@pytest.fixture()
def products():
    return [Product("Cats", 26.33),
            Product("Dogs", 33.22),
            Product("Rats", 55.87)]


@pytest.mark.parametrize("capacity, results", [(100, -1), (150, 34.58), (200.50, 85.08)])
def test_warehouse_add_one_product_at_a_time(capacity, results, products):
    test_warehouse = Warehouse(capacity)
    last_result = None
    for product in products:
        last_result = test_warehouse.add(product)
    assert round(last_result, 2) == results


@pytest.mark.parametrize("capacity, results", [(100, -1), (150, 34.58), (200.43, 85.01)])
def test_warehouse_add_products_list(capacity, results, products):
    test_warehouse = Warehouse(capacity)
    last_result = test_warehouse.add(products)
    assert round(last_result, 2) == results

# def test_wrong_product_arguments():
