from __future__ import print_function
import time
import timeit

"""
 Prompt 112-Py-Regex
"""

print("112-Py-Regex")

"""
Sometimes it's important to know how long your code is taking to run, 
or at least know if a particular line of code is slowing down your 
entire project. Python has a built-in timing module to do this.
"""
print("\n112-Py-Regex")
print("- - - - - - - - - - ")

def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

func_one(10)


def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str, range(n)))

func_one(10)


# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(10000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(10000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)


"""
What if we have two blocks of code that are quite fast, 
the difference from the time.time() method may not be 
enough to tell which is fater. In this case, we can 
use the timeit module.

The timeit module takes in two strings, 

a statement (stmt) and a setup. It then runs the setup code and 

runs the stmt code some n number of times and reports back average 
length of time it took.
"""

# We have to pass it as a string
stmt = 'func_one(100)'

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=1000000))


stmt2 = 'func_two(100)'

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=1000000))

print("Function 2 is Faster!")
