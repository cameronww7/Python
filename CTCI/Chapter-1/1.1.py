from __future__ import print_function

# Prompt
# 1.1 : Implement an algorithm to determine if a string has all unique characters.
#       What if you cannot use additional data structures.
print("1.1")

uniqueString = "qwertyuiq"

for x in range(len(uniqueString)):
    for i in range(len(uniqueString)):
        if(uniqueString[x] == uniqueString[i] and x != i):
            print("FOUND DUPP | x = " + x.__str__() + " | i = " + i.__str__() + " |")

print(" I DID IT!")


print(" The Big O of this Solution is O(n^2)")