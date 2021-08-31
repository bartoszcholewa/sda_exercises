"""
Zadanie 42
Skopiuj listę pracowników z zadania 41 i wklej ją do pliku. Wczytaj plik i oblicz średnią pensję dla
pracowników w firmie.
Dołącz wyliczoną pensję do obiektu (do każdej firmy) i zapisz tak zmienione dane jako JSON w
innym pliku.
"""

import json
from pprint import pprint
from statistics import mean
with open("pracownicy.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
# data is now a Python object and can be modified

avg_salaries = dict()
for firma, pracownicy in data.items():
    avg_salaries[firma] = []
    for pracownik in pracownicy:
        avg_salaries[firma].append(pracownik['salary'])
    avg_salaries[firma] = mean(avg_salaries[firma])
    data[firma].append({'avg_salaries': avg_salaries[firma]})

pprint(data)

with open("save.json", "w", encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)