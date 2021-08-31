"""
Zadanie 10
Z użyciem map, filter, reduce napisz kod, który:
1. Dla podanej listy liczb zwróci te, które są podzielne przez 5.
2. Dla par liczb zapisanych w liście [(a, b), (c, d),
(e, f)...] zwróci listę sum tych par, z których iloczyn jest podzielny przez 5.
3. Dla danego słownika zwróci listę stringów ze złączonymi za pomocą podkreślnika kluczami i
wartościami, gdzie klucz zostanie dodatkowo zamieniony na wielkie litery {"klucz":
"wartosc"} -> ["KLUCZ_wartosc"]
4. Za pomocą samego reduce: sumę tych elementów tablicy liczbowej, które są większe od 10
(pierwszy - dowolny)
"""
from functools import reduce

'''
sequence0 = [10, 2, 8, 7, 5, 4, 3, 11, 1, 1, 12, 11, 3, 2]
mapped = map(lambda x: x * x, sequence0)
print(list(mapped))  # [100, 4, 64, 49, 25, 16, 9, 121, 1, 1, 144, 121, 9, 4]

filtered = filter(lambda x: x < 5, sequence0)
print(list(filtered))  # [2, 4, 3, 1, 1, 3, 2]

product = reduce((lambda x, y: x * y), sequence0)
print(product) # 585446400
'''
sequence1 = [9, 2, 8, 7, 5, 4, 3, 11, 1, 1, 12, 11, 3, 2, 10, 15]
podzielne_przez_5 = filter(lambda x: x % 5 == 0, sequence1)
print(list(podzielne_przez_5)) # [5, 10, 15]

sequence2 = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 1)]
sum_podzielnych_przez_5 = filter(lambda x: (x[0] * x[1]) % 5 == 0, sequence2)
b = map(sum, sum_podzielnych_przez_5)
print(list(b)) # [(7, 8), (9, 1)]

sequence3 = {"jeden": "dwa", "trzy": "cztery", "piec": "szesc", "siedem": "osiem", "dziewiec": "zero"}
slownik_na_liste = map(lambda x: x[0].upper() + '_' + x[1], sequence3.items())
print(list(slownik_na_liste)) # ['JEDEN_dwa', 'TRZY_cztery', 'PIEC_szesc', 'SIEDEM_osiem', 'DZIEWIEC_zero']

sequence4 = [5, 5, 15, 5, 1, 0, 1, 20] # 5 + 15 + 20 = 40
suma_wiekszych_od_10 = reduce(lambda x, y: x + y if y > 10 else x, sequence4)
print(suma_wiekszych_od_10)