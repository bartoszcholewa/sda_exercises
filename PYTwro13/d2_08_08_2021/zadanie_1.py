"""
List / Set Comprehension - porównanie działania i prędkości
"""
from datetime import datetime
num = 100000000

start = datetime.now()
a = []
for x in range(num):
    if x % 2:
        a.append(x)
duration = datetime.now() - start
print(f'Normal For: {duration}')


start2 = datetime.now()
b = (x for x in range(num) if x % 2)
print(type(b))
duration2 = datetime.now() - start2
print(f'Comprehension For: {duration2},\nfaster by {duration - duration2}')

