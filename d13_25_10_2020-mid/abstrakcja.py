from abc import ABC, abstractmethod


class Animal(ABC):
    # tutaj zaimplementuj asbtrakcyjna metodę make_sound
    def __init__(self, weight):
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def live(self):
        self.move()
        self.make_sound()


class Dog(Animal):
    @staticmethod
    def _bark():
        print("Hau hau!")

    @staticmethod
    def make_sound():
        Dog._bark()

    @staticmethod
    def move():
        print("Ide sobie, ide.")


dog = Dog(48)
dog.make_sound()
# dog.live()
