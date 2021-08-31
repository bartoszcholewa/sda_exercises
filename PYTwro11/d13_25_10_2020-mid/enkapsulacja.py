# Enkapsulacja, gettery i settery
class Computer:
    number = 4
    def __init__(self):
        self.__max_price = 900

    def get_max_price(self):
        return self.__max_price

    def set_max_price(self, price):
        self.__max_price = price

    @property
    def max_price(self):
        return self.__max_price

    @max_price.setter
    def max_price(self, price):
        self.__max_price = price

    @classmethod
    def num_computers(cls):
        print(cls.number)

c = Computer()

# print(c.__max_price) #AttributeError! Czyli ok!
print(c.get_max_price())
c.set_max_price(1200)
print(c.get_max_price())

# @property
print(c.max_price)

# @setter
c.max_price = 1500
print(c.max_price)

# @classmethod
print(c.num_computers())