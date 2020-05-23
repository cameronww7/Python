from __future__ import print_function

"""
 Prompt 71-Errors-and-Exception-Handling
"""

print("71-Errors-and-Exception-Handling")

"""
Errors and Exception Handling
In this lecture we will learn about Errors and Exception Handling in Python. You've definitely 
already encountered errors by this point in the course. For example:

print('Hello)

File "<ipython-input-1-db8c9988558c>", line 1
    print('Hello)
                 ^
SyntaxError: EOL while scanning string literal
Note how we get a SyntaxError, with the further description that it was an EOL (End of Line Error) 
while scanning the string literal. This is specific enough for us to see that we forgot a single 
quote at the end of the line. Understanding these various error types will help you debug your 
code much faster.

This type of error and description is known as an Exception. Even if a statement or expression is 
syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected 
during execution are called exceptions and are not unconditionally fatal.

You can check out the full list of built-in exceptions here. Now let's learn how to handle errors 
and exceptions in our own code.

try and except
The basic terminology and syntax used to handle errors in Python are the try and except statements. 
The code which can cause an exception to occur is put in the try block and the handling of the 
exception is then implemented in the except block of code. The syntax follows:

try:
   You do your operations here...
   ...
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. 

We can also just check for any exception with just using except: To get a better understanding of all 
this let's check out an example: We will look at some code that opens and writes a file:
"""

print("\n71-Errors-and-Exception-Handling\n")
print("- - - - - - - - - - ")

