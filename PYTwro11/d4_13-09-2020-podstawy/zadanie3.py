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
                return True
            else:
                return False

class KontrolerNaglowka(object):
    def __init__(self):
        self.nazwa = "Naglowek"
    def control(self, plik):
        o_file = open(plik, 'r')
        c_file = o_file.readline()
        o_file.close()
        if c_file.isupper():
            return True
        else:
            return False

class KontrolerBasha(object):
    def __init__(self):
        self.nazwa = "Bash"
    def control(self, plik):
        if plik.endswith('.sh'):
            o_file = open(plik, 'r')
            c_file = o_file.readline()
            o_file.close()
            if '#!/bin/sh' in c_file:
                return True
            else:
                return False
        else:
            return False

class KontrolerTabulacji(object):
    def __init__(self):
        self.nazwa = 'Tabulatory'
    def control(self, plik):
        if plik.endswith('.py'):
            o_file = open(plik, 'r')
            c_file = o_file.read(-1)
            o_file.close()
            if '\t' in c_file:
                return True
            else:
                return False
        else:
            return False

class MasterControl(object):
    def __init__(self, control_list):
        self.lista_kontrolerow = control_list
    def testall(self, file):
        test_dict = dict()
        for x in self.lista_kontrolerow:
            test_dict[x.nazwa] = x.control(file)
        return test_dict

# tworzenie instancji Kontrolerow
test1 = KontrolerPrzeklenstw()
test2 = KontrolerNaglowka()
test3 = KontrolerBasha()
test4 = KontrolerTabulacji()

# wysylanie listy z instancja do glownego kontrolera
master_test1 = MasterControl({test1,test2,test3,test4})

# wywolywanie glownego kontrolera z plikiem
print(master_test1.testall('test.txt'))
print(master_test1.testall('test.sh'))
print(master_test1.testall('test.py'))

