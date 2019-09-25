from __future__ import print_function

"""
 Prompt 34 for Loops 
"""

print("34 for Loops")

"""
for Loops
A for loop acts as an iterator in Python; it goes through items 
that are in a sequence or any other iterable item. Objects that 
we've learned about that we can iterate over include strings, 
lists, tuples, and even built-in iterables for dictionaries, 
such as keys or values.

We've already seen the for statement a little bit in past 
lectures but now let's formalize our understanding.

Here's the general format for a for loop in Python:

for item in object:
    statements to do stuff
The variable name used for the item is completely up to the coder, 
so use your best judgment for choosing a name that makes sense and 
you will be able to understand when revisiting your code. This item 
name can then be referenced inside your loop, for example if you 
wanted to use if statements to perform checks.

Let's go ahead and work through several example of for loops using a 
variety of data object types. We'll start simple and build more 
complexity later on.
"""

# We'll learn how to automate this sort of list in the next lecture
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --------------------------------------------------
for num in list1:
    print(num)

# --------------------------------------------------
for num in list1:
    if num % 2 == 0:
        print(num)

# --------------------------------------------------
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')

# --------------------------------------------------
# Start sum at zero
list_sum = 0

for num in list1:
    list_sum = list_sum + num

print(list_sum)

# --------------------------------------------------
for letter in 'This is a string.':
    print(letter)

# --------------------------------------------------
tup = (1,2,3,4,5)

for t in tup:
    print(t)

# --------------------------------------------------
list2 = [(2,4),(6,8),(10,12)]

for tup in list2:
    print(tup)

# Now with unpacking!
for (t1,t2) in list2:
    print(t1)

# --------------------------------------------------
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

# Create a dictionary view object
d.items()

# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v)
