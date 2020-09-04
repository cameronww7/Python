from __future__ import print_function
import time

"""
 Prompt 109-Py-Regex
"""

print("109-Py-Regex")

"""
Sometimes it's important to know how long your code is taking to run, 
or at least know if a particular line of code is slowing down your 
entire project. Python has a built-in timing module to do this.
"""
print("\n109-Py-Regex")
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
    return list(map(str,range(n)))

func_one(10)


# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)
