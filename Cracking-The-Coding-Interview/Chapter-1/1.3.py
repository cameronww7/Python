from __future__ import print_function

# Prompt 1.3 : Write a method to replace all spaces in a string with '%20'. You may assume that the string has
# sufficient space at the end to hold the additional characters, and that you are given the "true" length of the
# string.
#
# Input : "Mr John Smith", 13
# Output: "Mr%20John%20Smith"

print("1.3")

inputString = "Mr John Smith"

inputString = inputString.replace(" ","%20")

print("Round 1: " + inputString)

inputString = "Mr John Smith"

newString = ""

for x in range(len(inputString)):
    if(inputString[x] == " "):
        newString = newString + "%20"
    else:
        newString = newString + inputString[x]

print("Round 2: " + newString)