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



def pr2(xVar = "Cats Dogs"):
    #    "#### ANIMAL CRACKERS: Write a function takes a two-word string and
    #    returns True if both words begin with same letter\n",
    #"    animal_crackers('Levelheaded Llama') --> True\n",
    #"    animal_crackers('Crazy Kangaroo') --> False"
    var = xVar.split()
    var1 = var[1].upper()
    var = var[0].upper()
    print(var[:1] + var1[:1])

    if var[:1] == var1[:1]:
        return True
    else:
        return False


print(pr2("Dog Dock"))



def pr3(xVar1, xVar2):
    #    "#### MAKES TWENTY: Given two integers, return True if the sum of the
    #    integers is 20 *or* if one of the integers is 20. If not, return False.
    #"    makes_twenty(20,10) --> True\n",
    #"    makes_twenty(12,8) --> True\n",
    #"    makes_twenty(2,3) --> False"
     if xVar1 == 20 or xVar2 == 20:
         return True
     elif (xVar1 + xVar2) == 20:
         return True
     else:
         return False


print("{} - 8, 12".format(pr3(8, 12)))
print("{} - 8, 20".format(pr3(8, 20)))
print("{} - 8, 1".format(pr3(8, 1)))
