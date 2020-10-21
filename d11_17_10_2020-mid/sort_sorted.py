"""
Zadanie 11
Napisz funkcję sortującą litery w stringu i zwracającą string.
Napisz funkcję, która posortuje i zwróci listę liczb bez duplikatów.
"""
from statistics import mean

print(''.join(sorted("Babcia jest super")))

lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

print(sorted(set(lista)))

lista2 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
lista3 = list(set(lista2))
print(lista3)

# Sortowanie listy wg pierwszego elementu
a = [(1, 2, 3), (6, 6, 6)]
print(sorted(a, key=lambda x: x[1]))

# Zadanie 14
# Listę zawierającej krotki o różnej długości posortuj wg średniej wartości elementów.

krotka = [(9,9,9,9,9,9), (1,2,3,1), (4,5,6,2,3), (7,8,9,4,5,6,7)]
sortowanie = sorted(krotka, key=mean)
print(sortowanie)

tablice_stringow = ('abc', 'bcdeasdsad', 'rt23redasd', 'asd4rfaddasd')
dlugosc = sorted(tablice_stringow, key=len)
print(dlugosc)