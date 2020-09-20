class Animal(object):
    def __init__(self, rodzina, gatunek, waga, plec, rok_u=None):
        self.rodzina = rodzina
        self.gatunek = gatunek
        self.plec = plec
        self.waga = waga
        #self.__noga = 2
        if not rok_u:
            self.rok_urodzenia = 'dzisiaj'
    def jedz(self, ile):
        self.waga += ile

class Pies(Animal):
    def __init__(self, rasa, *args):
        Animal.__init__(self, *args)
        self.rasa = rasa
    def daj_glos(self):
        print("Hau Hau!")
    def __str__(self):
        return 'To jest pies'

class Kot(Animal):
    def __init__(self, rasa, *args):
        Animal.__init__(self, *args)
        self.rasa = rasa
        self._noga = 2
    def daj_glos(self):
        print("Miau Miau")

moj_pies = Pies("York", "Psowaty", "Wilczasty", 10, "Pies")
moj_pies.daj_glos()
print(f"Rasa mojego zwierza: {moj_pies.rasa}")
print(f"Rok urodzenia: {moj_pies.rok_urodzenia}")
print(f"Waga przed jedzeniem: {moj_pies.waga}kg")
moj_pies.jedz(10)
print(f"Waga po zjedzeniu 10kg: {moj_pies.waga}kg")

moj_kot = Kot("Syjamski", "Kotowaty", "Tygrysiasty", 5, "Kocica")
moj_kot.daj_glos()
print(f"Rasa mojego zwierza: {moj_kot.rasa}")
print(f"Rok urodzenia: {moj_kot.rok_urodzenia}")
print(f"Waga przed jedzeniem: {moj_kot.waga}kg")
moj_kot.jedz(10)
print(f"Waga po zjedzeniu 10kg: {moj_kot.waga}kg")
print(moj_kot._noga)
print(str(moj_pies))
print(moj_pies)