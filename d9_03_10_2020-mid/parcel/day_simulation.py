from time import sleep
import random
from sender import Sender
from sorting_facility import SortingFacility

number_of_days = 3
senders = (Sender("Jan Kowalski", "Tczew"), Sender("Maria Rutkowska", "Rumia"), Sender("Jerzy Brzuszek", "Wejherowo"))
facility = SortingFacility()

for day in range(number_of_days):
    print(f"Day {day + 1}")
    for sender in senders:
        parcels = sender.prepare_parcels(random.randint(2,10))
        facility.take_parcels_from_sender(parcels)
    sleep(10)