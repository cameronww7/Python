from __future__ import print_function


# Prompt 1.6 : Implement a method to perform basic string compression using the counts
#               of repeated characters.
#               EX: the string aabcccccaaa would become a2b1c5a3. if the compressed
#               string would not become smaller than the original string your method
#               should return the original string . you can assume the string has only
#               uppercase and lower case letters (a-z)

print("1.6")

# StrCompression
#   This function takes in a string, then parses through the string counting the number
#   consecutive letters and building a string out with the letter and the number
#   associated with the number of consecutive letters and returns the new build string.
def StrCompression(xInString):
    xInString   = xInString.lower().replace(" ", "")
    newString   = ""
    letterCount = 1

    # Moves through the passed in string counting the letters building the return string.
    for x in range(len(xInString)-1):
        if xInString[x] == xInString[(x+1)]:
            letterCount = letterCount + 1
        else:
            if letterCount > 1:
                newString = newString + xInString[x] + letterCount.__str__()
            else:
                newString = newString + xInString[x] + "1"
            letterCount = 1

    # If Else Required to get the very last count to be added to the string.
    if letterCount > 1:
        newString = newString + xInString[x] + letterCount.__str__()
    else:
        newString = newString + xInString[len(xInString)-1] + "1"

    # If Else finally checking if the new string size is smaller than the original.
    # If the new string is longer will return original, if shorter will return new string.
    if len(newString) < len(xInString):
        return newString
    else:
        return xInString


print("\nStarting Program")

solutionStr1 = StrCompression("aabcccccaaa")
print("\naabcccccaaa =", solutionStr1)

solutionStr2 = StrCompression("aabbccbbbbbbba")
print("\naabbccbbbbbbba =", solutionStr2)

solutionStr3 = StrCompression("aabbcca")
print("\naabbcca =", solutionStr3)

solutionStr4 = StrCompression("AAbbCCZZZZZ")
print("\nAAbbCCZZZZZ =", solutionStr4)

print("\nEnd of Program")
