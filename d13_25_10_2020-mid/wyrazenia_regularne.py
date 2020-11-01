"""
Sprawdź, czy podany nr telefonu jest poprawny,
przykladowe poprawne formaty:
    500500500
    +48500500500
    0048500500500
"""
import re


def is_phone_number(number: str):
    pattern = r"(\+48|0048)?\d{9}"
    p = re.compile(pattern)
    return bool(p.fullmatch(number))
    # return bool(re.fullmatch(pattern, number))


print(is_phone_number('0048500500500'))  # True
print(is_phone_number('0049500500500'))  # False
