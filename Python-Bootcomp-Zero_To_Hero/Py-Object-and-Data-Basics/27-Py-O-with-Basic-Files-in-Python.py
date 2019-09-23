from __future__ import print_function

from Tools.scripts.parseentities import writefile

"""
 Prompt 27 Booleans :
"""

print("27 Booleans")

"""

Files
Python uses file objects to interact with external files on your computer. 
These file objects can be any sort of file you have on your computer, 
whether it be an audio file, a text file, emails, Excel documents, etc. 
Note: You will probably need to install certain libraries or modules to 
interact with those various file types, but they are easily available. 
(We will cover downloading modules later on in the course).

Python has a built-in open function that allows us to open and play with 
basic file types. First we will need a file though. We're going to use 
some IPython magic to create a text file!

IPython Writing a File

%%writefile test.txt
Hello, this is a quick test file.


Python Opening a file
Let's being by opening the file test.txt that is located in the same 
directory as this notebook. For now we will work with files located in 
the same directory as the notebook or .py script you are using.

It is very easy to get an error on this step:
"""
myfile = open('whoops.txt')

"""
Writing to a File
By default, the open() function will only allow us to read the file. 
We need to pass the argument 'w' to write over the file. For example:
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file
"""
my_file = open('test.txt','w+')



