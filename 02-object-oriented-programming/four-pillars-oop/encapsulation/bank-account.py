# Enacapsulation
# Encapsulation is about bundling and methods that work on the data within a single
# unit (the class) and restricting access to some of the object's components.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(Self):
        return Self.__balance
