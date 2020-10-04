from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

# lst = get_n_primes(1000000000)
# for elem in lst:
#     print(elem)

# iteracja
class PrimeIterator:
    # Iterator pozwalający na iterowanie po n liczbach pierwszych
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self): # referencja do instancji tej klasy
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()

#
# iter = PrimeIterator(1000000)
# for elem in iter:
#     print(elem)


# Generator
def prime_generator(n):
     # Generator pozwalający na iterowanie po n liczbach pierwszych
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1

gen = prime_generator(100000)
print(next(gen))
print(next(gen))
print(next(gen))