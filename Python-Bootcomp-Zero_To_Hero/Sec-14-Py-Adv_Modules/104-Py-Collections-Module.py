from __future__ import print_function
from collections import Counter
from collections import defaultdict
from collections import namedtuple

"""
 Prompt 104-Py-Collections-Module
"""

print("104-Py-Collections-Module")

"""

Collections Module
The collections module is a built-in module that implements specialized 
container data types providing alternatives to Python’s general purpose 
built-in containers. We've already gone over the basics: dict, list, set, 
and tuple.

Now we'll learn about the alternatives that the collections module provides.

Counter
Counter is a dict subclass which helps count hashable objects. Inside of 
it elements are stored as dictionary keys and the counts of the objects 
are stored as the value.

Let's see how it can be used:
"""

print("\n104-Py-Collections-Module")

print("\nCounter")
print("- - - - - - - - - - ")

lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print(Counter(lst))

print(Counter('aabsbsbsbhshhbbsbs'))

# Counter is a sub class of Dictionary class so it will look like one/function like one


s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print(Counter(words))


letters = "aaaaaabbbbbbccdddddsssss"

c = Counter(letters)

print(c)

print(c.clear())

"""
Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
"""

"""
defaultdict
defaultdict is a dictionary-like object which provides all methods 
provided by a dictionary but takes a first argument (default_factory) 
as a default data type for the dictionary. Using defaultdict is 
faster than doing the same using dict.set_default method.

A defaultdict will never raise a KeyError. Any key that does not exist 
gets the value returned by the default factory.
"""
print("\ndefaultdict")
print("- - - - - - - - - - ")
d = {}

#d['one']

d = defaultdict(object)

d['one']

for item in d:
    print(item)

    d = defaultdict(lambda: 0)

d['one']


"""
namedtuple
The standard tuple uses numerical indexes to access its members, for example:
"""
print("\nnamedtuple")
print("- - - - - - - - - - ")
t = (12, 13, 14)


t[0]


Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sam = Dog(age=2, breed='Lab', name='Sammy')

frank = Dog(age=2, breed='Shepard', name="Frankie")

print(sam)
print(frank)

print(sam.age)

print(sam[0])
