class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def action(self):
        print(f'{self.name} совершает действие')
    def attack(self):
        print(f'{self.name} атакует')
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
        if self.arrows <= 0:
            print(f'{self.name} закончились стрелы!')
            return
        self.arrows -= 1
        if self.precision <= 0.5:
            print(f'{self.name} выпустил стрелу и попал в цель. Осталось: {self.arrows}')
        else:
            print(f'{self.name} промахнулся. Осталось: {self.arrows}')
    def rest(self):
        self.arrows += 5
        print(f'{self.name} пополнил запас стрел(+5). Осталось: {self.arrows}')
    def status(self):
        return f'{self.name}, hp: {self.hp},стрелы :{self.arrows},точность: {int(self.precision * 100)}%'
archer = Archer('Fuu', 15,10, 0.7)
archer.attack()
archer.action()
archer.attack()
archer.rest()
print(archer.status())
