from __future__ import print_function
import random

"""
 Prompt 101-Generators-HW
"""

print("101-Generators-HW")

"""

"""

print("\n101-Generators-HW")

def Problem_One():
    """
    Problem 1
    Create a generator that generates the squares of numbers up to some number N.
    """
    print("\nProblem_One")
    print("- - - - - - - - - - ")

    def gensquares(N):
        for x in range(N):
            yield x**2

    for x in gensquares(10):
        print(x)

#Problem_One()


def Problem_Two():
    """
    Problem 2
    Create a generator that yields "n" random numbers between a low and high number
    (that are inputs).
    Note: Use the random library. For example:
    """
    print("\nProblem_Two")
    print("- - - - - - - - - - ")

    def rand_num(low, high, n):
        for x in range(n):
            yield random.randint(low, high)

    for num in rand_num(1, 10, 12):
        print(num)


Problem_Two()

def Problem_Three():
    """
    Problem 3
    Use the iter() function to convert the string below into an iterator:
    """
    print("\nProblem_Three")
    print("- - - - - - - - - - ")

    s = 'hello'

    s_iter = iter(s)

    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))

Problem_Three()

def Problem_EC():
    """
    Extra Credit!
    Can you explain what gencomp is in the code below? (Note: We never covered
    this in lecture! You will have to do some Googling/Stack Overflowing!)
    """
    print("\nProblem_EC")
    print("- - - - - - - - - - ")
    my_list = [1, 2, 3, 4, 5]

    gencomp = (item for item in my_list if item > 3)

    for item in gencomp:
        print(item)
