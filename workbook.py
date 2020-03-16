def retmenu():
    input("ENTER aby wrócić...\n")
    workbookmenu()


def workbook1():
    print(
        "[1] To ćwiczenie rozbija wpisaną wartość liczbową \n(w systemie dziesiętnym) na sumy kolejnych potęg liczby 10\n")
    user_choice = int(input("Podaj liczbę całkowitą: "))
    digits_number1 = len(str(user_choice))
    digits_number2 = len(str(user_choice))
    wynik = ""
    wynik_int = 0
    error = ""
    print(
        f"Twoja liczba {user_choice} posiada {digits_number1} znaków, jej pierwszym znakiem jest {int(str(user_choice)[0])}")
    for digit in str(user_choice):
        digits_number1 -= 1
        wynik += (f"{digit}x10^{digits_number1}")
        if digits_number1 == 0:
            wynik += (" = ")
        else:
            wynik += (" + ")

    for digit in str(user_choice):
        digits_number2 -= 1
        wynik_int += (int(digit) * 10 ** (int(digits_number2)))  # + 1 # Trigger math error!
        wynik += str(int(digit) * 10 ** (int(digits_number2)))
        if digits_number2 == 0:
            if (int(user_choice) == wynik_int):
                wynik += (f" = {wynik_int}")
            else:
                error = f"Błąd programu! Podana wartość {user_choice} nie jest równa wynikowi skryptu {wynik_int}"
        else:
            wynik += (" + ")

    if error:
        print(error)
    else:
        print(wynik)


def workbook2():
    print("[2] To ćwiczenie przekształca podaną liczbę w podanym systemie liczbowym na liczbę w systemie dziesiętnym")
    user_base = int(input("Podaj system liczbowy (1-10, 16): "))
    system_types = {1: "jedynkowy",
                    2: "dwójkowy",
                    3: "trójkowy",
                    4: "czwórkowy",
                    5: "piątkowy",
                    6: "szóstkowy",
                    7: "siódemkowy",
                    8: "ósemkowy",
                    9: "dziewiątkowy",
                    10: "dziesiętny",
                    16: "szesnastkowy"}
    if (user_base >= 1 and user_base <= 10):
        print(f"Wybrano system {system_types[user_base]}.")
        user_number = int(input(f"Wprowadź liczbę w systemie {system_types[user_base]}m: "))
        validate_user_number = max(set(str(user_number)))
        if int(validate_user_number) >= int(user_base):
            print(f"Liczba {user_number} w systemie {system_types[user_base]}m nie jest poprawna!\nSpróbuj ponownie!")
            workbook2()
        else:
            digits_number1 = len(str(user_number))
            digits_number2 = len(str(user_number))
            wynik = ""
            wynik_int = 0
            error = ""
            # print(f"Twoja liczba {user_number} posiada {digits_number1} znaków, jej pierwszym znakiem jest {int(str(user_number)[0])}")
            for digit in str(user_number):
                digits_number1 -= 1
                wynik += f"{digit}x{user_base}^{digits_number1}"
                if digits_number1 == 0:
                    wynik += " = "
                else:
                    wynik += " + "

            for digit in str(user_number):
                digits_number2 -= 1
                wynik_int += (int(digit) * int(user_base) ** (int(digits_number2)))  # + 1 # Trigger math error!
                wynik += str(int(digit) * int(user_base) ** (int(digits_number2)))
                if digits_number2 == 0:
                    wynik += (f" = {wynik_int}")
                    # if (int(user_number) == wynik_int):
                    #    wynik += (f" = {wynik_int}")
                    # else:
                    #    error = f"Błąd programu! Podana wartość {user_number} nie jest równa wynikowi skryptu {wynik_int}"
                else:
                    wynik += (" + ")

            if error:
                print(error)
            else:
                print(wynik)

    elif (user_base == 16):
        print(f"Wybrano system {system_types[user_base]}.")
        user_number = str(input(f"Wprowadź liczbę w systemie {system_types[user_base]}m: "))
        validate_user_number = set(list(user_number))
        hex_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
        validate_hex = validate_user_number.difference(hex_set)
        if validate_hex:
            print(f"Liczba {user_number} w systemie {system_types[user_base]}m nie jest poprawna!\nSpróbuj ponownie!")
            workbook2()
        else:
            hex_to_decimal = {"0": 0,
                              "1": 1,
                              "2": 2,
                              "3": 3,
                              "4": 4,
                              "5": 5,
                              "6": 6,
                              "7": 7,
                              "8": 8,
                              "9": 9,
                              "A": 10,
                              "B": 11,
                              "C": 12,
                              "D": 13,
                              "E": 14,
                              "F": 15}
            digits_number1 = len(str(user_number))
            digits_number2 = len(str(user_number))
            wynik = ""
            wynik_int = 0
            error = ""
            # print(f"Twoja liczba {user_number} posiada {digits_number1} znaków, jej pierwszym znakiem jest {int(str(user_number)[0])}")
            for digit in str(user_number):
                digits_number1 -= 1
                wynik += f"{digit}x{user_base}^{digits_number1}"
                if digits_number1 == 0:
                    wynik += " = "
                else:
                    wynik += " + "

            for digit in str(user_number):
                digits_number2 -= 1
                wynik_int += (int(hex_to_decimal[digit]) * int(user_base) ** (int(digits_number2)))  # + 1 # Trigger math error!
                wynik += str(int(hex_to_decimal[digit]) * int(user_base) ** (int(digits_number2)))
                if digits_number2 == 0:
                    wynik += (f" = {wynik_int}")
                    # if (int(user_number) == wynik_int):
                    #    wynik += (f" = {wynik_int}")
                    # else:
                    #    error = f"Błąd programu! Podana wartość {user_number} nie jest równa wynikowi skryptu {wynik_int}"
                else:
                    wynik += (" + ")

            if error:
                print(error)
            else:
                print(wynik)

    else:
        print(f"Wartość {user_base} nie jest poprawnym/zdefiniowanym systemem liczbowym")


def workbookmenu():
    print(
        "[WORKBOOK] Wybierz ćwiczenie:\n [1] Systemy liczbowe - dziesiętne\n [2] Systemy liczbowe - inne\n [0] - wróć\n")
    user_choice = int(input("Wybór: "))
    if (user_choice == 1):
        workbook1()
        retmenu()
    elif (user_choice == 2):
        workbook2()
        retmenu()
    else:
        return


def main():
    workbookmenu()


if __name__ == "__main__":
    main()
