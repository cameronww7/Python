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


def pr7(xVar):
    #    "#### FIND 33: \n",
    #    "\n",
    #    "Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.\n",
    #    "\n",
    #    "    has_33([1, 3, 3]) → True\n",
    #    "    has_33([1, 3, 1, 3]) → False\n",
    #    "    has_33([3, 1, 3]) → False"
    print("\nProblem # 7")
    varReturn = False

    size = len(xVar)

    for index in range(0, size-1, 1):
        if xVar[index] == 3 and xVar[index+1] == 3:
            varReturn = True

    return varReturn


print(pr7([3, 1, 3, 1, 4, 9, 9, 1, 3, 3]))


def pr8(xVar="Hello"):
    # "#### PAPER DOLL: Given a string, return a string where for every character in the
    # original there are three characters\n",
    # "    paper_doll('Hello') --> 'HHHeeellllllooo'\n",
    # "    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'"
    print("\nProblem 8")
    varReturn = ""
    for index in range(0, len(xVar), 1):
        varReturn = varReturn + xVar[index] + xVar[index] + xVar[index]

    return varReturn


print(pr8("Mississippi"))



def pr9(xVar1=8, xVar2=6, xVar3=7):
    #    "#### BLACKJACK: Given three integers between 1 and 11,
    #    if their sum is less than or equal to 21, return their sum.
    #    If their sum exceeds 21 *and* there's an eleven, reduce the
    #    total sum by 10. Finally, if the sum (even after adjustment)
    #    exceeds 21, return 'BUST'\n",
    #   "    blackjack(5,6,7) --> 18\n",
    #   "    blackjack(9,9,9) --> 'BUST'\n",
    #   "    blackjack(9,9,11) --> 19"
    print("\nProblem 9")
    handTotal = xVar1 + xVar2 + xVar3
    valReturn = "BUST"

    # pre check to see if there is a 11 and they exceed 21
    if handTotal > 21 and (xVar1 == 11 or xVar2 == 11 or xVar3 == 11):
        handTotal = handTotal - 10

    if handTotal > 21:
        valReturn = "BUST"
    elif handTotal < 21:
        valReturn = handTotal
    elif handTotal == 21:
        valReturn = "BLACKJACK"

    return valReturn


print(pr9(5, 5, 5))
print(pr9(5, 5, 11))
print(pr9(5, 7, 10))
print(pr9(10, 11, 0))



def pr10(xVar):
    #    "#### SUMMER OF '69: Return the sum of the numbers in the array,
    #    except ignore sections of numbers starting with a 6 and extending
    #    to the next 9 (every 6 will be followed by at least one 9).
    #    Return 0 for no numbers.\n",
    #    " \n",
    #    "    summer_69([1, 3, 5]) --> 9\n",
    #    "    summer_69([4, 5, 6, 7, 8, 9]) --> 9\n",
    #    "    summer_69([2, 1, 6, 9, 11]) --> 14"
    print("\nProblem 10")

    varReturn = 0

    for index in range(0, len(xVar), 1):
        if xVar[index] < 6 or xVar[index] > 9:
            varReturn = varReturn + xVar[index]

    return varReturn


print(pr10([1, 3, 5]))
print(pr10([4, 5, 6, 7, 8, 9]))
print(pr10([2, 1, 6, 9, 11]))


def pr11(xVar):
    #   SPY GAME: Write a function that takes in a list of integers
    #   and returns True if it contains 007 in order\n",
    print("\nProblem 11")

    varReturn = False

    for index in range(0, len(xVar)-2, 1):
        if xVar[index] == "0" and xVar[index+1] == "0" and xVar[index+2] == "7":
            varReturn = True

    return varReturn


print(pr11("007asdasd"))


def pr12(xVar):
    # "#### COUNT PRIMES: Write a function that returns the *number* of
    # prime numbers that exist up to and including a given number\n",
    # "    count_primes(100) --> 25\n"
    print("\nProblem 12")

    varReturn = []

    for index1 in range(2, xVar, 1):
        counter = 0
        #print("index1 = {}".format(index1))
        for index2 in range(2, index1+1, 1):
            #print("index1 {} % {} index2 = {}".format(index1, index2, (index1%index2)))
            if (index1 % index2) == 0 and index1 != index2:
                counter = counter + 1
                #print("counter = {}".format(counter))

        if counter == 0:
            #print("adding - {}".format(index1))
            varReturn.append(index1)


    size = len(varReturn)


    print("Size {} - {}".format(size, varReturn))
    return varReturn


print(pr12(100))


def pr13(xVar):
    # "#### PRINT BIG: Write a function that takes in a single letter,
    # and returns a 5x5 representation of that letter\n",
    # "    print_big('a')\n",
    # "    \n",
    # "    out:   *  \n",
    # "          * *\n",
    # "         *****\n",
    # "         *   *\n",
    # "         *   *\n",
    # "HINT: Consider making a dictionary of possible patterns, and
    # mapping the alphabet to specific 5-line combinations of patterns.
    # <br>For purposes of this exercise, it's ok if your dictionary stops at \"E\"."
    print("\nProblem 13")
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    for pattern in alphabet[xVar.upper()]:
        print(patterns[pattern])


print(pr13("a"))

