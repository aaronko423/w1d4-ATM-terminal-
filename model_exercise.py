#! usr/bin/env python3

from mappers_exercises import Database

class User:

    def __init__(self, first_name, last_name, account_number, password, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit_money(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw_money(self, withdrawal_amount):
        self.balance -= withdrawal_amount

if __name__ == "__main__":
    User2 = User("FN", "LN", 123, 123, 123)
    User2.account_number = 234
    print(User2.account_number)
