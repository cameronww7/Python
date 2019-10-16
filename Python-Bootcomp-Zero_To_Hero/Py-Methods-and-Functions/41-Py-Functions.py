from __future__ import print_function

"""
 Prompt 41-Py-Functions.py
"""

print("41-Py-Functions.py")

"""
Functions
Introduction to Functions
This lecture will consist of explaining what a function is in Python and 
how to create one. Functions will be one of our main building blocks 
when we construct larger and larger amounts of code to solve problems.

So what is a function?

Formally, a function is a useful device that groups together a set of 
statements so they can be run more than once. They can also let us 
specify parameters that can serve as inputs to the functions.

On a more fundamental level, functions allow us to not have to repeatedly 
write the same code again and again. If you remember back to the lessons 
on strings and lists, remember that we used a function len() to get the 
length of a string. Since checking the length of a sequence is a common 
task you would want to write a function that can do this repeatedly at command.

Functions will be one of most basic levels of reusing code in Python, and 
it will also allow us to start thinking of program design (we will dive 
much deeper into the ideas of design when we learn about Object Oriented Programming).
"""
# --------------------------------------------------
"""
def Statements
Let's see how to build out a function's syntax in Python. It has the following form:
"""
# --------------------------------------------------


def name_of_function(arg1, arg2):
    """
    This is where the function's Document String (docstring) goes
    """
    # Do stuff here
    # Return desired result


"""
We begin with def then a space followed by the name of the function. Try to 
keep names relevant, for example len() is a good name for a length() function. 
Also be careful with names, you wouldn't want to call a function the same 
name as a built-in function in Python (such as len).

Next come a pair of parentheses with a number of arguments separated by a 
comma. These arguments are the inputs for your function. You'll be able to 
use these inputs in your function and reference them. After this you put a colon.

Now here is the important step, you must indent to begin the code inside your 
function correctly. Python makes use of whitespace to organize code. Lots of 
other programing languages do not do this, so keep that in mind.

Next you'll see the docstring, this is where you write a basic description of 
the function. Using iPython and iPython Notebooks, you'll be able to read these 
docstrings by pressing Shift+Tab after a function name. Docstrings are not 
necessary for simple functions, but it's good practice to put them in so you or 
other people can easily understand the code you write.

After all this you begin writing the code you wish to execute.

The best way to learn functions is by going through examples. So let's try to 
go through examples that relate back to the various objects and data structures 
we learned about before.
"""
# --------------------------------------------------


def say_hello():
    print('hello')


say_hello()

# --------------------------------------------------

"""
Using return
Let's see some example that use a return statement. return allows a function to 
return a result that can then be stored as a variable, or used in whatever manner 
a user wants.
"""


# added a default to passed in params
def add_num(num1=1, num2=1):
    return num1+num2


print(add_num(4, 5))

# --------------------------------------------------


def is_prime(num):
    """
    Naive method of checking for primes.
    """
    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
    else: # If never mod zero, then prime
        print(num, 'is prime!')


print(is_prime(16))

print(is_prime(17))
