'''
Zadanie 2:
Utwórz i uzupełnij moduł parcels.py zgodnie z wymaganiami:

Zadanie 3.
W pliku parcels.py zdefiniuj namedtuple o nazwie Parcel i polach destination, send_time, size,
serial_number. Zwracaj typ Parcel zamiast poprzednio przygotowanej krotki.

Zadanie 6.
Zmodyfikuj kod pliku parcels.py, by zamiast krotki zawierał dataclass Parcel ze wszystkimi do tej
pory potrzebnymi parametrami (destination, send_time, size, serial_number, sender_name,
sender_origin).
Parametrom, których nie ustawia bezpośrednio generator (sender_name, sender_origin) przypisz
wartości domyślne None.
Zmodyfikuj plik sender.py, by aktualizował pola sender_name i sender_origin każdej utworzonej
paczki.
'''
import random
import datetime
from collections import namedtuple
from dataclasses import dataclass
destinations = ("Gdansk", "Gdynia", "Sopot")
sizes = ("A", "B", "C")
@dataclass
class Parcel:
    destination: str
    send_time: str
    size: str
    serial_number: int
    sender_name: str = None
    sender_origin: str = None

def __parcel_generator():
    serial = 0
    while True:
        date = datetime.date.today() + datetime.timedelta(days=random.randint(-100, 100))
        yield Parcel(destination=random.choice(destinations),
                     send_time=str(date),
                     size=random.choice(sizes),
                     serial_number=serial)
        serial += 1

parcel_generator = __parcel_generator()
if __name__ == "__main__":

    for _ in range(10):
        print(next(parcel_generator))

    a = next(parcel_generator)
    print(a.destination)
