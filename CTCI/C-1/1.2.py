from __future__ import print_function
"""
# Prompt
# 1.2 :  Given two strings, write a method to decide if one is a permutation of other.
# Example:
#   "sumit" and "tiums" are permutations of each other.
#   "abcd" and bdea" are not permutations of each other.
"""

print("1.2")

"""
# IsStringPermutation
#   This function takes in two strings then moves through each slot
#   in string 2 comparing if they have the same letters and if they
#   are the same size with the same variables they are the
#   permutation of each other.
"""
def IsStringPermutation(xString1, xString2):
    sameLetterCount = 0

    if IsSameSize(xString1, xString2):
        for x in range(len(string1)):
            for i in range(len(string2)):
                if string1[x] == string2[i]:
                    sameLetterCount = sameLetterCount + 1
        if sameLetterCount == len(string1) and sameLetterCount == len(string2):
            return True
        else:
            return False
    else:
        return False


"""
 IsSameSize
   This function takes two strings in and returns if they are the
   same size or not with a true or false return
"""
def IsSameSize(xString1, xString2):
    if len(xString1) == len(xString2):
        return True
    else:
        return False


"""
 PrintResult
   This function takes in a true or false and returns the
   correct output message depending on what was passed in.
"""
def PrintResult(xResult):
    if xResult:
        print("\nTwo Strings are permutations")
    else:
        print("\nStrings are not permutations")


print("\nStarting Program\n")

string1 = "sumit"
string2 = "tiums"

print("String 1:", string1)
print("String 2:", string2)

result = IsStringPermutation(string1, string2)

PrintResult(result)

print("\nThe Big O of this Solution is O(n^2)")

print("\nEnd of Program")
