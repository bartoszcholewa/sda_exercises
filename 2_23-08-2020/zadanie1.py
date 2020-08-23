import string

def pangram(s):
    # utworz set wszystkich znakow alfabetu
    a = set(string.ascii_lowercase)

    # utworz set malych znakow z input
    set_s = set(s.lower())

    filtered_set = set()
    for letter in set_s:
        if letter >= 'a' and letter <= 'z':
            filtered_set.add(letter)

    # utworz set posiadajacy roznice pomiedzy inputem a alfabetem
    diff = a.difference(filtered_set)

    # utworz set posiadajacy roznice symetryczna pomiedzy inputem a alfabetem
    # posiada spacje, znaki specjalne
    sym = a.symmetric_difference(filtered_set)

    print(s)
    if not diff:
        return True
    else:
        return False

pan1 = "The quick brown fox jumps over the lazy dog"
pan2 = "Sphinx of black quartz, judge my vow"
pan3 = "Pack my box with five dozen liquor jugs, abc! -!@#$%^&*()_+__)****&#$%^&*"

print(f"Czy to pangram?: {pangram(pan3)}")