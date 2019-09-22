from __future__ import print_function

"""
 Prompt 24 Tuples :
"""

print("24 Tuples")

"""
In Python tuples are very similar to lists, however, unlike lists
they are immutable meaning they can not be changed. You would use 
tuples to present things that shouldn't be changed, such as days 
of the week, or dates on a calendar.

In this section, we will get a brief overview of the following:

1.) Constructing Tuples
2.) Basic Tuple Methods
3.) Immutability
4.) When to Use Tuples

You'll have an intuition of how to use tuples based on what you've 
learned about lists. We can treat them very similarly with the major 
distinction being that tuples are immutable.
"""

# Create a tuple
t = (1, 2, 3, 6, 7, 8, 10)

# Check len just like a list
print(len(t))

# Can also mix object types
t = ('one', 2)

# Show
print(t)

# Use indexing just like we did in lists
print(t[0])

# Use indexing just like we did in lists
print(t[-1])


# Use .index to enter a value and return the index
print(t.index('one'))

# Use .count to count the number of times a value appears
print(t.count('one'))

# It can't be stressed enough that tuples are immutable.
# It can't be stressed enough that tuples are immutable.
# It can't be stressed enough that tuples are immutable.
