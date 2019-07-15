from __future__ import print_function
from collections import OrderedDict
import unittest

# Prompt 1.4 : Palindrome Permutation
#
# Given a string, write a function to check if it is a permutation of a palindrome.
#
# Ex: input "Tact coa"
#       True  Tacocat or atcocta

print("1.4")

def IsPermPal(xInputString):
    dic = {}  # Setup dictionary

    xInputString = xInputString.lower()
    xInputString = xInputString.replace(" ", "")

    for c in xInputString:  # Init Dic
        dic[c] = 0

    for c in xInputString:  # count Frequency
        dic[c] += 1

    num_even = 0
    for c, count in dic.items():
        if count % 2 == 0:
            num_even += 1

    if (num_even in (len(dic), len(dic) - 1)):
        size = len(xInputString) / 2
        size = size.__round__()

        x = []
        y = []

# Problem with Characters that repeat for display

        for i in range(len(xInputString)):

            if xInputString.count(xInputString[i]) == 2:

                if xInputString[i] not in x:
                    x.append(xInputString[i])

            elif xInputString.count(xInputString[i]) >= 2:
                x.append(xInputString[i])

            elif xInputString.count(xInputString[i]) == 1:
                y.append(xInputString[i])

        print("x: ", x)
        print("y: ", y)

        newString = ""

        for i in range(len(x)):
            newString = newString + x[i]

        for i in range(len(y)):
            newString = newString + y[i]

        for i in range(len(x)-1, -1, -1):
            newString = newString + x[i]

        print(xInputString, "is a Palindrome Permutation = ", newString)
        return True
    else:
        print(xInputString, "is Not a Palindrome Permutation")
        return False


class Tests(unittest.TestCase):
    def test_case_01(self):
        self.assertFalse(IsPermPal("cisco"))

    def test_case_02(self):
        self.assertTrue(IsPermPal("Rotator"))

    def test_case_03(self):
        self.assertTrue(IsPermPal("Step on no pets"))

    def test_case_04(self):
        self.assertTrue(IsPermPal("No lemon no melon"))

    def test_case_05(self):
        self.assertTrue(IsPermPal("Eva can I see bees in a cave"))


unittest.main()
