from __future__ import print_function
"""
 Prompt 2.1 : Remove Dups
               Write code to remove duplicates from an unsorted linked list.
        Follow up - Ho would you solve this problem if a temporary buffer is not allowed.
        
        Video Watched - https://www.youtube.com/watch?v=Ast5sKQXxEU
        Site Using - https://www.tutorialspoint.com/python/python_linked_lists For Linked Listed in Python
"""

print("2.1")



def RemoveDuplicates():


    return False


class Node:
    def __init__(self, data_Value, next_Node = None):
        self.data = data_Value
        self.next_Node = next_Node

    def get_next(self):
        return self.next_Node

    def set_next_Node(self, new_Node):
        self.next_Node = new_Node

    def get_data(self):
        return self.data

    def set_data(self, new_Date):
        self.data = new_Date

class LinkedList:
    def __init__(self):
        self.headval = None

    def list_print(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def get_size(self):
        print("Still Building")

    def find_node(self):
        print("Still Building")

    def add_node(self):
        print("Still Building")

    def remove_node(self):
        print("Still Building")


list = LinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.list_print()



print("Starting Program")


print("\nEnd of Program")
