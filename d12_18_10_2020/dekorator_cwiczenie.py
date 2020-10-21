from datetime import datetime
from freezegun import freeze_time
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def greet_time(func):
    def wrapper():
        print(f"Time {datetime.now()}")
        func()

    return wrapper


"""
Zadanie 27
Napisz dekorator do_twice, który każdą funkcję, którą dekoruje wywoła dwukrotnie.
Napisz funkcję greet_president, która napisze uroczyste powitanie prezydenta i z szacunku
udekoruj ją napisanym dekoratorem.
"""


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        print("General Kenobi!")

    return wrapper


@do_twice
@greet_time
def greet_president():
    print("Hello there, Mr. President")


# greet_president()
# Time 2020-10-18 09:34:09.935947
# Hello there, Mr. President
# Time 2020-10-18 09:34:09.935985
# Hello there, Mr. President
# General Kenobi!

"""
Zadanie 29
Zmodyfikuj dekorator do_twice by pasował do każdego rodzaju funkcji.
Wymyśl 3 rodzaje funkcji: z argumentami pozycyjnymi, z argumentami nazwanymi i mieszaną
oraz bez argumentów. Przetestuj, że dekorator działa z każdą z funkcji.
"""


@do_twice
def argumenty_pozycyjne(a, b, c):
    print(f"Funkcja z argumentami pozycyjnymi dla a: {a}, b: {b}, c: {c}")


@do_twice
def argumenty_nazwane(d=1, e=2, f=3):
    print(f"Funkcja z argumentami nazwanymi dla d={d}, e={e}, f={f}")


@do_twice
def argumenty_mieszkane(g, h=4):
    print(f"Funkcja z argumentami mieszanymi dla g: {g}, h={h}")


@do_twice
def bez_argumentow():
    print("Funkcja bez argumentow")


# argumenty_pozycyjne(1, 2, 3)
# argumenty_nazwane(d=4, e=5, f=6)
# argumenty_mieszkane(7, h=8)
# bez_argumentow()


"""
Zadanie 30
Napisz dekorator funkcji, który przed wykonaniem zacznie mierzyć czas a na koniec wypisze:
Nazwę wykonanej funkcji, wszystkie argumenty przekazane do funkcji, czas
wykonania.
Samodzielnie zaproponuj funkcje, które udekorujesz i sprawdzisz działanie dekoratora."""
from functools import wraps
from time import sleep
import random


def czasomierz(name=True, show_args=True, show_kwargs=True, execution_time=True, loop_times=5):
    def czasomierz_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, loop_times + 1):
                print(f"Loop #{i}")
                print("=====================================")
                time_before = datetime.now()
                result = func(*args, *kwargs)
                if name:
                    print(f"Nazwa funkcji: {func.__name__}")
                if execution_time:
                    print(f"Czas wykonania: {datetime.now() - time_before}")
                if show_args:
                    print(f"Argumenty funkcji args: {args}")
                if show_kwargs:
                    print(f"Argumenty funkcji kwargs: {kwargs}")
                print("=====================================")
            return result
        return wrapper
    return czasomierz_decorator


"""
Zadanie kolejne
Napisz dekorator, który pozwoli wykonać kod dekorowanej funkcji tylko w dzień między 7 a 22 o nazwe disable_at_night
"""


def disable_at_night(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 7 <= datetime.now().hour <= 22:
            func(*args, *kwargs)
        else:
            print(f"Idź spać! Jest {datetime.now().hour} w nocy!!!")
    return wrapper


@czasomierz(name=True, show_args=True, show_kwargs=True, execution_time=True, loop_times=1)
@freeze_time('2020-10-18 08:04:05')
@disable_at_night
def funkcja_do_zmierzenia(argument1="1", argument2="2", argument3="3", *args, **kwargs):
    print("Wykonuje funkcje...")
    sleep(random.randint(1, 5))
    print("Łączenie argumentów:", argument1.upper() + argument2.upper() + argument3.upper())
    sleep(random.randint(1, 5))
    print("Skonczyłem funkcje!")


funkcja_do_zmierzenia(get_random_string(5), get_random_string(8), get_random_string(10), bartosz=get_random_string(10))
