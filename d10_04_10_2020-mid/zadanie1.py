'''
1. Napisz klasę: Employee, która przechowuje 4 zmienne:
	name
	surname
	is_staff - domyslnie False
	equipment - który jest listą sprzętu - domyslnie None (lub [])
2. Napiszmy metodę tej klasy, która jest generatorem i zwraca po kolei elementy z listy sprzętu pod warunkiem, że is_staff=True.
Jesli is_staff=False, niech generator zwróci stosowny komunikat
3. Utwórzmy zmienną w pliku (poza klasą):
COMPANY_EQUIPMENT = {
	'PC': [],
	'monitor': [],
	'keyboard': [],
	'docking station': [],
}
Zmieńmy nasz generator z zadania 2 tak, aby przy każdym generowaniu pojedynczego sprzętu dodawał imię i nazwisko osoby do listy (wartości słownika COMPANY_EQUIPMENT), jeśli nazwa danego sprzętu odpowiada tej w słowni
'''
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    surname: str
    is_staff: bool = False
    equipment: list = None


    def __init__(self, name, surname, is_staff=False, equipment=None):
        self.name = name
        self.surname = surname
        self.is_staff = is_staff
        self.equipment = equipment

    def generator(self):
        for item in self.equipment:
            if self.is_staff:
                if item in COMPANY_EQUIPMENT.keys():
                    COMPANY_EQUIPMENT[item].append(f"{self.name} {self.surname}")
                yield item
            else:
                yield "Pracownik zwolniony"

COMPANY_EQUIPMENT = {'PC' :[],
                     'monitor': [],
                     'keyboard':[],
                     'docking station':[],
                     }
employee0 = Employee(name="Bartosz",
                     surname="Cholewa",
                     is_staff=True,
                     equipment=['PC',
                              'monitor',
                              'keyboard',
                              'docking station'])


# gen0 = employee0.generator()
# for i in gen0:
#     print(i)
# print(COMPANY_EQUIPMENT)

for id in Employee._ids:
    for i in eval(f'gen{id}'):
        print(i)

# employee0.print_name()