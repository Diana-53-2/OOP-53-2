from main import Hero
class Jester(Hero):
    def unique_attack(self):
        print(f'{self.name} crazy attack')
    def unique_scream(self):
        print(f'{self.name} screaming "OAOAOAOAOOA!"')
    def unique_action(self):
        number = self.get_random_int()
        print (f'{self.name} action {number}')
        if number == 1:
            self.attack()
        elif number == 2:
            self.protection()
        elif number == 3:
            self.rest()


hero1 = Jester(name='Naruto', health=100)
hero1.unique_attack()
hero1.unique_scream()
hero1.unique_action()


