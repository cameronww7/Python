from __future__ import print_function

"""
 Prompt 49-Lambda-Exp-Map-Filter-Func
"""

print("49-Lambda-Exp-Map-Filter-Func")

"""
Lambda Expressions, Map, and Filter
Now its time to quickly learn about two built in functions, filter and map. 
Once we learn about how these operate, we can learn about the lambda 
expression, which will come in handy when you begin to develop your skills 
further!
"""

"""
map function
The map function allows you to "map" a function to an iterable object. 
That is to say you can quickly call the same function to every item in 
an iterable, such as a list. For example:
"""


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)


print(list(map(square,my_nums)))


def splicer(myStr):
    if len(myStr)%2 == 0:
        return 'EVEN'
    else:
        return myStr[0]


name = ["joe", "amea", "noface"]

print(list(map(splicer, name)))



