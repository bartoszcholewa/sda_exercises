def fib(n): #iteracyjna
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a, b = b, c
    return a

print(fib(10))

def fib_re(n): #rekurencja
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_re(n-1) + fib_re(n-2)

print(fib_re(10))
