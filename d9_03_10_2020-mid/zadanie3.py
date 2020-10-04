'''
Zadanie 3.
Za pomocą rozpakowywania i list comprehensions zamień listę krotek na słownik
prices = [("apples", 5.50), ("oranges", 6.30), ("bananas", 3.44)]
prices_dict = { <uzupełnij> }
'''

prices = [("apples", 5.50), ("oranges", 6.30), ("bananas", 3.44)]
print({x:y for x,y in prices})