def prime_factors(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    li = list()

    for prime in primes:
        while x % prime == 0:
            li.append(prime)
            x = x / prime
    return li