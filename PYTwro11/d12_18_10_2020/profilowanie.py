"""
Profilowanie
"""
from timeit import timeit
setup = """
import random
scale = 1000000
lucky_number = random.randint(0, scale)
"""

statement = """
shots = 0
while True:
    shot = random.randint(0, scale)
    if shot == lucky_number:
        print(f"BONZAIIII! after {shots} tries!")
        break
    shots += 1
"""

print(timeit(stmt=statement, setup=setup, number=10))