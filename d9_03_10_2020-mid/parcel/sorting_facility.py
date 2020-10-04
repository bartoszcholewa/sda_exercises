# sorting_facility
import time
import random
from itertools import chain


class SortingFacility:
    def __init__(self):
        self.parcels = []
        self.parcels_num = 0
        self.acc = 1

    def take_parcels_from_sender(self, parcels_from_sender):
        print(f"{self.parcels_num} new parcels in facility")
        self.parcels.append(parcels_from_sender)
        self.parcels_num += len(self.parcels)

    def sort_parcels(self):
        for parcel in chain(*self.parcels):
            time.sleep(random.uniform(0, 0.5))
            print(f'[{self.acc}/{self.parcels_num}] Destination: {parcel.destination} | Send Date: {parcel.send_time} '
                  f'| Size: {parcel.size} Serial Number: {parcel.serial_number}| Sender: '
                  f'{parcel.sender_name} | Sender Origin: {parcel.sender_origin}')
            self.acc += 1
