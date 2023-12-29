class Shape:

    def __init__(self, parameter, area):
        self.parameter = parameter
        self.set_area(area)

    def get_area(self):
        return self.__area

    def set_area(self, new_value):
        if new_value > 0:
            self.__area = new_value

    def __str__(self):
        return f'area={self.__area}, parameter={self.parameter}'


answer1 = Shape('up', 15)

print(answer1.get_area())
answer1.set_area(28)
print(answer1)
