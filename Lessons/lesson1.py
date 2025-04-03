class Person:

    def __init__(self, name,age,city):
        #atriuty
        self.name = name,
        self.age = age,
        self.city = city,

    def introduce(self):
        print(f'Hi my name is {self.name} ')


#class object/example Person
diana = Person('diana', 26, 'bishkek')
print(diana.name)
print(diana.age)
print(diana.city)
diana.introduce()