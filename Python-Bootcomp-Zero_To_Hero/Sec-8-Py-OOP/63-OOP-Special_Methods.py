
from __future__ import print_function

"""
 Prompt 63-OOP-Special_Methods
"""

print("63-OOP-Special_Methods")

"""

Special Methods
Finally let's go over special methods. Classes in Python can implement 
certain operations with special method names. These methods are not 
actually called directly but by Python specific language syntax. 
"""

print("\n63-OOP-Special_Methods\n")
print("- - - - - - - - - - ")


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print("\nPrint Book")
print(book)

print("\nLength of Book")
print(len(book))

print("\nDeleting Book")
del book
