# coffee = ['black', 'turkish', 'latte', 'instant']
#
# for c in coffee:
#     length = len(c)
#     new_c = c.title()
#     print(f'[{new_c}] coffee price is: {length} ')



# for i in range(0, 1000, 7):
#     print(i)
#
# print(list(range(0, 1000, 7)))




# ==============================while=============================

# while condition:

# while True:
#     print('hello')
# print all the numbers between 0-9
# x = 0
#
# while x < 10:
#     print(x)
#     x += 1


# changin the var must be logical

# x = 0
#
# while x < 10:
#     print(x)
#     x -= 1

# import datetime
# import time
#
# while datetime.datetime.now().minute < 30: # if time is under 30 count seconds
#     print(datetime.datetime.now().second)
#     time.sleep(1)

# while True:
#     print('Reply from 1.1.1.1: bytes=32 time=7ms TTL=59')


# ask the user to enter his PIN code untill the right guess
# the Pin contains 3 digit

# guess = input('enter your pin code : ')
# pin = '321'
# while guess != '321':
#     if guess == pin:
#         break
#         print('wrong idiot')
#     guess = input('enter your PIN code : ')
#
# print('Wolecome Boss')
#
# while True:
#     guess = input('enter your PIN code : ')
#     result = True if guess == pin else False if len(guess) != len(pin) else "none"
#     print(result)



