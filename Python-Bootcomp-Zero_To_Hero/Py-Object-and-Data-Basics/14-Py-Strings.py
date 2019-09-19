from __future__ import print_function

"""
 Prompt 14 Strings :
"""

print("14 Strings")

print("mixing ''quotes''")

print("escape sequences '\n'newline''")
print("escape sequences '\t'tab''")

print(len("stringgg"))


my_str = "HACK THE PLANET"

# Grab first Char
print(my_str[0])

# grab last char
print(my_str[-1])


# String Slicing

my_str = "123456789"

# Grabs everything past the third char in str
print(my_str[2:])

print(my_str[2:-2])

# grabs everything up to second slot, not including the second slot
print(my_str[:2])

# prints the entire string
print(my_str[::])

# jumps to ever second slot, interesting
print(my_str[::2])


# jumps to ever second slot, interesting
# [Start:Stop:Jump Size]
print("my_str[1:1:2]", my_str[1:9:1])

# Quick easy reverse string
print(my_str[::-1])

# Immutability

name = "Sam"

# This will Cause an Error
# name[0] = 'P'

last_letters = name[1:]

print("P" + last_letters)

# String concatenation
print("Pam" + " YO")

# upper cases
my_str.upper()

# lower cases
my_str.lower()

# splits a string based on white space unless specified
# returns a List
my_str.split()


# String interpolation
# String interpolation
print("this is a string {}".format("INSERTED"))


print("The {} {} {}".format("Fox", "Brown", "Quick"))


print("The {2} {1} {0}".format("Fox", "Brown", "Quick"))


print("The {q} {b} {f}".format(f="Fox", b="Brown", q="Quick"))

