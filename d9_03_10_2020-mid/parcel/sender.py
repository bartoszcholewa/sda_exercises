import parcels
from time import sleep


class Sender:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def _prepare_parcel(self):
        sleep(0.01)  # it takes some time to prepare parcel...
        new_package = next(parcels.parcel_generator)
        new_package.sender_name = self.name
        new_package.sender_origin = self.origin
        return new_package

    def prepare_parcels(self, n):
        return [self._prepare_parcel() for _ in range(n)]


if __name__ == "__main__":
    sender1 = Sender(name="DHL", origin="Krakow")

    paczki = sender1.prepare_parcels(5)
    for paczka in paczki:
        print(paczka.size)
