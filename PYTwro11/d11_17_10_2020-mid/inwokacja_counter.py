from collections import Counter
import os

# print(os.getcwd())
# # os.walk()
# # os.chdir("")
#
# with open('inwokacja.txt', 'r', encoding='utf-8') as file:
#     inwokacja = file.read().lower()
#     words = inwokacja.split()
#     cnt = Counter(words)
#     print(cnt)

with open('inwokacja.txt', encoding='utf-8') as file:
    l = ''.join(letter.lower() for row in file for letter in row if letter.isalpha() or letter == " " or letter == "\n").split()
    print(Counter(l))
