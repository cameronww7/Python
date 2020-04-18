from __future__ import print_function

"""
 Prompt 37 List Comprehensions
"""

print("37 List Comprehensions")

"""
List Comprehensions

In addition to sequence operations and list methods, Python 
includes a more advanced operation called a list comprehension.

List comprehensions allow us to build out lists using a 
different notation. You can think of it as essentially a 
one line for loop built inside of brackets. 

For a simple example:
"""
my_str = "CATSAREREALLYCOOLLL"

my_list = []

for letter in my_str:
    my_list.append(letter)

# However we can do the same operation in a single line using List Comprehension

# --------------------------------------------------
# Grab every letter in string
lst = [x for x in 'waterMELLON']

# Check
print(lst)

# --------------------------------------------------
"""
This is the basic idea of a list comprehension. If you're familiar 
with mathematical notation this format should feel familiar for 
example: x^2 : x in { 0,1,2...10 }

Let's see a few more examples of list comprehensions in Python:
"""

# Square numbers in range and turn into list
lst = [x**2 for x in range(0, 11)]

# Check
print(lst)

# --------------------------------------------------
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]

# Check
print(lst)

# --------------------------------------------------

# Convert Celsius to Fahrenheit
celsius = [0, 10, 20.1, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius]

print(fahrenheit)

# --------------------------------------------------
lst = [x**2 for x in [x**2 for x in range(11)]]

# Check
print(lst)

