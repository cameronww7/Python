from __future__ import print_function

"""
 Prompt 2.8 : Python - Loop-Detection
                        Make a circular linked list and have a function that finds the original first node

EX:       
        Input:  
        Output: 

        Video Watched - https://www.youtube.com/watch?v=Ast5sKQXxEU
        Site Using - https://www.tutorialspoint.com/python/python_linked_lists For Linked Listed in Python
"""

print("2.8")

"""
class Node
    This class is used for LinkedList, its the the core to the list.
    As this is the structure needed to create the list of nodes (self).
"""


class Node:
    # Class Constructor
    def __init__(self, data_value, next_node=None):
        self.data = data_value
        self.head = next_node

    # get_next - Getter
    #   Sends the pointer to the next node
    def get_next(self):
        return self.next_node

    # set_next_node - Setter
    #   Sets the node current node to point at the next node passed in
    def set_next_node(self, new_node):
        self.next_node = new_node

    # get_data - Getter
    #   Sends the data of the current Node
    def get_data(self):
        return self.data

    # set_data - Setter
    #   Sets the passed in data to the current Node
    def set_data(self, new_data):
        self.data = new_data


"""
class LinkedList
    This class is a data structure to create a list of Node class which is called a LinkedList.
    Because all the nodes connect to one another. 
"""


class LinkedList(object):
    # Class Constructor
    def __init__(self, root_node=None, tail_node=None):
        self.root = Node(None)
        self.tail = Node(None)
        self.root.next_node = self.tail
        self.tail.next_node = self.root
        self.size = 0

    # get_size - Getter
    #   Returns the Current Size of the LinkedList
    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size < 0:
            print("> Linked List Is EMPTY <")
            return False
        else:
            return True

    # add_new_node - Add
    #   Adds a new node to the LinkedList, adds to the End
    def add_new_node(self, new_data):
        print("Adding :", new_data)
        new_node = Node(new_data)

        if self.root.data is None:
            self.root = new_node
            self.tail = new_node
            new_node.next_node = self.root
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.tail.next_node = self.root

    def print_list(self):
        current = self.root
        if self.root is None:
            print("List is empty")
            return
        else:
            print("Nodes of the circular linked list: ")
            print(current.data),
            while current.next_node != self.root:
                current = current.next_node
                print(current.data)


print("\nStarting Program\n")


my_list_1 = LinkedList()

my_list_1.add_new_node(1)
my_list_1.add_new_node(2)
my_list_1.add_new_node(3)
my_list_1.add_new_node(4)

my_list_1.print_list()

print("\nEnd of Program")

