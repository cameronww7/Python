from __future__ import print_function
"""
 Prompt
 1.1 : Implement an algorithm to determine if a string has all unique characters.
      What if you cannot use additional data structures.
"""

print("1.1")

"""
 FindDupChars
   This function will take in a string and check if the string contains all
   unique characters and will return a true for false depending on the string.
"""
def FindDupChars(xString):
    print("\nTest String:", xString)

    for index1 in range(len(xString)):
        for index2 in range(len(xString)):
            if (xString[index1] == xString[index2] and index1 != index2):
                print("ERROR: FOUND DUPP | x = " + index1.__str__() + " | i = " + index2.__str__() + " |")
                return False

    return True


"""
 PrintOutput
   This Function will take in a result and display the correct output
   message depending on the result.
"""
def PrintOutput(xResult):
    if xResult:
        print("The String is Unique")
    else:
        print("ERROR: A Duplicate letter was found")


print("\nStarting Program")

result = FindDupChars("qwertyuiq")
PrintOutput(result)

result = FindDupChars("qwertyui")
PrintOutput(result)

print("\nThe Big O of this Solution is O(n^2)")

print("\nEnd of Program")
