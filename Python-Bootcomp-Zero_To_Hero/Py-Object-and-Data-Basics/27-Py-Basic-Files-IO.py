from __future__ import print_function

from Tools.scripts.parseentities import writefile

"""
 Prompt 27 IO :
"""

print("27 IO")

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
# COMMENTED OUT CAUSE IT CAUSES AN ERROR
#myfile = open('whoops.txt')


# Open the text.txt we made earlier
my_file = open('test.txt')

# We can now read the file
print(my_file.read())


# But what happens if we try to read it again?
print(my_file.read())


# Seek to the start of file (index 0)
print(my_file.seek(0))

# Now read again
print(my_file.read())


# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()

my_file.close()

# provides a file permissions on
"""
mode= r'  - read only
mode='w'  - is write only
mode='a'  - is append only
mode='r+' - is reading and writing
mode='w+' - is writing and reading
"""
with open("test.txt", mode="w+") as my_file:
    my_file.write("\n1-NEW DATA AHHHHH")
    my_file.write("\n2-NEW DATA AHHHHH")
    my_file.write("\n3-NEW DATA AHHHHH")
    my_file.write("\n4-NEW DATA AHHHHH")

with open("test.txt", mode="r") as my_file:
    contents = my_file.read()

with open("test.txt", mode="a") as my_file:
    my_file.write("\nNEW DATA AHHHHH")

with open("test.txt", mode="r+") as my_file:
    print(my_file.read())

"""
Writing to a File

By default, the open() function will only allow us to read the file. 
We need to pass the argument 'w' to write over the file. For example:
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file
"""
# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file
my_file = open('test.txt', 'w+')

# Write to the file
my_file.write('This is a new line')

# Read the file
my_file.seek(0)
my_file.read()

my_file.close()  # always do this when you're done with a file

"""
Appending to a File

Passing the argument 'a' opens the file and puts the pointer at the 
end, so anything written is appended. Like 'w+', 'a+' lets us read 
and write to a file. If the file does not exist, one will be created.
"""
my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')

my_file.seek(0)
print(my_file.read())

my_file.close()
