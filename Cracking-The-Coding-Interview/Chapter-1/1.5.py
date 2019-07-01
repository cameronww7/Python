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

def isOneAway(xString1, xString2):
    print("  Start : String1-", xString1.__str__(), "|", "String2-", xString2.__str__())

    xString1 = xString1.lower().replace(" ", "")
    xString2 = xString2.lower().replace(" ", "")

    print("Cleaned : String1-", xString1.__str__(), "|", "String2-", xString2.__str__())

    offByOne = 0

    for x in range(len(xString2)):
        if (xString1.find(xString2[x]) == -1):
            print(":xString1.find(xString2[x]) -", xString1.find(xString2[x]))
            offByOne = offByOne + 1
            print("OffByOne -", offByOne)

    if (offByOne < 2):
        print("\nIt is Off By One - TRUE\n")
        return False
    else:
        print("\nIt is Off By More Than One - FALSE\n")
        return True


isOneAway("Pale", "Ple")
isOneAway("Pales", "pale")
isOneAway("Pale", "bale")
isOneAway("Pale", "bake")


#
#class Tests1_5(unittest.TestCase):
#    def test_case_06(self):
#        self.assertTrue(isOneAway("Pale"))

#    def test_case_07(self):
#        self.assertTrue(isOneAway("Pales"))

#    def test_case_08(self):
#        self.assertTrue(isOneAway("Pale"))

 #   def test_case_09(self):
 #       self.assertTrue(isOneAway("Pale"))
#

#unittest.main()
