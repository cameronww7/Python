from __future__ import print_function

# Prompt
# 1.2 :  Given two strings, write a method to decide if one is a permutation of other.
# Example:
#   "sumit" and "tiums" are permutations of each other.
#   "abcd" and bdea" are not permutations of each other.

print("1.2")

string1 = "sumit"
string2 = "tiums"

#string1 = "abcd"
#string2 = "bdea"

t = 0

for x in range(len(string1)):
    for i in range(len(string2)):
        if (string1[x] == string2[i]):
            t = t + 1


if (t == len(string1) and t == len(string2)):
    print("Two Strings are permutations")
else:
    print("Strings are not permutations")

print(" The Big O of this Solution is O(n^2)")
