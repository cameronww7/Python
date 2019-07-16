from __future__ import print_function

# Prompt 1.4 : Palindrome Permutation
#
# Given a string, write a function to check if it is a permutation of a palindrome.
#
# Ex: input "Tact coa"
#       True  Tacocat or atcocta

print("1.4")


# IsPermPal
#   This function will take in a string, then will make the string all
#   lower case and then will remove all whitespace from the string.
#   Once if has done that it will move through the string comparing
#   the start and end for the same characters in the string, if they
#   do match it will return false otherwise will return true as it
#   will move to the center of the string.
def IsPermPal(xString):
    print("\nPassed In String :", xString)

    xString = xString.lower()
    xString = xString.replace(" ", "")

    print("Passed In String Sanitized:", xString)

    sizeHalfed = len(xString) / 2
    sizeHalfed = sizeHalfed.__round__()

    size = len(xString)
    size = size - 1

    for x in range(sizeHalfed):
        if xString[x] != xString[size]:
            return False
        else:
            size = size - 1

    return True


# PrintResult
#   This function will output the result from IsPermPal that has been
#   passed in and will output the string being tested.
def PrintResult(xPrompt, xResult):
    if xResult:
        print(" > \"", xPrompt, "\"", "is a Palindrome Permutation = ", xResult)
    else:
        print(" > \"", xPrompt, "\"", "is Not a Palindrome Permutation =", xResult)


print("Starting Program")

result = IsPermPal("cisco")
PrintResult("cisco", result)

result = IsPermPal("Rotator")
PrintResult("Rotator", result)

result = IsPermPal("Step on no pets")
PrintResult("Step on no pets", result)

result = IsPermPal("No lemon no melon")
PrintResult("No lemon no melon", result)

result = IsPermPal("Eva can I see bees in a cave")
PrintResult("Eva can I see bees in a cave", result)

print("\nEnd of Program")
