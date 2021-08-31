'''
Zadanie 7
Czujniki pogodowe zwracają listę krotek w postaci: [("Miejscowosc_1", "pomiar", wartość),
("Miejscowosc", "pomiar", wartość)...]
np. [("Bydgoszcz", "Temperatura", 30), ("Bydgoszcz", "Wilgotnosc", "60%")]
Przygotuj dane testowe.
Zagreguj dane z kilku czujników pogodowych do listy i użyj metody chain z modułu itertools aby
wypisać wszystkie pomiary
'''
from itertools import chain
czujniki = [
    ("Wrocław", "pomiar", 11),
    ("Warszawa", "pomiar", 13),
    ("Kraków", "pomiar", 10),
    ("Szczecin", "pomiar", 8),
]
for test in chain(*czujniki):
    print(test)
