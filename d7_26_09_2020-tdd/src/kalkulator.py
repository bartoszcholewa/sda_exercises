# Testowanie:
# - Unit Tests, Testy Integracyjne, End-To-End Tests

# PYTEST - narzedzie testowania, dobra dokumentacjap
#nvidia jetson #deepstream

import pytest

#Konwencja nazewnictwa testow
# test_<nazwa_funkcji>_<komentarz>

def add_numbers(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        raise Exception("Warunek musi byc liczba")



