# CTRL and click the word - builtins
# def <function_name>():

# def greet(name):
#     # function block
#     print(f'hello {name}')
#
#
# # greet('johnny')
# # greet('mikey')
# #
# # x = 'johnny'
# # greet(x)
# def greet_with_age(name: str, age):
#     print(f'my name is{name}, and im {age} years old')
#
# greet_with_age( 'johnny' , 34)
# greet_with_age( 'typhoon' , 35)
# greet_with_age( 44 , 35)

# def arg_print(a,b,c,d,e='sleeping'):
#     print(f'a={a}')
#     print(f'b={b}')
#     print(f'c={c}')
#     print(f'd={d}')
#     print(f'e={e}')
#
# #
# # arg_print(1,2, 3, 4,)
#
# arg_print(1,2,3,4)

#========================*args=========================
# def odd_sum(*args):
#     for n in args:
#         print(n if n % 2 == 1 else 'naaaaaaaah')
#
#
# odd_sum(1,2,3,4,5)
# odd_sum(1,2,3,4,5,6,7,8,9)

#========================**kwargs=====================


# def foo(**kwargs):
#     print(kwargs)
#
# foo(x=4, reverse = True, color='johnny')

# def (*args):
#     sum = 0
#     for n in args:
#         if n % 2==1:
#             sum += n
#     print(sum)
#
# odds(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)


# def my_sum(*args, **kwargs):
   # '''
    #    print the sum of the even numbers in default
    #   by sending the flag odd we sum the odd numbers
   # '''
    # print(args)
    # print(kwargs)
    # sum = 0
    # x = 1
    # if kwargs.get('sum'):
        # x = 1
    # for n in args:
        # if n % 2==1:
            # sum += n
    # print(sum)
# [].sort()
# odds(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# even(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

# my_sum(1, 2, 3, 4, 5, 6, 7, odd=True)
# my_sum(1, 2, 3, 4, 5, 6, 7, te=1)

# define a function in python to calc the area of triangle
# the function must receive from the user 2 arguments base and height
# the function must return the area

# def calc_area(b,h):
    # area = b * h / 2
    # print(area)
    # return area

# area = calc_area(1, 2)
# area2 = calc_area(42, 2)
# area3 = calc_area(551, 2)
# print(max(area, area2, area3))
