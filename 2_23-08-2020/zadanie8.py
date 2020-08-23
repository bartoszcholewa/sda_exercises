def wytnij_liczny(tekst):
    digits_from_tekst = []
    for letter in tekst:
        if letter.isdigit():
            digits_from_tekst.append(int(letter))
    return digits_from_tekst


user_input = input("Wprowadz znaki: ")
print(f"Liczby z tekstu to: {wytnij_liczny(user_input)}")
