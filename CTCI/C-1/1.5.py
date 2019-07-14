from __future__ import print_function
from collections import OrderedDict
import unittest

# Prompt 1.5 : There are three types of edits that can be performed on strings:
#               Incert a character, remove a character, or replace a character.
#               Given two strings, write a function to check if they are one
#               edit (or zero edits) away.
#    Ex: Pale, Ple -> True
#        Pales, pale -> True
#        Pale, bale -> true
#        Pale, bake -> False

print("1.5")

# IsOneAway
#   IsOneAway takes in two strings and compares the first string to the
#   second string check to is if one letter was to be added or subtracted
#   that the two strings would then become the same exact string and
#   once processed will return a true or false depending on the result.
def IsOneAway(xString1, xString2):
    print("  Start : String1-", xString1.__str__(), "|", "String2-", xString2.__str__())

    xString1 = xString1.lower().replace(" ", "")
    xString2 = xString2.lower().replace(" ", "")

    print("Cleaned : String1-", xString1.__str__(), "|", "String2-", xString2.__str__())

    offByOne = 0

    for x in range(len(xString2)):
        if xString1.find(xString2[x]) == -1:
            offByOne = offByOne + 1

    if offByOne < 2:
        return False
    else:
        return True


# PrintIsOneAwayReturn
#   Function is to print out the true or false statement provided by IsOneAway
def PrintIsOneAwayReturn(xResult):
    if xResult:
        print(">> Off By More Than One = FALSE\n")
    else:
        print(">> Off By One = TRUE\n")


print("\nStarting Program\n")

result = IsOneAway("Pale", "Ple")
PrintIsOneAwayReturn(result)

result = IsOneAway("Pales", "pale")
PrintIsOneAwayReturn(result)


result = IsOneAway("Pale", "bale")
PrintIsOneAwayReturn(result)


result = IsOneAway("Pale", "bake")
PrintIsOneAwayReturn(result)

print("End of Program")
