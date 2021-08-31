"""
Zaprojektuj  klasę Complex,  reprezentującą  liczby  zespolone  wraz z podstawowymi działaniami arytmetycznymi i porównaniem.
W klasie powinny znaleźć się następujące metody
1.  dodawanie: add(arg)
2.  odejmowanie: sub(arg)
3.  równość: equals(arg)
4. mnożenie: mul(arg)
7.  tekstowa reprezentacja liczby:to_string().
"""


class Complex:

    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def add(self, other: 'Complex') -> str:
        self.real += other.real
        self.imaginary += other.imaginary
        return self.to_string()

    def sub(self, other: 'Complex'):
        self.real -= other.real
        self.imaginary -= other.imaginary
        return self.to_string()

    def equals(self, other: 'Complex') -> bool:
        return bool((self.real == other.real) and (self.imaginary == other.imaginary))

    def mul(self, other: 'Complex'):
        self.real = self.real * other.real * self.imaginary * other.imaginary * -1
        self.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return self.to_string()

    def to_string(self):
        if self.imaginary > 0:
            return f'{self.real}+{self.imaginary}j'
        else:
            return f'{self.real}{self.imaginary}j'

    def to_complex(self):
        return complex(self.real, self.imaginary)


if __name__ == '__main__':
    a = Complex(5, 10)
    b = Complex(2, 7)
    print(a.add(b))
    print(a.to_string())
    print(a.equals(b))
    print(a.to_complex())
    print(a.sub(b))
    print(a.equals(b))
    print(a.mul(b))
