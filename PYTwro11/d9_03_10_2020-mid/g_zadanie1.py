'''
Zadanie 1:
Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.
'''

def fib(): #iteracyjna
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

# f = fib()
# for i in range(10):
#     print(next(f))

'''
Zadanie 1*:
*Zadania z gwiazdką to zadania dla osób, które zrobią podstawową wersję szybciej lub zadania
do poćwiczenia w domu.
Dodaj do funkcji generującej argument n, który ograniczy liczbę generowanych wyrazów ciągu.
Stwórz generator i użyj go w wyrażeniu list comprehension (typu [x for x in f] ) by stworzyć
listę będącą kwadratami pierwszych n wyrazów ciągu Fibonacciego.
'''

def fib_n(n): #iteracyjna
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

f = fib_n(100)
fib_square = [x**2 for x in f]
print(fib_square)
