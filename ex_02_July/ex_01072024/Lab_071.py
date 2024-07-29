# Abstraction
# Hiding the details and showing what is required

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "bow bow"


class Cat(Animal):
    def sound(self):
        return "Meow"


dog = Dog("Rencho")
print(dog.sound())

cat = Cat("julie")
print(cat.sound())
