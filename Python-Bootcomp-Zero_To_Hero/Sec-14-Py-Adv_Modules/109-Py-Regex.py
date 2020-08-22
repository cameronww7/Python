from __future__ import print_function
import re

"""
 Prompt 109-Py-Regex
"""

print("109-Py-Regex")

"""
Overview of Regular Expressions
Regular Expressions (sometimes called regex for short) allows a 
user to search for strings using almost any sort of rule they 
can come up. For example, finding all capital letters in a string, 
or finding a phone number in a document.

Regular expressions are notorious for their seemingly strange 
syntax. This strange syntax is a byproduct of their flexibility. 
Regular expressions have to be able to filter out any string 
pattern you can imagine, which is why they have a complex string 
pattern format.

Let's begin by explaining how to search for basic patterns in a string!

Searching for Basic Patterns
Let's imagine that we have the following string:
"""
print("\n109-Py-Regex")
print("- - - - - - - - - - ")

text = "The person's phone number is 408-555-1234. Call soon!"

print('phone' in text)


print("\nphone")
print("- - - - - - - - - - ")
pattern = 'phone'
print(re.search(pattern, text))


print("\nNOT IN TEXT")
print("- - - - - - - - - - ")
pattern = "NOT IN TEXT"
print(re.search(pattern, text))


print("\nphone")
print("- - - - - - - - - - ")
pattern = 'phone'
match = re.search(pattern, text)
print(match)

print("\nmatch.span()")
print("- - - - - - - - - - ")
print(match.span())

print("\nmatch.start()")
print("- - - - - - - - - - ")
print(match.start())

print(match.end())

text = "my phone is a new phone"

match = re.search("phone",text)

print(match.span())


matches = re.findall("phone",text)

print(matches)

for match in re.finditer("phone",text):
    print(match.span())

print(match.group())
