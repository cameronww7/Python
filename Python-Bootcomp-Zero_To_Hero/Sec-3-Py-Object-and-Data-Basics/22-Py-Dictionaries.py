from __future__ import print_function

"""
 Prompt 22 Dictionaries :
"""

print("22 Dictionaries")

# Dictionaries: Objects retrieved by key name.
#   Unordered and can not be sorted

# Lists: Objects retrieved by location
#   Ordered Sequence can be indexed or sliced

my_dict = {'key1': 'value1', 'key2': 'value2'}


my_price = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.99}

print(my_price['apple'])

my_dict = {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']}

# Let's call items from the dictionary
print(my_dict['key3'])

print(my_dict['key3'][0])

# Can then even call methods on that value
print(my_dict['key3'][0].upper())

# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

print(d)
