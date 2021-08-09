def dod(x, y):
    print(f'{x} + {y} = {x + y}')

def calc(a, b):
    """ Napisz funkcję która przyjmię od użytkownika dwie liczby i je do siebie doda """
    print("== Kalkulator Dodawania ===")
    a = int(input('Podaj pierwszą liczbe: '))
    b = int(input('Podaj drugą liczbe: '))
    return a + b

def foo(l, b=None):
    if b is None:
        b = []
    print(id(l))
    l.append(3)