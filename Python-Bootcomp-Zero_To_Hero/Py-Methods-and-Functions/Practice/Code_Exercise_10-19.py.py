from __future__ import print_function

"""
 Prompt Code_Exercise_10-19.py
"""

print("Code_Exercise_10-19.py")

"""
Purpose:

The purpose of this file is to go through the coding exercise and knock them out one by one!

So, here we go!
"""

#Write a function that will output hello world
def ex1():
    print("Hello World!!")


ex1()


#Define a function that names a name in and prints hello, name
def ex2(xName, xMethod):
    if xMethod == 1:
        print("Hello " + xName)
    else:
        print("Hello {}".format(xName))


ex2("FOO BAR", 0)
ex2("FOO BAR", 1)


#define a function that takes in a boolean value. If true return hello, and if false return goodbye
def ex3(xBoolean):
    if xBoolean == True:
        print("Hello")
    elif xBoolean == False:
        print("Goodbye")


ex3(False)


#Define a function that takes in three arguemnts and if z is true return x, if z is false return y
def ex4(xVarX, xVarY, xVarZ):
    if xVarZ == True:
        return xVarX
    elif xVarZ == False:
        return xVarY

print(ex4(True, True, False))
