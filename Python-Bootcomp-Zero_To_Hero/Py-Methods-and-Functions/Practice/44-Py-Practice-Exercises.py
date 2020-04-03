from __future__ import print_function

"""
 Prompt 44-Py-Practice-Exercises
"""

print("44-Py-Practice-Exercises")

"""
    "Problems are arranged in increasing difficulty:\n",
    "* Warmup - these can be solved using basic comparisons and methods\n",
    "* Level 1 - these may involve if/then conditional statements and simple methods\n",
    "* Level 2 - these may require iterating over sequences, usually with some kind of loop\n",
    "* Challenging - these will take some creativity to solve"

"""


def pr1(xVar1, xVar2):
    #    "#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
    #    *if* both numbers are even, but returns the greater if one or both numbers are odd\n",
    #"    lesser_of_two_evens(2,4) --> 2\n",
    #"    lesser_of_two_evens(2,5) --> 5"
    varToReturn = ""

    if (xVar1%2 == 0) and (xVar2%2 ==0):
        if xVar1 > xVar2:
            varToReturn = xVar2
        else:
            varToReturn = xVar1
    else:
        if xVar1 > xVar2:
            varToReturn = xVar1
        else:
            varToReturn = xVar2

    return varToReturn


print(pr1(2, 4))
print(pr1(2, 5))


