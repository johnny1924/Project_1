# 1
# class Example:
#     x = 1
#     y = 2
#
#
# e1 = Example()
# print(e1.x)

# 2

# class Cookie:
#     def __init__(self, sugar, kind='ch chips'):
#         self.sugar = sugar
#         self.kind = kind
#
#     def __str__(self):
#         return self.kind
#
#     def __repr__(self):
#         return f'Cookie({self.sugar}, \'{self.kind}\')'
#
#     def __eq__(self, other):
#         return other.sugar == self.sugar
#
#     def __add__(self, other):
#         return self.sugar + other.sugar
#
#
# happy_cookies = Cookie(190, 'weed cookies')
# happy_cookies2 = Cookie(1)
#
# print(happy_cookies)
# print(happy_cookies2)
# print(happy_cookies.__repr__())
# print(happy_cookies != happy_cookies2)
# print(happy_cookies + happy_cookies2)


# class BankAccount:
#     def __init__(self, account_id, first_name, last_name, balance):
#         self.account_id = account_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.balance = balance
#
#     class BankAccount:
#         def __init__(self, account_id, first_name, last_name, balance):
#             self.account_id = account_id
#             self.first_name = first_name
#             self.last_name = last_name
#             self.balance = balance
#
#         def __str__(self):
#             results = ''
#             for k, v in self.__dict__.items():
#                 results = results + f'{k} => {v}, '
#             return results[:-2]
#
#         def __eq__(self, other):
#             return self.balance == other.balance
#
#         def __add__(self, other):
#             if isinstance(other, BankAccount):
#                 return BankAccount(
#                     account_id=self.account_id,
#                     first_name=self.first_name,
#                     last_name=self.last_name,
#                     balance=self.balance + other.balance
#                 )
#             else:
#                 raise TypeError("Unsupported operand type. You can only add two BankAccount instances.")
#
#     acc1 = BankAccount(1, 'neora', 'sharon', 5000)
#     acc2 = BankAccount(2, 'johnny', 'halevi', 123412)
#
#     print(acc1)
#     print(acc2)
#     print(f'Is acc1 == acc2 -> {acc2 == acc1}')
#     print(f'Sum of acc1 and acc2 -> {acc2 + acc1}')
