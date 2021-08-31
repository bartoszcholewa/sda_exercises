'''
Za pomocą dekoratora @dataclass można w szybki sposób tworzyć klasy służące do
przechowywania danych.
'''
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name:str
    age:int

person = Person(name="N", age=23)
# person.name = "Abc" - frozen TRUE
print(person.name)
'''
Taka klasa zachowuje się jak każda inna, jedynie zaoszczędza nam pisania konstruktora, metody
__repr__ i kilku innych... Możemy spowodować, by klasa bardziej przypominała krotkę pod
względem niemodyfikowalności, dodając do dekoratora dataclass atrybut frozen=False.
'''