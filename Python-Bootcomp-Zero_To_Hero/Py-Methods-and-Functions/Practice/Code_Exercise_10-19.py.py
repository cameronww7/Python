from __future__ import print_function

"""
 Prompt Code_Exercise_10-19.py
"""

print("Code_Exercise_10-19.py")

"""
Purpose:

The purpose of this file is to go through the coding exercise and knock them out one by one!

So, here we go!
"""

#Write a function that will output hello world
def hello_world():
    print("Hello World!!")

hello_world()


#Define a function that names a name in and prints hello, name
def respond(xName, xMethod):
    if xMethod == 1:
        print("Hello " + xName)
    else:
        print("Hello {}".format(xName))

respond("FOO BAR", 0)
