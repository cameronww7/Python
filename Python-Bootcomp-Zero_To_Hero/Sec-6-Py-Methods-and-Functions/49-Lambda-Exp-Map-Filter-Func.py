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


"""
lambda expression
One of Pythons most useful (and for beginners, confusing) tools is the 
lambda expression. lambda expressions allow us to create "anonymous" 
functions. This basically means we can quickly make ad-hoc functions 
without needing to properly define a function using def.

Function objects returned by running lambda expressions work exactly 
the same as those created and assigned by defs. There is key difference 
that makes lambda useful in specialized roles:

lambda's body is a single expression, not a block of statements.

The lambda's body is similar to what we would put in a def body's return 
statement. We simply type the result as an expression instead of explicitly 
returning it. Because it is limited to an expression, a lambda is less 
general that a def. We can only squeeze design, to limit program nesting. 
lambda is designed for coding simple functions, and def handles the larger 
tasks.

Lets slowly break down a lambda expression by deconstructing a function:
"""
print("\nlambda Function\n")


square = lambda num: num**2

print(square(3))


"""
So why would use this? Many function calls need a function passed in, 
such as map and filter. Often you only need to use the function you 
are passing in once, so instead of formally defining it, you just use 
the lambda expression. Let's repeat some of the examples from above 
with a lambda expression
"""
print("\nBring it all Together\n")

print("\nMap + Lambda")
print(list(map(lambda num: num ** 2, my_nums)))

checkEven = lambda num: num%2 == 0

print("\nFilter + Lambda")
print(list(filter(lambda n: n % 2 == 0, my_nums)))

print("\nMap + Lambda")
print(list(map(lambda name: name[0], names)))

print("\nMap + Lambda")
print(list(map(lambda xtx:xtx[::-1], names)))
