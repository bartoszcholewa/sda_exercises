"""
Dict Comprehension - porównanie działania i prędkości
"""

import string
from datetime import datetime

start = datetime.now()
a = {}
for letter in string.ascii_letters:
    a[letter] = ord(letter)
duration = datetime.now() - start
print(f'Dict For: {duration}')
print(a)

start2 = datetime.now()
b = {letter: ord(letter) for letter in string.ascii_letters}
duration2 = datetime.now() - start2
print(f'Comp For: {duration2}')
print(b)
