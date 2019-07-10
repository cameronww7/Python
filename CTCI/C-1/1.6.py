from __future__ import print_function


# Prompt 1.6 : Implement a method to perform basic string compression using the counts
#               of repeated characters.
#               EX: the string aabcccccaaa would become a2b1c5a3. if the compressed
#               string would not become smaller than the original string your method
#               should return the original string . you can assume the string has only
#               uppercase and lower case letters (a-z)

print("1.6")

def strCompression(xInString):
    xInString   = xInString.lower().replace(" ", "")
    newString   = ""
    letterCount = 1

    for x in range(len(xInString)-1):
        #print(xInString[x],xInString[(x+1)])
        if xInString[x] == xInString[(x+1)]:
            letterCount = letterCount + 1
            #print("1Count= ",letterCount)
        else:
            #print("2Count= ", letterCount)
            if letterCount > 1:
                newString = newString + xInString[x] + letterCount.__str__()
            else:
                newString = newString + xInString[x] + "1"
            letterCount = 1

    if letterCount > 1:
        newString = newString + xInString[x] + letterCount.__str__()
    else:
        newString = newString + xInString[len(xInString)-1] + "1"

    #print("newString:", newString)

    if len(newString) < len(xInString):
        print("newString:", newString)
        return newString
    else:
        print("xInString:", xInString)
        return xInString

strCompression("aabcccccaaa")
strCompression("aabbccbbbbbbba")
strCompression("aabbcca")
strCompression("AAbbCCZZZZZ")