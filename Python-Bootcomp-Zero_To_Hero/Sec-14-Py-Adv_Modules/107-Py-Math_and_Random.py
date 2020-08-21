from __future__ import print_function
import math
import random

"""
 Prompt 107-Py-Math_and_Random
"""

print("107-Py-Math_and_Random")

"""
Math and Random Modules
Python comes with a built in math module and random module. In this lecture we will 
give a brief tour of their capabilities. Usually you can simply look up the function 
call you are looking for in the online documentation.

Math Module
https://docs.python.org/3/library/math.html

Random Module
https://docs.python.org/3/library/random.html

We won't go through every function available in these modules since there are so many, 
but we will show some useful ones.
"""
print("\nhelp(math)")
print("- - - - - - - - - - ")
print(help(math))


print("\nPlaying with Math")
print("- - - - - - - - - - ")

value = 5.4322432

print(math.floor(value))

print(math.ceil(value))

print(round(value))

