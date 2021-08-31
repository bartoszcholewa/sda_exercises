"""
SDA - PYTwro11 - blok Testowanie oprogramowania i TDD - Mateusz Z.
Dzień 8 - 27-09-2020r
Zadanie 1:
Utwórz dwie klasy. Pierwsza klasa o nazwie 'Produkt', przyjmująca za argument 'nazwa (str)' i 'objętość (float)'.
Druga klasa o nazwie 'Magazyn', przyjmująca za argument 'pojemność (float)'.
Klasa 'Magazyn' ma posiadać metodę 'dodaj' która przyjmuje za argument obiekt 'Produkt' lub ich listę.
Podczas dodawania produktu do magazynu, magazyn musi sprawdzić czy jest miejsce danego produktu lub listy produktów
w magazynie. Jeśli jest, ma dodać każdą która się zmieści. Po zakończeniu dodawania, ma zwrócić aktualną pojemność
magazynu. Jeśli miejsca nie ma, lub się skończyło podczas dodawania produktów, magazyn ma zwrócić wartość -1.
Dodatkowo:
Klasa magazyn ma posiadać możliwość wywołania jej aktualnej pojemności i zawierających w sobie produktów wraz z ich
objętością.
"""
class ProductError(Exception):
    """An exception class for product"""


class Product(object):
    def __init__(self, name: str, volume: float):
        try:
            self.name = str(name)
            self.volume = float(volume)
        except ValueError:
            raise ProductError("Niepoprawne dane produktu")



class Warehouse(object):
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.products = list()

    def __place_to_warehouse(self, product: object):
        self.products.append(product)
        self.capacity -= product.volume

    def add(self, products: object) -> float:
        if isinstance(products, list):
            for product in products:
                if product.volume > self.capacity:
                    return -1
                else:
                    self.__place_to_warehouse(product)
        else:
            if products.volume > self.capacity:
                return -1
            else:
                self.__place_to_warehouse(products)
        return self.capacity

    def check_content(self) -> dict:
        ret = dict()
        for product in self.products:
            ret[product.name] = product.volume
        return ret

#
# product1 = Product("Cats", 156.3)
# product2 = Product("Dogs", 133.7)
# product3 = Product("Rats", 74.4)
# pet_shop = Warehouse(3000.0)
# pet_shop.add(product1)
# pet_shop.add([product2, product3])
# print(pet_shop.capacity, pet_shop.check_content())
