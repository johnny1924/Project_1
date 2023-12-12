# for i in range(1, 10):
    # for j in range(i):
        # print(i, end="")
    # print(i)
# in class
# for row in range(1,10):
#     for col in range(1, row):
#         print(row, end='')
#         print()
#==========palindrome=================

# def is_palindrome(input_str):
#     cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
#     return cleaned_str == cleaned_str[::-1]
# user_input = input("Enter a string: ")
# if is_palindrome(user_input):
#     print("It is a palindrome!")
# else:
#     print("It is not a palindrome.")

#========FIbonacci============

# a = 0
# b = 1
# counter = 0
# while True:
    # z = a+b
   # print(z)
   # a = b
   # b = z
   # counter += 1
   # if counter ==20:
     #   break


# for number in range(1,100):
#     is_prime = True
#     for dividers in range(2,number):
#         if number % dividers == 0:
#             is_prime=False
#             break
#     if is_prime:
#         print(number)
# strings = ['abd', 'xyz', 'aba', '12331']

# c = 0

# for s in strings:
   # if len(s) > 2 and s[0] == s[-1]:
       # c += 1
# print(c)

# strings = list(set(strings))

