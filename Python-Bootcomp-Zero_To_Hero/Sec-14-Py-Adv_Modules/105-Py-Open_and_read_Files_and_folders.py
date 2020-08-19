from __future__ import print_function
import os # os.
import shutil # for shutil.
#import send2trash

"""
 Prompt 105-Py-Open_and_read_Files_and_folders
"""

print("105-Py-Open_and_read_Files_and_folders")

"""

"""

print("\nCreating Practice.txt")
print("- - - - - - - - - - ")
f = open('practice.txt','w+')

f.write('test')
f.close()

print(os.getcwd())
t = os.getcwd()

print(t)

# In your current directory
print(os.listdir())
t = os.listdir()

print(t)

"""
Moving Files
You can use the built-in shutil module to to move files to different 
locations. Keep in mind, there are permission restrictions, for 
example if you are logged in a User A, you won't be able to make 
changes to the top level Users folder without the proper permissions, 
more info
"""
print("\nMoving Practice.txt")
print("- - - - - - - - - - ")
#print(shutil.move('practice.txt','C:\\Users\\Marcial'))

print(os.listdir())



"""
Deleting Files
NOTE: The os module provides 3 methods for deleting files:

os.unlink(path) which deletes a file at the path your provide
os.rmdir(path) which deletes a folder (folder must be empty) at the 
path your provide
shutil.rmtree(path) this is the most dangerous, as it will remove all 
files and folders contained in the path. All of these methods can not 
be reversed! Which means if you make a mistake you won't be able to 
recover the file. Instead we will use the send2trash module. A safer 
alternative that sends deleted files to the trash bin instead of 
permanent removal.
"""
print("\nDeleting Practice.txt")
print("- - - - - - - - - - ")
print(os.listdir())

#send2trash.send2trash('practice.txt')

print(os.listdir())


"""
Walking through a directory
Often you will just need to "walk" through a directory, that is 
visit every file or folder and check to see if a file is in the 
irectory, and then perhaps do something with that file. Usually 
recursively walking through every file and folder in a directory 
would be quite tricky to program, but luckily the os module has a 
direct method call for this called os.walk(). Let's explore how 
it works.
"""
print("\nWalking through a directory")
print("- - - - - - - - - - ")

print(os.getcwd())

print(os.listdir())
