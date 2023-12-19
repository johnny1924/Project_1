class Dog:

    def __init__(self, name, color, age, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    def run(self):
        print(f'{self.name} is running...')

    def bark(self, sound):
        print(f'{self.name} is barking: {sound}')

    def age_in_years(self):
        return self.age // 7  # Assuming 1 human year is equivalent to 7 dog years

    def __str__(self):
        return f'Dog(name={self.name}, color={self.color}, age={self.age}, breed={self.breed})'

d1 = Dog('dummy', 'brown', 11, 'chow chow')
d2 = Dog('mike', 'brown', 9, 'dogo')

print(d1)
d1.run()
d2.run()
d1.bark('waffffff')
d2.bark('waaaaaf')

# Example of using age_in_years method
print(f"{d1.name} is {d1.age_in_years()} years old in human years.")
