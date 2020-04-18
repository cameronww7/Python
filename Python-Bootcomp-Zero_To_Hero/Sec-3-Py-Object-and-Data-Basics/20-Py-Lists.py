from __future__ import print_function

"""
 Prompt 20 List :
"""

print("20 List")

my_list = [1, 2, 3, 4]

my_list_two = ['String', 200, 34.22]

# Len of list
print(len(my_list))

# slicing
print(my_list[2:])

# concatation
print(my_list + my_list_two)

# can change any item in a list
my_list[0] = "BOOMMMM"

# append a  item to the end of the list
my_list.append(23232)

print(my_list)

# pops the last item
print(my_list.pop())

popped_item = my_list.pop()

print(popped_item)


print(my_list.pop(0))

my_list = ["a","s","f","z"]

num_list = [1, 2, 3, 4, 6, 0]

my_list.sort()
num_list.sort()

print(my_list)
print(num_list)





