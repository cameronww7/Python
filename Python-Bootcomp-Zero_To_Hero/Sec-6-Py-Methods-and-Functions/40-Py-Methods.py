from __future__ import print_function

"""
 Prompt 40-Py-Methods.py
"""

print("40-Py-Methods.py")

"""
Methods
We've already seen a few example of methods when learning about Object and 
Data Structure Types in Python. Methods are essentially functions built 
into objects. Later on in the course we will learn about how to create our 
own objects and methods using Object Oriented Programming (OOP) and classes.

Methods perform specific actions on an object and can also take arguments, 
just like a function. This lecture will serve as just a brief introduction 
to methods and get you thinking about overall design methods that we will 
touch back upon when we reach OOP in the course.

Methods are in the form:

object.method(arg1,arg2,etc...)

You'll later see that we can think of methods as having an argument 'self' 
referring to the object itself. You can't see this argument but we will be 
using it later on in the course during the OOP lectures.

Let's take a quick look at what an example of the various methods a list has:
"""

# Create a simple list
lst = [1, 2, 3, 4, 5]

print(lst)

lst.append(6)

print(lst)

# Check how many times 2 shows up in the list
lst.count(2)

help(lst.count)
