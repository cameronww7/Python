from __future__ import print_function

"""
 Prompt 43-Py-args-and-kwards.py
"""

print("43-Py-args-and-kwards.py")

"""
Purpose:

The purpose of this document is to play with *args and **kwargs to gain a better understanding.
"""


def ex1(xVar1, xVar2):
    #Returns 5% of the usme of a and b
    return(sum((xVar1,xVar2))) * 0.05


print(ex1(5,1))


def ex2(xVar1, xVar2, xVar3=0, xVar4=0, xVar5=10):
    #Returns 5% of the usme of a and b
    return(sum((xVar1,xVar2,xVar3,xVar5,xVar4))) * 0.05


print(ex2(5,1))


def ex3(*args):
    #Demosrate the power of Args
    return sum(args) * 0.05


print(ex3(5,34,6,6,3,73,3))


def ex4(*spam):
    #This is an example of using args but the name doesnt matter, should always still use args
    return sum(spam) * 0.05


print(ex4(5,34,6,6,3,73,3))


def ex5(*args):
    #Demosrate you can loop through them easily
    for index in args:
        print(index)


ex5(1,2,3,4,5,6,8)


def ex6(**kwargs):
    #test out kwargs
    if 'fruit' in kwargs:
        print("My fruit of choise is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit in here")

ex6(fruit='appple', veg="brussel", pizza='is the best')
ex6(veg="brussel", pizza='is the best')


def ex7(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs['food']))

ex7(10,20,30, fruit='orange',food='eggs')


