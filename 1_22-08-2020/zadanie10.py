def dodaj_do_siebie_cyfry_w_liczbie(liczba=12345):
    suma = 0
    for x in str(liczba):
        suma = int(x) + suma
    a = f"Suma cyfr {liczba} to {suma}"
    return a

def dodaj_do_siebie_cyfry_w_liczbie_az_do_1_znaku(liczba=999):
    suma = 0
    print = str(liczba)
    while not len(str(liczba)) <= 1:
        for x in str(liczba):
            suma = int(x) + suma
        liczba = suma
        suma = 0
    a = f"Cyfry liczby {print} dodane do siebie az do 1 cyfry to: {liczba}"
    return a

print(dodaj_do_siebie_cyfry_w_liczbie(84758347))
print(dodaj_do_siebie_cyfry_w_liczbie_az_do_1_znaku(3847587345))
