from __future__ import print_function

"""
 Prompt 100-Generators
"""

print("100-Generators")

"""
Iterators and Generators
In this section of the course we will be learning the difference 
between iteration and generation in Python and how to construct 
our own Generators with the yield statement. Generators allow us 
to generate as we go along, instead of holding everything in 
memory.

We've touched on this topic in the past when discussing certain 
built-in Python functions like range(), map() and filter().

Let's explore a little deeper. We've learned how to create 
functions with def and the return statement. Generator functions 
allow us to write a function that can send back a value and 
then later resume to pick up where it left off. This type of 
function is a generator in Python, allowing us to generate a 
sequence of values over time. The main difference in syntax 
will be the use of a yield statement.

In most aspects, a generator function will appear very similar 
to a normal function. The main difference is when a generator 
function is compiled they become an object that supports an 
iteration protocol. That means when they are called in your 
code they don't actually return a value and then exit. Instead, 
generator functions will automatically suspend and resume their 
execution and state around the last point of value generation. 
The main advantage here is that instead of having to compute an 
entire series of values up front, the generator computes one 
value and then suspends its activity awaiting the next 
instruction. This feature is known as state suspension.

￼￼To start getting a better understanding of generators, 
let's go ahead and see how we can create some.
"""

print("\n100-Generators")
print("- - - - - - - - - - ")

# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

print("\ngencubes")
print("- - - - - - - - - - ")
for x in gencubes(10):
    print(x)


def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


print("\ngenfibon")
print("- - - - - - - - - - ")
for num in genfibon(10):
    print(num)


def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b

    return output


print("\nsimple_gen")
print("- - - - - - - - - - ")
def simple_gen():
    for x in range(3):
        yield x

# Assign simple_gen
g = simple_gen()


print(next(g))
print(next(g))
print(next(g))



print("\niterator")
print("- - - - - - - - - - ")
s = 'hello'

#Iterate over string
for let in s:
    print(let)


#next(s)

s_iter = iter(s)


print("\niterator 2")
print("- - - - - - - - - - ")
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
