# 6. Python Collections
from __future__ import print_function

print("\nPython Collections")

print ("\nList/Tuples")
x = [1,2,3,4,5]

print ("\nprint x:", x)
print ("\nprint x[3]:", x[3])

y = (1,2,3,4,5)

print ("\nprint y:", y)
print ("\nprint y[4]:", y[4])

u = {"kacl", 124, 'Ben',3232}

print("\nPrint u: ", u)

print("\nPrint u.pop(): ", u.pop())

# Dic uses { } Brackets
u = {"kacl":1, 124:2, 'Ben':4,3232:3}

print("\nPrint u: ", u)

u = {"A":1, 'B':2,9:3}

print("\nPrint u: ", u)

#List uses [ ] Square Brackets
l = ['AaA', 'BbB', 'DdD', 'CcC', 'eEe']

for letter in l:
    print(letter)

z = len(l)
print ("len(l): ", z)

print ("\nLoop finding index")
for index in range(0,len(l)):
    print(l[index], 'is found at index:', index)

print ("\nLoop Telling where item is in the list")
for index in l:
    print(index, 'is found at index:', l.index(index))

names = ["Ben", "Sally", "Amy", "George", "Randy", "Alice"]
print(names)

raw_newIndex = input('\nPlease enter the index to replace:')
newIndex = int(raw_newIndex)

newName = input('\nPlease enter the name to put into index:')

names[newIndex] = newName
print(names)

newName = input('\nPlease enter the name to add to the list:')
names.append(newName)
print(names)

remName = input('\nPlease enter the name to remove from the list:')
names.remove(remName)
print(names)