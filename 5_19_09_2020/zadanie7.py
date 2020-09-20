class Klasa1(object):
    def __init__(self, list):
        self.lista_uczniow = list
    def __len__(self):
        return len(self.lista_uczniow)
    def __str__(self):
        return str(self.lista_uczniow)
    def __add__(self, other):
        return self.lista_uczniow + other.lista_uczniow
    def __sub__(self, other):
        return [item for item in self.lista_uczniow if item not in other.lista_uczniow]
    def __getitem__(self, item):
        return self.lista_uczniow[item]

moja_klasa = Klasa1(['Ania', 'Kasia', 'Michal', 'Kamil', 'Zosia', 'Jas'])
moja_klasa2 = Klasa1(['Andrzej', 'Basia', 'Kasia', 'Maksymilian'])
print(len(moja_klasa))
print(str(moja_klasa))
print(moja_klasa + moja_klasa2)
print(moja_klasa - moja_klasa2)
print(moja_klasa[1])