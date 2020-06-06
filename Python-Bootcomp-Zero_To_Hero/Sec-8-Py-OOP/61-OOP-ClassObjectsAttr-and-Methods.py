from __future__ import print_function

"""
 Prompt 61-OOP-ClassObjectsAttr-and-Methods
"""

print("61-OOP-ClassObjectsAttr-and-Methods")

"""
Object Oriented Programming
"""

print("\n61-OOP-ClassObjectsAttr-and-Methods\n")
print("- - - - - - - - - - ")


class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"

    # Attributes
    # We take in the argument
    # Assign it using self.attribute_name
    def __init__(self, breed, name): # is a constructor
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print("WOOF! \n I am {} wooffffff".format(self.name))
        print("WOOF! {}".format(number))

#sam = Dog() # will cause an error

myDog = Dog(breed='Lab', name="Groot")

myDog.bark(9)


"""
Methods
Methods are functions defined inside the body of a class. They are used to 
perform operations with the attributes of our objects. Methods are a key 
concept of the OOP paradigm. They are essential to dividing responsibilities
in programming, especially in large applications.

You can basically think of methods as functions acting on an Object that 
take the Object itself into account through its self argument.

Let's go through an example of creating a Circle class:
"""


print("\nNext Example - Circle")
print("- - - - - - - - - - ")


class Circle:
    # CLASSS OBJECT ATTRIBUTE
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        # Circle.pi can be self.pi but you can call it Circle.pi
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def set_radius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def get_circumference(self):
        return self.radius * self.pi * 2


c = Circle(30)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.get_circumference())

