'''
Zadanie 5.
Utwórz slownik, tuple, namedtuple oraz dataclass dla obiektu reprezentującego tą samą książkę.
Porównaj obiekty ze sobą za pomocą operatora ==
Wypisz wszystkie obiekty.
'''
from collections import namedtuple
from dataclasses import dataclass
ksiazka_slownik = {"Tytul" : "Wpadlam do studzienki", "Autor" : "Krystyna Krawężnik"}
tuple = "Wpadłam do studzienki", "Krystyna Krawężnik"
Ksiazka = namedtuple("Ksiazka", "Tytul, Autor")
tuple_ksiazka = Ksiazka("Wpadłam do studzienki", "Krystyna Krawężnik")

@dataclass
class Ksiazka:
    tytul: str
    autor: str

class_ksiazka = Ksiazka(tytul="Wpadłam do studzienki", autor="Krystyna Krawężnik")

print(ksiazka_slownik)
print(tuple)
print(tuple_ksiazka)
print(type(class_ksiazka), class_ksiazka.tytul, class_ksiazka.autor)

print(tuple == tuple_ksiazka)

print(tuple_ksiazka.Autor)