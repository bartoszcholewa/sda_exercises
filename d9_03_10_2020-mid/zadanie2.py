""" Rozpakowywanie tupli, ignorowanie wartości """


def dzialanie(a: int, b: int) -> tuple:
    sum_ab = a + b
    sub_ab = a - b
    mult = a * b
    dev = a / b
    return sum_ab, sub_ab, mult, dev

a, b, *_ = dzialanie(10, 20)
print(a ,b)

def zadanie3():
    return range(1000)

a, b, *args, c, d, e, f, g = zadanie3()
print(a, b, c, d, e, f, g)

