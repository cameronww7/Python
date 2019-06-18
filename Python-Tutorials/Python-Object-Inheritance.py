from __future__ import print_function
import math

# Python Object Inheritance
print("Python Object Inheritance")


class Shape(object):
    def __init__(self):
        self.color = "Red"
        self.sides = 0

    def calcArea(self):
        return 0


class Quadrilateral(Shape):
    def __init__(self, w, l, c):
        self.sides = 4
        self.width = w
        self.length = l
        self.color = c

    def calcArea(self):
        return self.width * self.length


class Square(Quadrilateral):
    def __init__(self, w, c):
        super(Square, self).__init__(w, w, c)


class Circle(Shape):
    def __init__(self, r, c):
        super(Circle, self).__init__()
        self.radius = r
        self.color = c

    def calcArea(self):
        return math.pi * (self.radius ** 2)


class Triangle(Shape):
    def __init__(self, s1, s2, s3, c):
        Shape.__init__(self)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.color = c


def printArea(s):
    print(s.calcArea())


sq1 = Square(5, "Blue")
sq2 = Square(9, "Green")

circle1 = Circle(10, "Orange")
t1 = Triangle(2, 3, 4, "Purple")

print("Square Sizes:", sq1.width, "x", sq1.sides, sq1.color,
      ",", sq2.width, "x", sq2.sides, sq2.color)
print("Circle:", circle1.radius, circle1.color)

printArea(sq1)
