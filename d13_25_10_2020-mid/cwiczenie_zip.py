"""
Zadanie Zip1
Mając odpowiadające sobie listy:
fruits_prices = [("banana", 3), ("orange", 2), ("apple", 2), ("strawberry", 5)]
fruits_quantity = [("banana", 200), ("orange", 400), ("apple", 200),
("strawberry", 500)]
Za pomocą metody izip w jednej pętli wypisz nazwę owocu, jego cenę oraz posiadaną ilość.
"""
from itertools import groupby

fruits_prices = [("banana", 3), ("orange", 2), ("apple", 2), ("strawberry", 5)]
fruits_quantity = [("banana", 200), ("orange", 400), ("apple", 200),
("strawberry", 500)]

for a, b in (zip(fruits_prices, fruits_quantity)):
    print(a[0], a[1], b[1])