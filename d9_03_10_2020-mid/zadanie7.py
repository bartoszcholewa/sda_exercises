'''
Zadanie 7.
Przygotuj funkcję wypisującą dane skazańca wg schematu:
Imię Nazwisko
Czy jest aresztowany? (domyślnie True)
Cecha: wartość
Cecha: wartość
Cecha: wartość
(dowolna ilość nazwanych cech)
'''

slownik = {"Wiek": 23,
           "Wzrost": 181,
           "Oczy" : "Zielone2"}

def skazaniec(imie, nazwisko, aresztowany=True, **kwargs):
    print(f"Imie i nazwisko: {imie} {nazwisko}")
    print(f"Czy skazaniec aresztowany? {'Tak' if aresztowany else 'Nie'}")
    for value in kwargs.items():
        print(*value)

    # return True if True else False

skazaniec(imie="Bartosz", nazwisko="Cholewa", **slownik)
