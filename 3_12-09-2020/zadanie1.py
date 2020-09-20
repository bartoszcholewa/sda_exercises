#otwieranie plikow
# file = open(filename, mode)

#file modes:
# r - tylko do odczytu
# w - tworzy jesli nie instnieje, modyfikuje, czyści istniejący, nie czyta
# x - tworzy plik, jesli juz insnieje, operacja sie wypieprzy
# a - dopisuje do istniejacej, tworzy jest nie istnieje, nie czyta
# t - domyslny, otwiera w trybie tekstowym
# b - otwiera w trybie binarnym
# + - updateting (write and rea)

#zamykanie pliku
# file.close()

# with open(filename, mode) as f:
#     f.read(5) - czyta pierwsze 5 znaków z pliku
#     f.readline() - czyta pierwszą linijkę tekstu
#     f.readlines() - zwraca cały tekst jako lista, gdzie kazdy element to jedna linijka
#     f.write("Whoops!")

def file_a(plik):
    # a - dopisuje do istniejacej, tworzy jest nie istnieje, nie czyta
    with open(plik, "a") as f:
        f.write("Pierwsza linijka \n druga linijka")
        # f.read(2) - not readable
        # f.readline() - not readable
        #f.readlines() - not readable
        f.write("Whoops!")

def file_w(plik):
    # w - tworzy jesli nie instnieje, modyfikuje, czyści istniejący, nie czyta
    with open(plik, "w") as f:
        f.write("Pierwsza linijka \n druga linijka")
        # f.read(2) - not readable
        # f.readline() - not readable
        # f.readlines() - not readable
        f.write("Whoops!")

def file_r(plik):
    # r - tylko do odczytu, plik musi istnieć (FileNotFoundError)
    with open(plik, "r") as f:
        # f.write("Pierwsza linijka \n druga linijka") # FileNotFoundError, not writable
        print(f.read(5))
        print(f.readline())
        print(f.readlines())
        # f.write("Whoops!") # not writable

def file_plus(plik):
    # + - updating (write and read)
    # ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    with open(plik, "+") as f:
        f.write("Pierwsza linijka \n druga linijka") # FileNotFoundError, not writable
        print(f.read(5))
        print(f.readline())
        print(f.readlines())
        f.write("Whoops!") # not writable

def file_a_plus(plik):
    # a - dopisuje do istniejacej, tworzy jest nie istnieje, nie czyta
    # + - updating (write and read)
    with open(plik, "a+") as f:
        f.write("Pierwsza linijka \n druga linijka")
        print(f.read(5))
        print(f.readline())
        print(f.readlines())
        f.write("Whoops!") # not writable

def file_r_plus(plik):
    # a - dopisuje do istniejacej, tworzy jest nie istnieje, nie czyta
    # + - updating (write and read)
    with open(plik, "r+") as f:
        f.write("Pierwsza linijka \n druga linijka")
        print(f.read(5))
        print(f.readline())
        print(f.readlines())
        f.write("Whoops!") # not writable

#file_a("plik1.txt")
#file_w("plik2.txt")
#file_r("plik1.txt")s
file_a_plus("plik4.txt")