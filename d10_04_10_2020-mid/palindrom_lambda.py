"""
Dodatkowo proszę (ćwiczenie lambdy), żebyście napisali funkcję, która z przekazanej listy słów zwróci listę
zawierającą palindromy (niech wielkość liter nie ma znaczenia). (edited)
"""


def palindrom(list_of_words: list) -> iter:
    return list(filter(lambda x: x.lower() == x[::-1].lower(), list_of_words))


words_list = ['Bartosz', 'Cholewa', 'Aga', 'nie', 'mam', 'Xanax', 'super', 'Anna']
print(palindrom(words_list))

# Bartosz Cholewa
