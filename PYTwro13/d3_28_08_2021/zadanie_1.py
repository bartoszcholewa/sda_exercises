"""
Poruszane tematy:
pętla for
pętla while
co to jest funkcja
co to są argumenty funkcji
jak zdefiniować argumenty funkcji (pozycyjne, kluczowe)
kwarksy i argsy
operacje na plikach open()

"""


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


d = delta(1, 2, 3)
print(d)


def args_kwargs(*args, **kwargs):
    print(f'What in args:{args}')
    print(f'What in kwargs {kwargs}')


args_kwargs(1, 2, 3, 'a', 'b', 'c', a=1, b=2, c=3)

a = '/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/PYTwro13/d3_08_2021/zadanie_1.py'
b = r'C:\Users\LucWr\Dysk_Google_Maja\PYTHON\_PYTHON_projekty\Powtorka\2-kalkulator.py'

"""
Operacje na plikach:
'r' - tryb do odczytu (read)
'w' - tryb do zapisu
'x' - tryb do tworzenia, błąd gdy plik istnieje
'a' - tryb dopisywania do pliku
'b' - binarny
't' - tryb tekstowy
'+' - tryb dopisywania z odczytem
"""

# f = open('/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/PYTwro13/d3_08_2021/plik.txt', 'r')
# while True:
#     line = f.readlines()
#     if not line:
#         break
#     print(line)

with open('sample.txt', 'w') as f:
    for index in range(10):
        f.write(f'To jest linia numer: {index} \n')


def read_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(f'{line}')


read_file('sample.txt')
