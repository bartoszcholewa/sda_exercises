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

def write_file(path):
    with open(path, 'w') as f:
        for index in range(10):
            f.write(f'To jest linia numer: {index}\n')


def read_file(path):
    with open(path, 'r') as f:
        return f.readlines()


write_file('sample.txt')
content = read_file('sample.txt')
print(*content)
