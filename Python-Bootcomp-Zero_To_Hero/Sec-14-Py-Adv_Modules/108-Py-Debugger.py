from __future__ import print_function
import pdb

"""
 Prompt 108-Py-Debugger
"""

print("108-Py-Debugger")

"""
Python Debugger
You've probably used a variety of print statements to try to find 
errors in your code. A better way of doing this is by using 
Python's built-in debugger module (pdb). The pdb module implements 
an interactive debugging environment for Python programs. It 
includes features to let you pause your program, look at the 
values of variables, and watch program execution step-by-step, 
so you can understand what your program actually does and find 
bugs in the logic.

This is a bit difficult to show since it requires creating an 
error on purpose, but hopefully this simple example illustrates 
the power of the pdb module.
"""
print("\n108-Py-Debugger")
print("- - - - - - - - - - ")
x = [1, 3, 4]
y = 2
z = 3

result2 = 0
result = y + z
print(result)
#result2 = y+x
print(result2)

print("\nuse Debugger")
print("- - - - - - - - - - ")

x = [1, 3, 4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
pdb.set_trace()

result2 = y+x
print(result2)

