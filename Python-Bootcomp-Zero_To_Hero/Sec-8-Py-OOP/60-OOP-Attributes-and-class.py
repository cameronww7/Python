from __future__ import print_function

"""
 Prompt 60-OOP-Attributes-and-class
"""

print("60-OOP-Attributes-and-class")

"""
Object Oriented Programming
Object Oriented Programming (OOP) tends to be one of the major obstacles 
for beginners when they are first starting to learn Python.

There are many, many tutorials and lessons covering OOP so feel free to 
Google search other lessons, and I have also put some links to other 
useful tutorials online at the bottom of this Notebook.

For this lesson we will construct our knowledge of OOP in Python by 
building on the following topics:

Objects
Using the class keyword
Creating class attributes
Creating methods in a class
Learning about Inheritance
Learning about Polymorphism
Learning about Special Methods for classes

"""

print("\n60 - OOP - Attributes and Classes\n")
print("- - - - - - - - - - ")

lst = [1, 2, 3]
print(lst.count(2))


myset = set()

print(type(myset))

"""
Objects
In Python, everything is an object. Remember from previous lectures we 
can use type() to check the type of object something is:
"""
print("\n\nObjects")
print("- - - - - - - - - - ")

print(type(1))
print(type([]))
print(type(()))
print(type({}))

"""
class
User defined objects are created using the class keyword. The class is a 
blueprint that defines the nature of a future object. From classes we 
can construct instances. An instance is a specific object created from a 
particular class. For example, above we created the object lst which was 
an instance of a list object.

Let see how we can use class:
"""
print("\n\nClasses")
print("- - - - - - - - - - ")

# Create a new object type called Sample
class Sample():
    pass

# Instance of Sample
my_sample = Sample()

print(type(my_sample))


"""
Attributes
The syntax for creating an attribute is:

self.attribute = something

There is a special method called:

__init__()

This method is used to initialize the attributes of an object. For example:
"""
print("\n\nAttributes")
print("- - - - - - - - - - ")


class Dog:
    # Attributes
    # We take in the argument
    # Assign it using self.attribute_name
    def __init__(self, breed, name, spots): # is a constructor
        self.breed = breed
        self.name = name

        # Boolean Value
        self.spots = spots


#sam = Dog() # will cause an error

sam = Dog(breed='Lab', name="sam", spots=False)
frank = Dog(breed='Huskie', name="frank", spots=True)


print(sam)
print(frank.breed)
