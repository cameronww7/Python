from __future__ import print_function

# Prompt 1.9 : Assume you have a method isSubstring which checks if one word is a substring of another.
# given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to
# isSubstring (e.g, "watterbottle" is a rotation of "erbottlewat")


print("1.9")

string1 = "watterbottle"
string2 = "terbottlewat"


def IsSubstring(xOrginalStr, xCheckIfSubStr):
    if CheckSameSize(xOrginalStr, xCheckIfSubStr):
        newString = ""

        for index1 in range(len(xOrginalStr)):
            for index2 in range(len(xCheckIfSubStr)):
                if xOrginalStr[index1] == xCheckIfSubStr[index2]:
                    newString = newString + xOrginalStr[index1]
        return newString
    else:
        return False


def CheckSameSize(xOrginalStr, xCheckIfSubStr):
    if len(xOrginalStr) != len(xCheckIfSubStr):
        return False
    else:
        return True


print("Starting Program\n")

print("string1:", string1)
print("string1:", string2)

solutionString = IsSubstring(string1, string2)

print("\nsolutionString:", solutionString)

print("\nEnd of Program")
