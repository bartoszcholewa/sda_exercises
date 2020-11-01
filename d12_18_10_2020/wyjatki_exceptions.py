"""
Exceptions
Błędy wykryte w trakcie działania programu nazywamy wyjątkami. Nie każdy wyjątek jest
niewybaczalnym błędem kończącym program. Wiele z nich da się obsłużyć by "wybrnąć" z
sytuacji.
Python ma wbudowane kilkadziesiąt typów wyjątków
( https://docs.python.org/3/library/exceptions.html#exception-hierarchy )
i pozwala na bardzo proste tworzenie kolejnych.
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print("Result: ", result)
    finally:
        print("Executing finally clause!")


while True:
    try:
        x = int(input("Please enter a number x: "))
        y = int(input("Please enter a number y: "))
        divide(x, y)
        break
    except ValueError:
        print("Invalid number, try again.")
