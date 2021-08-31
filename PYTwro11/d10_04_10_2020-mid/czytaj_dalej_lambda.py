'''
Zadanie 9
W systemie blogowym potrzebna są funkcje, które skrócą tekst do pierwszych n znaków i
dodadzą do niego "... czytaj dalej". Napisz funkcję generującą lambdy spełniające te wymagania
dla danego n.
* Dla chętnych: Sprawdź czy twoja funkcja działa z tekstem krótszym od n i ew. popraw jej
działanie.
'''

def czytaj_dalej(n):
    return lambda text : text[:n] + '..czytaj dalej' if len(text) > n else text

if __name__ == "__main__":
    czytaj_10 = czytaj_dalej(20)
    czytaj_50 = czytaj_dalej(50)

    tekst10 = "Mniej niż 20 znaków."
    tekst20 = "Ten tekst ma więcej niż 20 znaków"
    print(czytaj_10("Mniej"))
    print(czytaj_10(tekst10))
    print(czytaj_10(tekst20))
