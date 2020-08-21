from __future__ import print_function
import math
import random
from math import pi

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

print(math.pi)

print(pi)

print(math.e)

print(math.tau)

print(math.inf)

print(math.nan)

"""
Random Module
Random Module allows us to create random numbers. We can even set a 
seed to produce the same random set every time.

The explanation of how a computer attempts to generate random numbers 
is beyond the scope of this course since it involves higher level 
mathmatics. But if you are interested in this topic check out:

https://en.wikipedia.org/wiki/Pseudorandom_number_generator
https://en.wikipedia.org/wiki/Random_seed
Understanding a seed
Setting a seed allows us to start from a seeded psuedorandom number 
generator, which means the same random numbers will show up in a 
series. Note, you need the seed to be in the same cell if your 
using jupyter to guarantee the same results each time. Getting a 
same set of random numbers can be important in situations where 
you will be trying different variations of functions and want to 
compare their performance on random values, but want to do it 
fairly (so you need the same set of random numbers each time).
"""
print("\nrandom.randint(0,1000)")
print("- - - - - - - - - - ")

print(random.randint(0,1000))

print("\nprint(random.randint(0,100))")
print("- - - - - - - - - - ")
random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

print("\nRandom with Sequences")
print("- - - - - - - - - - ")

mylist = list(range(0,20))

print(mylist)

print(random.choice(mylist))

print("\nShuffle a List")
print("- - - - - - - - - - ")
# Don't assign this to anything!
print(random.shuffle(mylist))
print(mylist)
