from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "gav"
    def move(self):
        return "go"

dog = Dog()
print(dog.make_sound())
print(dog.move())

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y