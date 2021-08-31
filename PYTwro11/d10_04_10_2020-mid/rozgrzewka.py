"""
1. Napisz klasę: Employee, która przechowuje 4 zmienne:
    name
    surname
    is_staff - domyślnie False
equipment - który jest listą sprzętu - domyślnie None (lub [])
"""
from dataclasses import dataclass


@dataclass
class Employee:
    """ This is a docstring for @dataclass """
    name: str
    surname: str
    is_staff: bool = False
    equipment: list = None

    # def __init__(self, name, surname, is_staff=False, equipment=None):
    #     self.name = name
    #     self.surname = surname
    #     self.is_staff = is_staff
    #     self.equipment = equipment
    """
    2. Napiszmy metodę tej klasy, która jest generatorem i zwraca po kolei elementy z listy sprzętu
    pod warunkiem, że is_staff=True.
    Jeśli is_staff=False, niech generator zwróci stosowny komunikat
    3. Utwórzmy zmienną w pliku (poza klasą). Zmieńmy nasz generator z zadania 2 tak, aby przy
    każdym generowaniu pojedynczego sprzętu dodawał imię i nazwisko osoby do listy
    (wartości słownika COMPANY_EQUIPMENT), jeśli nazwa danego sprzętu odpowiada tej w słowni.
    """

    def generator(self):
        """ This is a docstring for generator method """
        for item in self.equipment:
            if self.is_staff:
                if item in COMPANY_EQUIPMENT.keys():
                    COMPANY_EQUIPMENT[item].append(f"{self.name} {self.surname}")
                yield item
            else:
                yield "Pracownik zwolniony"


COMPANY_EQUIPMENT = {'PC': [],
                     'monitor': [],
                     'keyboard': [],
                     'docking station': [],
                     }

employee0 = Employee(name="Bartosz",
                     surname="Cholewa",
                     is_staff=True,
                     equipment=['PC',
                                'monitor',
                                'keyboard',
                                'docking station'])

gen0 = employee0.generator()
for i in gen0:
    print(i)
print(COMPANY_EQUIPMENT)
