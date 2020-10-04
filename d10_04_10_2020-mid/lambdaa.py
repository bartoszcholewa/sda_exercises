'''
Zadanie 9
W systemie blogowym potrzebna są funkcje, które skrócą tekst do pierwszych n znaków i
dodadzą do niego "... czytaj dalej". Napisz funkcję generującą lambdy spełniające te wymagania
dla danego n.
* Dla chętnych: Sprawdź czy twoja funkcja działa z tekstem krótszym od n i ew. popraw jej
działanie.
'''

mapped = map

def czytaj_dalej(n):
    return lambda text : text[:n] + '..czytaj dalej' if len(text) > n else text
do_dziesieciu_czytaj_dalej = czytaj_dalej(10)
do_piedziesieciu_czytaj_dalej = czytaj_dalej(50)

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore."
print(do_dziesieciu_czytaj_dalej("Abecadlo"))
print(do_dziesieciu_czytaj_dalej(tekst))
print(do_piedziesieciu_czytaj_dalej(tekst))
