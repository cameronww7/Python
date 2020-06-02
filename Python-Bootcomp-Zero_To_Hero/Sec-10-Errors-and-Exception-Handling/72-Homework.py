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


"""
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
"""
def ask():
    while True:
        try:
            # First Attempt - will be successful if an Int comes in
            val = int(input("Please enter an integer: "))
        except ValueError:
            # If an error pops it will display an Error and re-prompted the user for an Int
            print("ValueError -- Looks like you did not enter an integer!")
            continue
        except:
            # If an error pops it will display an Error and re-prompted the user for an Int
            print("An Error Occurred")
            continue
        else:
            # Breaks the infinite while loop if a int is entered
            print("Your number squared is: {}".format(val**2))
            break


ask()
