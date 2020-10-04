'''Zadanie 4.
Użyj funkcji range by wygenerować listę 10 elementów. Napisz funkcję, która przyjmuje 10
elementów i zwraca ich sumę oraz różnicę. Użyj rozpakowywania w wywołaniu funkcji, aby
przekazać 10 parametrów.'''

a = [*range(10)]
def zadanie4(*args):
    d = 0
    return sum(args), sum(0-i for i in args)

print(zadanie4(*a))
