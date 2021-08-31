# Context manager - Przykład klasa
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # otwarcie i udostępnienie zasobów
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # sprzątanie, zwalnianie zasobów
        self.file.close()


# przyklad - funkcja
from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()


# Zadanko - napiszmy context manager - file_reader - ktory automatycznie bedzie mial
# tylko mozliwosc odczytu + endoding utf-8
import json
from pprint import pprint


@contextmanager
def file_reader(name):
    f = open(name, mode='r', encoding='utf-8')
    yield f
    f.close()


with file_reader('pracownicy.json') as json_data:
    data = json.load(json_data)
    pprint(data)
