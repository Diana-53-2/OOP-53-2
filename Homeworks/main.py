import random
from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.__random_int = None
    def attack(self):
        print(f'{self.name} attacking!')
    def protection(self):
        print(f'{self.name} protection!')
    def rest(self):
        print(f'{self.name} resting !')


    def _generate_random_int(self):
        self.__random_int = random.randint(1, 3)

    def get_random_int(self):
        if self.__random_int is None:
            self._generate_random_int()
        return self.__random_int
    @abstractmethod
    def unique_scream(self):
        pass
    def unique_attach(self):
        pass
    def unique_action(self):
        pass