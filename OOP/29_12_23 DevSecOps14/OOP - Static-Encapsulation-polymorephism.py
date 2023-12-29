class BankAccount:
    def __init__(self, name, password, account_id, balance, credit_score):
        self.name = name
        self.password = password
        self.account_id = account_id
        self.__balance = balance  # private
        self._credit_score = credit_score  # protected member _pre

    def get_balance(self):
        return self.__balance * 2.9

    def set_balance(self, new_value):
        if new_value > 0:
            self.__balance = new_value

    def __str__(self):
        return f"Account({self.name}, {self.account_id}, Balance: {self.get_balance()}, Credit Score: {self._credit_score})"


acc1 = BankAccount('johnny', 1234, 1234432, 190, 10)

print(acc1)
print(acc1.get_balance())
print(acc1._credit_score)  # internal use

# Update balance using the set_balance method
acc1.set_balance(50)
print(acc1.get_balance())

# Note: Directly accessing __balance will raise an AttributeError
# Uncommenting the line below will result in an error
# print(acc1.__balance)



