import datetime
import time
class NowyTelefon(object):
    def __init__(self, cechy_telefonu):
        self.nazwa = cechy_telefonu['nazwa']
        self.model = cechy_telefonu['model']
        self.cena = cechy_telefonu['cena']
        self.data_produkcji = datetime.datetime.now()
    def pokaz(self, x):
        return self.nazwa[x], self.model[x], self.cena[x]
    def inflacja(self, x):
        nowa_cena = self.cena[x] + 100
        return nowa_cena
    def data_produkcji(self):
        print("Rozpoczynam produkcje...")
        self.start = datetime.datetime.now()
        time.sleep(10)
        self.czas_produkcji = datetime.datetime.now() - self.start
        return self.czas_produkcji


moje_potrzeby = {
    'nazwa': ['Samsung', 'Nokia', 'Motorola'],
    'model':['Galaxy S9 Plus', 'GTX300', 'CoolKids'],
    'cena':[1999, 1599, 1190]
}
moj_nowy_telefon = NowyTelefon(moje_potrzeby)
print("Czas produkcji: ", moj_nowy_telefon.data_produkcji())

#print(moj_nowy_telefon.pokaz(1))
#print(moj_nowy_telefon.inflacja(0))

