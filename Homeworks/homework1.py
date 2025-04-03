class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP
    def introduce(self):
        print(f'Hi, my name is {self.name},my lvl is {self.lvl} and HP is {self.HP}')

    def is_adult(self):
        return self.lvl >= 10
hero1 =Hero('Naruto', 100, 1200)
hero2 = Hero('Saske', 100, 800)
hero3 = Hero('Sakura', 9,3000)
hero1.introduce()
print(f'Is {hero1.name} adult?{hero1.is_adult()}')
print(f'is {hero2.name} adult? {hero2.is_adult()}')
print(f'is {hero3.name} adult? {hero3.is_adult()}')