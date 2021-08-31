"""
Zadanie 6.
Zmodyfikuj funkcję z zadania 4. by przyjmowała dowolną liczbę argumentów. Przetestuj
wywołanie dla różnych długości listy.
"""
a = [*range(100)]
def zadanie4(*args):
    d = 0
    return sum(args), sum(0-i for i in args)

print(zadanie4(*a))
