def kalkulator(liczba1, liczba2, dzialanie):
    if dzialanie == "+":
        wynik = int(liczba1) + int(liczba2)
    elif dzialanie == "-":
        wynik = int(liczba1) - int(liczba2)
    elif dzialanie == "*" or dzialanie == "x":
        wynik = int(liczba1) * int(liczba2)
    elif dzialanie == "/" or dzialanie == ":":
        if not int(liczba1) or not int(liczba2):
            wynik = "Blad dzielenia przez zero"
        else:
            wynik = int(liczba1) / int(liczba2)
    else:
        wynik = "Niepoprawne dzialanie"
    return wynik

liczba1 = input("Podaj pierwsza liczbe: ")
liczba2 = input("Podaj druga liczbe: ")
dzialanie = input("Podaj typ dzialania (+, *, x, /, :): ")
print(kalkulator(liczba1, liczba2, dzialanie))





