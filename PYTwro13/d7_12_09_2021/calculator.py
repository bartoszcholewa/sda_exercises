"""
Calculator module
"""
import operator


def dej_number(number_a):
    """ NO DEJ! """
    return number_a


def dej_nurnber(nurnber_a):
    """ DEJ TOM LICZBE! """
    return int(nurnber_a)


def dodawanie(number_x, number_y):
    """ Operator dodawania """
    return operator.add(dej_number(number_x), dej_number(number_y))


def odejmowanie(number_x, number_y):
    """ Operator odejmowania """
    return operator.sub(dej_nurnber(number_x), dej_nurnber(number_y))


def dzielenie(number_x, number_y):
    """ Operator odejmowania """
    return dej_nurnber(number_x) / dej_number(number_y)


def mnozenie(number_x, number_y):
    """ Operator mnożenia """
    return operator.mul(dej_nurnber(number_x), dej_number(number_y))


def main():
    """ Main function """
    number_w = 0
    number_x = input("podaj pierwsza liczbe: ")
    number_z = input("podaj znak dzialania: ")
    number_y = input("podaj druga liczbe: ")

    if number_z == "+":
        number_w = dodawanie(number_x, number_y)
    elif number_z == "-":
        number_w = odejmowanie(number_x, number_y)
    elif number_z == "*":
        number_w = mnozenie(number_x, number_y)
    elif number_z == "/":
        number_w = dzielenie(number_x, number_y)

    print(number_w)


if __name__ == '__main__':
    main()
