from __future__ import print_function
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


def isOneAway(xstring1: object) -> object:
    xstring2 = "222"
    xstring1 = xstring1.lower().replace(" ", "")
    xstring2 = xstring2.lower().replace(" ", "")

    print("String1 ", xstring1, "|", "String2", xstring2)

    return True


class Tests(unittest.TestCase):
    def test_case_01(self):
        self.assertTrue(isOneAway("Pale"))

    def test_case_02(self):
        self.assertTrue(isOneAway("Pales"))

    def test_case_03(self):
        self.assertTrue(isOneAway("Pale"))

    def test_case_04(self):
        self.assertTrue(isOneAway("Pale"))

unittest.main()