"""Bonusowe zadanie dla chętnych - zabawa z dataclass:
1. Należy stworzyć klasę (na bazie dataclass oczywiscie) osoby, ktora bedzie posiadac 3 pola odzwierciedlające
następujace wartości (zachęcam oczywiscie do anglojęzycznych nazw): masa ciala, wzrost, indeks BMI. Masa ciała i wzrost
mają byc przekazane w konstruktorze, a indeks BMI musi być polem obliczonym. (tip: metoda magiczna __post_init__)
2. Potem należy stworzyć klasę sportowca (dziedziczmy!), która zawiera dodatkowe pole: płeć. I w zależności od tego,
czy osoba jest mężczyzną, czy kobietą, współczynnik BMI powinien być mnożony przez odpowiednio: 0.7 lub 0.8 (wiem wiem,
duze uproszczenie :slightly_smiling_face: )
3. Obiekty powinny byc porownywalne na bazie indeksu BMI, tzn. jeśli mateusz i andrzej są instancjami klas z
punktów 1 i/lub 2, to powinno być możliwe porównanie mateusz > andrzej itp. Tip: Obiekty powinny byc callable
(wywyoływalny - metoda __call__) i w wyniku wykonania - zwracać wartosc indeksu BMI """

from dataclasses import dataclass, field


@dataclass
class Person:
    body_weight: float
    body_height: float
    body_mass_index: float = field(init=False)

    def __post_init__(self):
        factor = 1
        if isinstance(self, Sportsman):
            if self.sex == "male":
                factor = 0.7
            elif self.sex == "female":
                factor = 0.8
        self.body_mass_index = round((self.body_weight / (self.body_height / 100) ** 2) * factor, 2)

    def __call__(self, *args, **kwargs):
        return self.body_mass_index


@dataclass
class Sportsman(Person):
    sex: str = None


bartek = Person(body_weight=75.5, body_height=180.5)
print(f"Bartek is a IT guy and his BMI is {bartek()}")

super_bartek = Sportsman(body_weight=75.5, body_height=180.5, sex="male")
print(f"But if Bartek were an sportsman, his BMI would be {super_bartek()}")

print(f"Does Bartek an IT guy have a higher BMI than Bartek an sportsman? {bartek() > super_bartek()}")

super_weird_bartek = Sportsman(body_weight=75.5, body_height=180.5, sex="female")
print(f"They told Bartek that he can be anyone, so he became a female athlete, and his...her BMI is now "
      f"{super_weird_bartek()}")
print(f"Does female athlete Bartek have higher BMI than sportsman Bartek, but lower than IT Bartek? "
      f"{super_weird_bartek() > super_bartek() < bartek()}")
