import random
"""
    Generator liczb naturalnych.
    Funkcje użytkowe.
"""


def generate_number_between(min:int, max:int) -> int:
    """Losuje liczbę z przedziału <min, max>.

    :param min:
    :param max:
    :return:
    """
    print("Udaje, ze losuje, zwracam zawsze to samo")

    return random.randint(min, max)


def generate_until_drawn(number:int, min:int, max:int) -> int:
    """Losuje liczbę z przedzialu <min, max> tak dlugo az wylosuje liczbe number.

    :param number:
    :param min:
    :param max:
    :return: ilosc potrzebnych losowan do ostatecznego wylosowania liczby number.
    """
    print("Udaje, ze losuje w petli, a zwracam zawsze to samo")
    i = 0
    while not random.randint(min, max) == number:
        i += 1
    return i
