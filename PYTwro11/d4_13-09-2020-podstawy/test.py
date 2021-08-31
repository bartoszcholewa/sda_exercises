class KontrolerPrzeklenstw(object):
    def __init__(self):
        self.nazwa = "Przeklenstwa"
    def control(self, plik):
        o_file = open(plik, 'r')
        c_file = o_file.read(-1)
        o_file.close()
        baza_przeklenstw = {'dupa', 'chuja', 'kurwa'}
        for x in baza_przeklenstw:
            if x in c_file:
                return {self.nazwa:True}
            else:
                return {self.nazwa:False}

class KontrolerNaglowka(object):
    def __init__(self):
        self.nazwa = "Naglowek"
    def control(self, plik):
        o_file = open(plik, 'r')
        c_file = o_file.readline()
        o_file.close()
        if c_file.isupper():
            return {self.nazwa:True}
        else:
            return {self.nazwa:False}

class KontrolerBasha(object):
    def __init__(self):
        self.nazwa = "Bash"
    def control(self, plik):
        if plik.endswith('.sh'):
            o_file = open(plik, 'r')
            c_file = o_file.readline()
            o_file.close()
            if '#!/bin/sh' in c_file:
                return {self.nazwa:True}
            else:
                return {self.nazwa: False}

class KontrolerTabulacji(object):
    def __init__(self):
        self.nazwa = 'Tabulatory'
    def control(self, plik):
        if plik.endswith('.py'):
            o_file = open(plik, 'r')
            c_file = o_file.read(-1)
            o_file.close()
            if '\t' in c_file:
                return {self.nazwa: True}
            else:
                return {self.nazwa: True}


test1 = KontrolerPrzeklenstw()
test2 = KontrolerNaglowka()
test3 = KontrolerBasha()
test4 = KontrolerTabulacji()
print(test1.control('test.txt'))
print(test2.control('test.txt'))
print(test3.control('test.sh'))
print(test4.control('test.py'))
