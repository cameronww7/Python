from __future__ import print_function

# Prompt 1.9 : Assume you have a method isSubstring which checks if one word is a substring of another.
# given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to
# isSubstring (e.g, "watterbottle" is a rotation of "erbottlewat")


print("1.9")


# IsSubstring
#   This function takes in two strings and builds a new string of the same
#   letters they both have in common, if the sizes at the end do not match then
#   they are not a subString of each other and therefore the program returns a False.
#   Otherwise the function will return as long as they are the same size in the end.
def IsSubstring(xOrginalStr, xCheckIfSubStr):
    print("\n   xOrginalStr :", xOrginalStr)
    print("xCheckIfSubStr :", xCheckIfSubStr)

    if CheckSameSize(xOrginalStr, xCheckIfSubStr):
        newString = ""

        for index1 in range(len(xOrginalStr)):
            for index2 in range(len(xCheckIfSubStr)):
                if xOrginalStr[index1] == xCheckIfSubStr[index2]:
                    newString = newString + xOrginalStr[index1]
                    break

        if CheckSameSize(xOrginalStr, newString):
            return newString
        else:
            return False
    else:
        return False


# CheckSameSize
#   This function takes in two strings and returns if they are the same size
#   by returning true or false.
def CheckSameSize(xOrginalStr, xCheckIfSubStr):
    if len(xOrginalStr) != len(xCheckIfSubStr):
        return False
    else:
        return True


# PrintResult
#   This function will output the result from IsPermPal that has been
#   passed in and will output the string being tested.
def PrintResult(xResult, xString1, xString2):
    if xResult != False:
        print(" > \"", xString1, "\"", "is a SubString of",  "\"", xString2, "\"", "= True")
    else:
        print(" > \"", xString1, "\"", "is NOT a SubString of", "\"", xString2, "\" = False")


print("Starting Program\n")

result = IsSubstring("watterbottle", "terbottlewat")
PrintResult(result, "watterbottle", "terbottlewat")

result = IsSubstring("Cat", "Fat")
PrintResult(result, "Cat", "Fat")

result = IsSubstring("BowMan", "ManBow")
PrintResult(result, "BowMan", "ManBow")

print("\nEnd of Program")
