# class Person:
#     #data
#     gender = 'female'
#     age = 20
#     skin_color = 'navy'
#     weight = 93.1
#     name = 'brit'
#     #func
#
#
#
#
#
# p1 = Person()
# p2 = Person()


#
# # print(type(f))
# # print(type(p))
# print(p1.name)
# print(p2.name)

# p1.title = 'dr'
# p2.title = 'biatch'
#
# print(p1.title)
# print(p2.title)

# del p1.name # del p1 name
# print(p1.name)

# class Person:
#     # data
#     def __init__(self, name, gender, age, skin_color):  # magic function # self -> jumps between data (public)
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.skin_color = skin_color
#
#     #     p4.name = name
#     #     p4.gender = gender
#     #     # print(f'God good self = {self}')
#     #
#     # # gender = 'female'
#     # # age = 20
#     # # skin_color = 'navy'
#     # # weight = 93.1
#     # # name = 'brit'
#     # #func
#
#
# # p3 = Person('johnny', 'male', 11, 'black')  # class name ()
# # p4 = Person('koki', 'female', 22, 'brown')
#
#
# # p5 = Person('mike', 'male', 35, 'white')
# # p6 = Person('abe', 'male', 37, 'white')
#
# def __str__(self):
#     return f'the object name is {self.name}'
#
#
# def __int__(self):
#     return self.age
#
#
# def __float__(self):
#     return float(self.age)
#
#
# def __len__(self):
#     return len(self.__dict__.keys())  # number of var or attributes
#
#
# def __add__(self, other):
#     return self.name + other.name
#
#
# def __gt__(self, other):
#     return self.age > other.age
#
#
# def __le__(self, other):
#     return self.age < other.age
#
# p3 = Person('johnny', 'male', 11, 'black')  # class name ()
# p4 = Person('koki', 'female', 22, 'brown')
# p4.k = 11
#
# # p3.__dict__ = {'username' : 'go'} # change the structure of the object
# # print(p3.__dict__) # it's the way to extract a dict of attributes and their values
# # print(p4.__dict__)
# # print(p5.__dict__)
# # print(p6.__dict__)
# #
#
# print(p3)

# print(p3)
# print(p4)
class Person:
    # data
    def __init__(self, name, gender, age, skin_color):
        self.name = name
        self.gender = gender
        self.age = age
        self.skin_color = skin_color

    def __str__(self):
        return f'the object name is {self.name}'

    def __int__(self):
        return self.age

    def __float__(self):
        return float(self.age)

    def __len__(self):
        return len(self.__dict__.keys())  # number of var or attributes

    def __add__(self, other):
        return self.name + other.name

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age < other.age

p3 = Person('johnny', 'male', 11, 'black')  # class name ()
p4 = Person('koki', 'female', 22, 'brown')
p4.k = 11

print(p3)
print(p3 > p4)
print(p3 < p4)
print(p3 >= p4)
#