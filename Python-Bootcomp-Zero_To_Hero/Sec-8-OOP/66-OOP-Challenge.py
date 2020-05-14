
from __future__ import print_function
import math

"""
 Prompt 66-OOP-Challenge
"""

print("66-OOP-Challenge")

"""

Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to 
make sure the account can't be overdrawn.
"""

print("\n66-OOP-Challenge\n")
print("- - - - - - - - - - ")


class Account:
    def __init__(self, xName, xBalance):
        self.name = xName
        self.curBalance = xBalance

    def owner(self):
        print("The Account Holder Name is : {}".format(self.name))
        return self.name

    def balance(self):
        print("Your Current Balance is : {}".format(self.curBalance))
        return self.curBalance

    def deposit(self, xDepositAmount):
        print("Processing Deposit of {}".format(xDepositAmount))
        self.curBalance = self.curBalance + xDepositAmount
        print("Deposit Accepted, Your new Balance is : {}".format(self.curBalance))
        return True

    def withdraw(self, xWithdrawAmount):
        print("Processing Withdraw of {}".format(xWithdrawAmount))
        if xWithdrawAmount > self.curBalance:
            print("Error : Do not have enough Balance")
            return False
        else:
            self.curBalance = self.curBalance - xWithdrawAmount
            print("Withdraw Accepted, Your new Balance is : {}".format(self.curBalance))
            return True

# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print("\n# 2. Print the object")
print(acct1)

# 3. Show the account owner attribute
print("\n# 3. Show the account owner attribute")
print(acct1.owner())

# 4. Show the account balance attribute
print("\n# 4. Show the account balance attribute")
print(acct1.balance())

# 5. Make a deposit
print("\n# 5. Make a deposit")
print(acct1.deposit(50))

# 6. Make a withdrawal
print("\n# 6. Make a withdrawal")
print(acct1.withdraw(75))

# 7. Make a withdrawal that exceeds the available balance
print("\n# 7. Make a withdrawal that exceeds the available balance")
print(acct1.withdraw(500))
