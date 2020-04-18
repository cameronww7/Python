from __future__ import print_function

"""
 Prompt Code_Exercise_17-19.py
"""

print("Code_Exercise_17-19.py")

"""
Purpose:

The purpose of this file is to go through the coding exercise and knock them out one by one!

So, here we go!
"""


def ex17(*args):
    #Define a function that will take in an arbitrary number of arguments and retuns the sum
    return sum(args)

print(ex17(5,32,34,235,2345,234,23,423))


def ex18(*args):
    #Define a function that takes in an arbitrary number of arguments
    # and returns a list containing only even arguments
    myList = []

    for index in args:
        if (index%2) == 0:
            myList.append(index)

    return myList

print(ex18(2,4,6,7,8,9))


def ex19(xVar):
    # define a function that takes in a string, and returns a matching string
    # where every even letter is uppercase and every odd letter is lowercase.
    # Assume string is letters only
    tempStr = ""
    lenth = len(xVar)
    for index in range(lenth):
        if (index%2) == 0:
            tempStr = tempStr + xVar[index].upper()
        else:
            tempStr = tempStr + xVar[index].lower()

    return tempStr

print(ex19("AAAAAAAAAAAAAAAAAAAAA"))
