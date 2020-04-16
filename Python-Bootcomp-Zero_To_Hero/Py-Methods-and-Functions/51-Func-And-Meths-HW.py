from __future__ import print_function

"""
 Prompt 51-Func-And-Meths-HW
"""

print("51-Func-And-Meths-HW")

"""
Nested Statements and Scope
Now that we have gone over writing our own functions, it's important 
to understand how Python deals with the variable names you assign. 
When you create a variable name in Python the name is stored in a 
name-space. Variable names also have a scope, the scope determines 
the visibility of that variable name to other parts of your code.
"""


def pr1(xVal):
    # Write a function that computes the volume of a sphere given its radius.
    # 4/3 * xVal ^3
    print("\nProblem 1")

    return (4/3) * 3.14 * (xVal**3)

print(pr1(3))


def pr2(xHigh, xLow, xNum):
    # Write a function that checks whether a number is in a given range (inclusive of high and low)
    print("\nProblem 2")
    print("Passed in {}, {}, {}".format(xHigh, xLow, xNum))

    middle = (xHigh + xLow) / 2
    print("Middle : {}".format(middle))

    if middle < xNum:
        valReturn = "HIGH"
    else:
        valReturn = "LOW"

    if xNum <= xHigh and xNum >= xLow:
        valReturn = valReturn + " - Yes it is IN Range"
    else:
        valReturn = valReturn + " - No it is NOT Range"

    return valReturn


print(pr2(5, 1, 3))


def pr3(xVal):
    # Write a Python function that accepts a string and calculates the number of upper case
    # letters and lower case letters.
    #
    # Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    # Expected Output :
    # No. of Upper case characters : 4
    # No. of Lower case Characters : 33
    #
    # HINT: Two string methods that might prove useful: .isupper() and .islower()
    #
    # If you feel ambitious, explore the Collections module to solve this problem!
    print("\nProblem 3")

    numUpper = 0
    numLower = 0
    strLen = len(xVal)

    for index in range(0, strLen, 1):
        if xVal[index].isupper():
            numUpper += 1
        elif xVal[index].islower():
            numLower += 1

    print("No. of Upper case characters : {}".format(numUpper))
    print("No. of Lower case characters : {}".format(numLower))


pr3("OOoOoo")


def pr4(xVal):
    # Write a Python function that takes a list and returns a new list with unique elements of the first list.
    #
    # Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    # Unique List : [1, 2, 3, 4, 5]
    print("\nProblem 4")

    xVal = set(xVal)

    return xVal


print(pr4([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))



def pr5(xVal):
    # Write a Python function to multiply all the numbers in a list.
    #
    # Sample List : [1, 2, 3, -4]
    # Expected Output : -24
    print("\nProblem 5")

    listSize = len(xVal)

    result = 1

    for index in xVal:
        result = result * index

    return result

print(pr5([5, 5, 1, -1]))
print(pr5([1, 2, 3, -4]))


def pr6(xVal):
    # Write a Python function that checks whether a passed in string
    # is palindrome or not.
    #
    # Note: A palindrome is word, phrase, or sequence that reads the
    # same backward as forward, e.g., madam or nurses run.
    print("\nProblem 6")

    xVal = xVal.replace(" ", "")

    #print("|{}|".format(xVal))

    strSize = len(xVal)
    end = strSize-1
    retunVal = True

    #print(round(strSize/2))
    #print(end)

    for index in range(0, round(strSize/2), 1):
        #print("{}{} != {}{}".format(index,xVal[index], xVal[end], end))

        if xVal[index] != xVal[end]:
            retunVal = False
            break

        end = end - 1

    return retunVal


print(pr6("nurses run"))
print(pr6("madam"))
print(pr6("1225221"))
print(pr6("cats"))
