from __future__ import print_function

"""
 Prompt 72-Errors-and-Exception-Handling - Homework
"""

print("72-Errors-and-Exception-Handling - Homework")

"""

"""

print("\n72-Errors-and-Exception-Handling - Homework\n")
print("- - - - - - - - - - ")


"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""
try:
    for i in ['a' ,'b', 'c']:
        print(i**2)
except TypeError:
    print("TypeError")

except:
    print("Error")


"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.
"""
x = 5
y = 0

try:
    z = x/y

except ZeroDivisionError:
    print("ZeroDivisionError")

finally:
    print("All Done")

