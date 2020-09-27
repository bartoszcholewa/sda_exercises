#die klasy
#pierwsza klasa produkt
# var nazwa, objetosc

#druga klasa magazyn
# var objetosc, lista produktow

# def dodaj (produkt)
# prawdz czy jest miejsce,(metoda), jesli jest, dodaj do listy produktow, zwroc pozostala ilosc wolnego miesjca
# a jesli nie ma, zwroc -1

# def spawdz_czy_jest_miejsce

#stworzenie testow
class Produkt(object):
    def __init__(self, nazwa, objetosc):
        self.nazwa = nazwa
        self.objetosc = objetosc

class Magazyn(object):
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.produkty = list()
    def add(self, produkty):
        if isinstance(produkty, list):
            for produkt in produkty:
                if produkt.objetosc > self.pojemnosc:
                    return -1
                else:
                    self.produkty.append(produkt)
                    self.pojemnosc -= produkt.objetosc
        else:
            if produkty.objetosc > self.pojemnosc:
                return -1
            else:
                self.produkty.append(produkty)
                self.pojemnosc -= produkty.objetosc
        return self.pojemnosc
    def podaj_zawartosc(self):
        ret = dict()
        for produkt in self.produkty:
            ret[produkt.nazwa] = produkt.objetosc
        return ret

# produkt1 = Produkt("Koty", 156.3)
# produkt2 = Produkt("Psy", 133.7)
# produkt3 = Produkt("Szczury", 78.4)
# schronisko = Magazyn(3000.0)
# schronisko.add(produkt1)
# schronisko.add([produkt2, produkt3])
# print(f"Pojemnosc: {schronisko.pojemnosc}")
# print(f"Zawartosc z waga: {schronisko.podaj_zawartosc()}")



