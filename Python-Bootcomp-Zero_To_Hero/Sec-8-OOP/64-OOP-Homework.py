
from __future__ import print_function
import math

"""
 Prompt 64-OOP-Homework
"""

print("64-OOP-Homework")

"""


"""

print("\n64-OOP-Homework\n")
print("- - - - - - - - - - ")


"""
Problem 1
Fill in the Line class methods to accept coordinates as a pair 
of tuples and return the slope and distance of the line.
"""


class Line:

    def __init__(self, xCoor1, xCoor2):
        self.corr1 = xCoor1
        self.corr2 = xCoor2

    def distance(self):
        # Get Distance Formula
        # https://www.chilimath.com/lessons/intermediate-algebra/distance-formula/
        return ((self.corr2[0] - self.corr1[0])**2 + (self.corr2[1] - self.corr1[1])**2)**.5

    def slope(self):
        # Need Slope Formula
        # https://calcworkshop.com/graphing-linear-equations/slope-formula/?PageSpeed=noscript
        return (self.corr2[1] - self.corr1[1]) / (self.corr2[0] - self.corr1[0])


# EXAMPLE OUTPUT

coordinate1 = (3, 2)
coordinate2 = (8, 10)

print("\nCreating Line Object")
li = Line(coordinate1, coordinate2)

print("\nGetting Distance of Line Object")
print(li.distance())

print("\nGetting Slope of Line Object")
print(li.slope())

"""
Problem 2
Fill in the class
"""


class Cylinder:

    def __init__(self, xHeight = 1, xRadius = 1):
        self.height = xHeight
        self.radius = xRadius

    def volume(self):
        # Get Volume of a Cylinder
        # https://www.mathopenref.com/cylindervolume.html
        pass

    def surface_area(self):
        # Get the Surface Area of a Cylinder
        # https://www.w3resource.com/python-exercises/math/python-math-exercise-5.php
        pass


# EXAMPLE OUTPUT

print("\nCreating Cylinder Object")
c = Cylinder(2, 3)

print("\nGetting Volume of Cylinder Object")
c.volume()

print("\nGetting Surface Area of Cylinder Object")
c.surface_area()
