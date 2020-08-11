from __future__ import print_function

"""
 Prompt 98-Decorators
"""

print("98-Decorators")

"""

Decorators
Decorators can be thought of as functions which modify the 
functionality of another function. They help to make your 
code shorter and more "Pythonic".

To properly explain decorators we will slowly build up from 
functions. Make sure to run every cell in this Notebook for 
this lecture to look the same on your own computer.

So let's break down the steps:
"""

print("\n98-Decorators")
print("- - - - - - - - - - ")

def func():
    return 1

print(func())

greet = func()

print(greet)


def hello(name="Sam"):
    print('The Hello() function has ran')

    def greet():
        return "\t this is the greet () func inside hello!"

    def welcome():
        return "\t This is welcome() inside Hello"

    print("I am going to return a function")

    if name == "Sam":
        return greet()
    else:
        return welcome()


someFunc = hello()

print(someFunc)


def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
