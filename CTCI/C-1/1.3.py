from __future__ import print_function

# Prompt 1.3 : Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true" length of the
# string.
#
# Input : "Mr John Smith", 13
# Output: "Mr%20John%20Smith"

print("1.3")


# ReplaceWhiteSpace
#   This function takes in a string and returns a new string with all white
#   space replaced with %
def ReplaceWhiteSpace(xString):
    newString = ""

    for x in range(len(xString)):
        if(xString[x] == " "):
            newString = newString + "%20"
        else:
            newString = newString + xString[x]

    return newString


string1 = "Mr John Smith"

string1 = string1.replace(" ","%20")

string2 = "Mr John Smith"

result = ReplaceWhiteSpace(string2)

print("Round 1: ", string1)
print("Round 2: ", result)
