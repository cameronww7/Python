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
    # "    lesser_of_two_evens(2,4) --> 2\n",
    # "    lesser_of_two_evens(2,5) --> 5"
    print("\nProblem # 1")
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
    # "    animal_crackers('Levelheaded Llama') --> True\n",
    # "    animal_crackers('Crazy Kangaroo') --> False"
    print("\nProblem # 2")
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
    # "    makes_twenty(20,10) --> True\n",
    # "    makes_twenty(12,8) --> True\n",
    # "    makes_twenty(2,3) --> False"
    print("\nProblem # 3")
    if xVar1 == 20 or xVar2 == 20:
         return True
    elif (xVar1 + xVar2) == 20:
         return True
    else:
         return False


print("{} - 8, 12".format(pr3(8, 12)))
print("{} - 8, 20".format(pr3(8, 20)))
print("{} - 8, 1".format(pr3(8, 1)))



def pr4(xVar = "macdonald"):
    # "#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name\n",
    # "     \n",
    # "    old_macdonald('macdonald') --> MacDonald\n",
    # "    \n",
    # "Note: `'macdonald'.capitalize()` returns `'Macdonald'`"
    print("\nProblem # 4")
    var = ""
    var = xVar[0].upper() + xVar[1:3] + xVar[3].upper() + xVar[4:]
    print("var = {}".format(var))


pr4()


def pr5(xVar = "I am Home"):
    # "#### MASTER YODA: Given a sentence, return a sentence with the words reversed\n",
    # "\n",
    # "    master_yoda('I am home') --> 'home am I'\n",
    # "    master_yoda('We are ready') --> 'ready are We'\n",
    # "    \n",
    # "Note: The .join() method may be useful here. The .join() method allows you to join
    # together strings in a list with some connector string. For example, some uses of the
    # .join() method:\n",
    # "\n",
    # "    >>> \"--\".join(['a','b','c'])\n",
    # "    >>> 'a--b--c'\n",
    # "\n",
    # "This means if you had a list of words you wanted to turn back into a sentence,
    # you could just join them with a single space string:\n",
    # "\n",
    # "    >>> \" \".join(['Hello','world'])\n",
    # "    >>> \"Hello world\""
    print("\nProblem # 5")
    var = xVar.split()
    size = len(var)
    yodaSay = ""
    for index in range(size-1, -1, -1):
        yodaSay = yodaSay + " " + var[index] + " "

    print("Yoda Says \'{}\'".format(yodaSay))



pr5()
pr5("We Are Ready")



def pr6(xVar=101):
    # "source": [
    #     "#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200\n",
    #     "\n",
    #     "    almost_there(90) --> True\n",
    #     "    almost_there(104) --> True\n",
    #     "    almost_there(150) --> False\n",
    #     "    almost_there(209) --> True\n",
    #     "    \n",
    #     "NOTE: `abs(num)` returns the absolute value of a number"
    print("\nProblem # 6")
    varReturn = False

    if xVar >= 90 and xVar <= 110:
        varReturn = True
    elif xVar >= 190 and xVar <= 210:
        varReturn = True

    return varReturn

print(pr6(211))
