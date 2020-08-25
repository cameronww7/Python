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


"""
Patterns
So far we've learned how to search for a basic string. What about more complex 
examples? Such as trying to find a telephone number in a large string of text? 
Or an email address?

We could just use search method if we know the exact phone or email, but what 
if we don't know it? We may know the general format, and we can use that along 
with regular expressions to search the document for strings that match a 
particular pattern.

This is where the syntax may appear strange at first, but take your time with 
this, often its just a matter of looking up the pattern code.

Let' begin!

Identifiers for Characters in Patterns
Characters such as a digit or a single string have different codes that represent 
them. You can use these to build up a pattern string. Notice how these make heavy 
use of the backwards slash \ . Because of this when defining a pattern string for 
regular expression we use the format:

r'mypattern'

placing the r in front of the string allows python to understand that the \ in 
the pattern string are not meant to be escape slashes.

Below you can find a table of all the possible identifiers:

</tr>
</tr>
</tr>
</tr>
</tr>
</tr></table>
"""
print("\nPatterns")
print("- - - - - - - - - - ")

text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

print("\nphone.group()")
print("- - - - - - - - - - ")
print(phone.group())



"""
Quantifiers
Now that we know the special character designations, we can use them along 
with quantifiers to define how many we expect.

Character	Description	Example Pattern Code	Exammple Match
\d	A digit	file_\d\d	file_25
\w	Alphanumeric	\w-\w\w\w	A-b_1
\s	White space	a\sb\sc	a b c
\D	A non digit	\D\D\D	ABC
\W	Non-alphanumeric	\W\W\W\W\W	*-+=)
\S	Non-whitespace	\S\S\S\S	Yoyo
</tr>
</tr>
</tr>
</tr>
</tr>
</tr></table>
"""
print("\nQuantifiers")
print("- - - - - - - - - - ")

print("\nre.search(r'\d{3}-\d{3}-\d{4}',text)")
print("- - - - - - - - - - ")
print(re.search(r'\d{3}-\d{3}-\d{4}', text))


"""
Groups
What if we wanted to do two tasks, find phone numbers, but also be able to 
quickly extract their area code (the first three digits). We can use groups 
for any general task that involves grouping together regular expressions 
(so that we can later break them down).

Using the phone number example, we can separate groups of regular expressions 
using parenthesis:
"""
print("\nGroups")
print("- - - - - - - - - - ")

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern,text)


# The entire result
print(results.group())

print(results.group(1))
print(results.group(2))
print(results.group(3))
print(results.group(4))
