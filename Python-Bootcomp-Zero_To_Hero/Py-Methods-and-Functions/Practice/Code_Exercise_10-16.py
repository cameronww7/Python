from __future__ import print_function

"""
 Prompt Code_Exercise_10-16.py
"""

print("Code_Exercise_10-16.py")

"""
Purpose:

The purpose of this file is to go through the coding exercise and knock them out one by one!

So, here we go!
"""


# Write a function that will output hello world
def ex1():
    print("Hello World!!")


ex1()


# Define a function that names a name in and prints hello, name
def ex2(xName, xMethod):
    if xMethod == 1:
        print("Hello " + xName)
    else:
        print("Hello {}".format(xName))


ex2("FOO BAR", 0)
ex2("FOO BAR", 1)


# define a function that takes in a boolean value. If true return hello, and if false return goodbye
def ex3(xBoolean):
    if xBoolean == True:
        print("Hello")
    elif xBoolean == False:
        print("Goodbye")


ex3(False)


# Define a function that takes in three arguemnts and if z is true return x, if z is false return y
def ex4(xVarX, xVarY, xVarZ):
    if xVarZ == True:
        return xVarX
    elif xVarZ == False:
        return xVarY


print(ex4(True, True, False))


# Define a function that takes in two arguments and returns their sum
def ex5(xVar1, xVar2):
    return xVar1 + xVar2


print(ex5(5, 5))


# Define a function that takes in on variable and returns true if the value is even and false if odd
def ex6(xVar):
    if (xVar % 2) == 0:
        return True
    else:
        return False


print(ex6(5))

# Define a function that takes in two variables and returns true if the first is greater than the second
def ex7(xVar1, xVar2):
    if xVar1 > xVar2:
        return True
    else:
        return False

print(ex7(5,3))
