
def liczydlo(zdanie):
    slownik = {}
    for letter in zdanie:
        if letter.isalpha():
            if letter not in slownik:
                slownik[letter] = 1
            else:
                slownik.pop(letter)
    return slownik

print(liczydlo("Nie lubie plakow bardzo mocno!"))
