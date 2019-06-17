from __future__ import print_function
import math, random

# Python OOP 1
print("Python OPP 1")


# def calcCircumference(radius):
# 	return math.pi * 2 * radius
#
# class Circle:
# 	pass
#
# circle1 = Circle()
#
# circle1.radius = 4.2
#
# print(circle1.radius)
#
# circle2 = Circle()
# circle2.radius = 3.9
# print(circle2.radius)


# def calcCircumference(radius):
#     return math.pi * 2 * radius
#
#
# class Circle:
#     pass
#
#
# circles = []
#
# for i in range(0, 10):
#     c = Circle()
#     c.radius = random.uniform(1.1, 9.5)
#     c.circumference = calcCircumference(c.radius)
#     circles.append(c)
#
# for c in circles:
#     print("Radius:", c.radius, \
#           "circumference:", c.circumference)

class Circle:
    def __init__(self, radius):
        if radius == 0:
            self.radius = random.uniform(1.1, 9.5)
        else:
            self.radius = radius

    def calcCircumference(self):
        return math.pi * 2 * self.radius

    def calcDiameter(self):
        return self.radius * 2

    def calcArea(self):
        return math.pi * (self.radius ** 2)


circles = []

for i in range(0, 10):
    c = Circle(5.5)
    circles.append(c)

for c in circles:
    print("Radius:", c.radius, \
          "circumference:", c.calcCircumference(), \
          "Diameter:", c.calcDiameter(), \
          "Area:", c.calcArea())
