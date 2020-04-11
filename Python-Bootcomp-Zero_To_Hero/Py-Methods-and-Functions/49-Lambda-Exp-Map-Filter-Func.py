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
print("\nMap Function\n")

def square_func(num):
    return num**2


my_nums = [1, 2, 3, 4, 5, 6]

for item in map(square_func, my_nums):
    print(item)


print(list(map(square_func,my_nums)))


def splicer_func(myStr):
    if len(myStr)%2 == 0:
        return 'EVEN'
    else:
        return myStr[0]


names = ["joe", "amea", "noface", "Sally"]

print(list(map(splicer_func, names)))


"""
filter function
The filter function returns an iterator yielding those items of iterable 
for which function(item) is true. Meaning you need to filter by a function 
that returns either True or False. Then passing that into filter (along 
with your iterable) and you will get back only the results that would 
return True when passed to the function.
"""
print("\nFilter Function\n")

def check_even(num):
    return num%2 == 0


print(list(filter(check_even, my_nums)))


