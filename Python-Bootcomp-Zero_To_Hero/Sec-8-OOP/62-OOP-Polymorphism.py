from __future__ import print_function

"""
 Prompt 62-OOP-Polymorphism
"""

print("62-OOP-Polymorphism")

"""
We've learned that while functions can take in different arguments, 
methods belong to the objects they act on. In Python, polymorphism 
refers to the way in which different object classes can share the 
same method name, and those methods can be called from the same 
place even though a variety of different objects might be passed 
in. The best way to explain this is by example:
"""

print("\n62-OOP-Polymorphism\n")
print("- - - - - - - - - - ")

# Let's see an example by incorporating our previous work on the Dog class:


class Animal:
    # this is our Base class and other classes will inheritant this class
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("I am a Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self, myName):
        Animal.__init__(self)
        self.name = myName
        print("Dog created")

    def whoAmI(self):
        print("I am a Dog")

    def eat(self):
        print("I am a Dog Eating")

    def speak(self):
        print("Woof!")


class Cat:
    def __init__(self, myName):
        self.name = myName

    def speak(self):
        return self.name+' says Meow!'


print("\nCreating Animal")
myanimal = Animal()
myanimal.whoAmI()

print("\nCreating Dog Class")
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.speak()

print("\nCreating Dog Class")
niko = Dog('Niko')
print(niko.speak())

print("\nCreating Cat Class")
felix = Cat('Felix')
print(felix.speak())
