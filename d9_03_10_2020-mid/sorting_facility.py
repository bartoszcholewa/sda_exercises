# sorting_facility
from itertools import chain
class SortingFacility:
    def __init__(self):
        self.parcels = []

    def take_parcels_from_sender(self, parcels_from_sender):
        print(f"{len(parcels_from_sender)} new parcels in facility")
        self.parcels.append(parcels_from_sender)

    def sort_parcels(self):
        for parcel in chain(*self.parcels):
            print(parcel)
