
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
    pass


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))

print(acct1.withdraw(75))

# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))
