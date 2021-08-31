# sorting_facility
import time
import random
from itertools import chain, groupby
from collections import defaultdict
from functools import wraps
from pprint import pprint


def log_sorting_facility_status(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print("==== DECORATOR START ====")
        print(f"Function: '{func.__name__}'")
        pprint(f"Arguments: {args}")
        result = func(self, *args, **kwargs)

        try:
            self.log_parcels()
        except AttributeError as exc:
            print(f"ERROR: {exc}")

        print("==== DECORATOR END ====")
        return result
    return wrapper



class SortingFacility:
    def __init__(self):
        self.parcels_sorted_by_destination = defaultdict(list)

    @log_sorting_facility_status
    def take_parcels_from_sender(self, parcels_from_sender):
        print(f"{len(parcels_from_sender)} new parcels in facility")
        # zmiana wymagań, paczki sortujemy od razu po odebraniu od nadawcy
        self._sort_parcels(parcels_from_sender)

    def _sort_parcels(self, parcels):
        sorted_parcels = sorted(parcels, key=lambda parcel: parcel.destination)
        for destination, parcels in groupby(sorted_parcels, lambda parcel: parcel.destination):
            for parcel in parcels:
                self.parcels_sorted_by_destination[destination].append(parcel)

    def log_parcels(self):
        #pprint(dict(self.parcels_sorted_by_destination))
        for city, parcels in self.parcels_sorted_by_destination.items():
            print(f"City '{city}' has {len(parcels)} parcels")

