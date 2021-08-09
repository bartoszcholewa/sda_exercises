from collections import namedtuple
from math import sqrt

A = namedtuple('jestemtypem', ['pole1', 'pole2'])
i = A('abc', 'efd')

# print(type(i), i)
# print(i.pole1, i.pole2)


products = [
    ['maslo', '3.39', '2'],
    ['koc', '25', '3'],
]


def laczny_koszt(products: list):

    Product = namedtuple('Product', ['nazwa', 'netto', 'podatek'])
    cena = 0
    for product in products:
        produkt = Product(*product)
        print(produkt)
        cena += float(produkt.netto) + float(produkt.podatek)
    print(f'Łączny koszt: {cena}')


# laczny_koszt(products)
# print('\n')


def laczny_koszt2(products: list):
    """ Bez nametuple """
    cena = 0
    for product in products:
        print(product)
        cena += float(product[1]) + float(product[2])
    print(f'Łączny koszt: {cena}')


# laczny_koszt2(products)
# print('\n')

def dlugosc_odcinka(pt1, pt2):
    Point = namedtuple('Point', ['x', 'y'])
    a = Point(*pt1)
    b = Point(*pt2)
    dlugosc = sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
    print(f'Długość odcinka: {round(dlugosc, 2)}')

dlugosc_odcinka((1.0, 5.0), (2.5, 1.5))

# def dlugosc_odcinka(pt1, pt2):
#     Point = namedtuple('Point', ['x', 'y', 's'])
#     a = Point(*pt1, lambda x,y: (x-y)**2)
#     b = Point(*pt2, lambda x,y: (x-y)**2)
#     print(b.s)
#     dlugosc = sqrt(b.s(a.x,b.x) + (a.y - b.y)**2)
#     print(f'Długość odcinka: {dlugosc}')