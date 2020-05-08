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
    # Attributes
    # We take in the argument
    # Assign it using self.attribute_name
    def __init__(self, breed, name, spots): # is a constructor
        self.breed = breed
        self.name = name

        # Boolean Value
        self.spots = spots


#sam = Dog() # will cause an error

myDog = Dog(breed='Lab', name="sam", spots=False)

print(myDog)

