class Animal:
    def __init__(self, name=''):
        self.name = name

    def eat(self):
        print('eating...')

class Cat(Animal):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def walk(self):
        print('walking...')


class Fish(Animal):
    def swim(self):
        print('swimming...')

    def eat(self):
        print('eating lasagna')

animal1 = Animal()
nemo = Fish()
garfield = Cat(animal1.name)

animal1.eat()
nemo.eat()
garfield.eat()

an2 = Animal('mike')
print(an2.name)
