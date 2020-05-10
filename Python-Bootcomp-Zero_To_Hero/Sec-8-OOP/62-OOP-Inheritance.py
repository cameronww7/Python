from __future__ import print_function

"""
 Prompt 62-OOP-Inheritance
"""

print("62-OOP-Inheritance")

"""
Inheritance
Inheritance is a way to form new classes using classes that have already been defined. 
The newly formed classes are called derived classes, the classes that we derive from 
are called base classes. Important benefits of inheritance are code reuse and reduction 
of complexity of a program. The derived classes (descendants) override or extend the 
functionality of base classes (ancestors).

"""

print("\n62-OOP-Inheritance\n")
print("- - - - - - - - - - ")

#Let's see an example by incorporating our previous work on the Dog class:


class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")
