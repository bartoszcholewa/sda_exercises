def retmenu():
    input("ENTER aby wrócić...\n")
    workbookmenu()

def workbook1():
    print("[1] To ćwiczenie rozbija wpisaną wartość liczbową \n(w systemie dziesiętnym) na sumy kolejnych potęg liczby 10\n")
    user_choice = int(input("Podaj liczbę: "))
    digits_number1 = len(str(user_choice))
    digits_number2 = len(str(user_choice))
    wynik = ""
    wynik_int = 0
    error = ""
    print(f"Twoja liczba {user_choice} posiada {digits_number1} znaków, jej pierwszym znakiem jest {int(str(user_choice)[0])}")
    for digit in str(user_choice):
        digits_number1 -= 1
        wynik += (f"{digit}x10^{digits_number1}")
        if digits_number1 == 0:
            wynik += (" = ")
        else:
            wynik += (" + ")

    for digit in str(user_choice):
        digits_number2 -= 1
        wynik_int += (int(digit)*10**(int(digits_number2))) # + 1 # Trigger math error!
        wynik += str(int(digit)*10**(int(digits_number2)))
        if digits_number2 == 0:
            if (int(user_choice)==wynik_int):
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
    print("To jest część z Workbooka2")

def workbookmenu():
    print("[WORKBOOK] Wybierz ćwiczenie:\n [1] Systemy liczbowe - dziesiętne\n [2] Systemy liczbowe - inne\n [0] - wróć\n")
    user_choice = int(input("Wybór: "))
    if (user_choice==1):
        workbook1()
        retmenu()
    elif (user_choice==2):
        workbook2()
        retmenu()
    else:
        return


def main():
    workbookmenu()

if __name__=="__main__":
    main()
