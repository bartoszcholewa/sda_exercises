'''
Zadanie 5.
Przygotuj słownik prepared_dict , który pozwoli wywołać funkcję za pomocą
polecenia print_greeting(**prepared_dict)
'''

prepared_dict = {"name": "Bartosz", "surname": "Cholewa", "age": 26}
def print_greeting(name, surname, age):
    print(f"Hi {name} {surname}. You are {age} years old, but you look like {age-3}.")

print_greeting(**prepared_dict)
