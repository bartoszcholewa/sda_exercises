""" Dekorator z argumentami i funkcja z argumentami """
from datetime import datetime


def run_only_between(from_=7, to_=22):
    def dec(func):
        def wrapper(*args, **kwargs):
            if from_ <= datetime.now().hour < to_:
                func(*args, **kwargs)

        return wrapper

    return dec


@run_only_between(10, 15)
def say_something(something):
    print(something)


say_something("Hello World")
