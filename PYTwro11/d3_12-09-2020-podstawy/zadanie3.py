def wytnij_liczny(tekst):
    return [letter for letter in tekst if letter.isdigit()]

user_input = input("Wprowadz znaki: ")
print(wytnij_liczny(user_input))