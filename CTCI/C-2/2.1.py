from __future__ import print_function
"""
 Prompt 2.1 : Remove Dups
               Write code to remove duplicates from an unsorted linked list.
        Follow up - Ho would you solve this problem if a temporary buffer is not allowed.
        
        Video Watched - https://www.youtube.com/watch?v=Ast5sKQXxEU
        Site Using - https://www.tutorialspoint.com/python/python_linked_lists For Linked Listed in Python
"""

print("2.1")


"""
class Node
    This class is used for LinkedList, its the the core to the list.
    As this is the structure needed to create the list of nodes (self).
"""
class Node:
    # Class Constructor
    def __init__(self, data_value, next_node=None):
        self.data = data_value
        self.next_node = next_node

    # Getter - Sends the pointer to the next node
    def get_next(self):
        return self.next_node

    # Setter - Sets the node current node to point at the next node passed in
    def set_next_node(self, new_node):
        self.next_node = new_node

    # Getter - Sends the data of the current Node
    def get_data(self):
        return self.data

    # Setter - Sets the passed in data to the current Node
    def set_data(self, new_data):
        self.data = new_data


"""
class LinkedList
    This class is a data structure to create a list of Node class which is called a LinkedList.
    Because all the nodes connect to one another. 
"""
class LinkedList (object):
    # Class Constructor
    def __init__(self, root_node=None):
        self.root = root_node
        self.size = 0

    # Getter - Returns the Current Size of the LinkedList
    def get_size(self):
        return self.size

    # Add - Adds a new node to the LinkedList, adds to the End
    def add_new_node(self, new_data):
        print("Adding :", new_data)

        new_node = Node(new_data, self.root)
        self.root = new_node
        self.size += 1

    # Remove - Removes the passed in node number from the LinkedList
    def remove_node(self, node_to_remove):
        print("Removing :", node_to_remove)

        current_node = self.root
        previous_node = None

        if current_node is not None:
            if current_node.get_data() == node_to_remove:
                self.root = current_node.get_next()
                current_node = None
                print(node_to_remove, "Was Found & Removed")
                return True

        while current_node:
            if current_node.get_data() == node_to_remove:
                if previous_node:
                    previous_node.set_next_node(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                print(node_to_remove, "Was Found & Removed")
                return True  # data is removed
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        print(node_to_remove, "Was Not Found & Removed")
        return False  # data was not found/removed

    # Find - Finds the passed in node and returns its Data
    def find_node(self, data_to_find):
        print("Finding: ", data_to_find)

        current_node = self.root

        while current_node:
            if current_node.get_data() == data_to_find:
                return data_to_find
            else:
                current_node = current_node.get_next()

        return None

    # Print - Prints all the Nodes in the list, Start to End
    def print_list(self):
        print("\nPrinting LinkedList Nodes")
        print("--------------------------")

        current_node = self.root
        node_count = 0

        while current_node:
            print("   Node Count", node_count, ":", current_node.get_data())
            current_node = current_node.get_next()
            node_count += 1

        print("--------------------------\n")

    # Core Function to this Project, Removes Duplicates
    def remove_duplicates(self):
        print("Removing all Duplicates")
        current_node = self.root

        while current_node:
            #print("1 - ", current_node.get_data())
            dup_search = current_node.get_next()
            while dup_search:
                #print("2 - ", dup_search.get_data())
                if current_node.get_data() == dup_search.get_data():
                    self.remove_node(current_node.get_data())
                dup_search = dup_search.get_next()
            current_node = current_node.get_next()
        #print("3")

print("\nStarting Program\n")

myList = LinkedList()

myList.add_new_node(1)
myList.add_new_node(2)
myList.add_new_node(4)
myList.add_new_node(3)
myList.add_new_node(4)
myList.add_new_node(6)
myList.add_new_node(5)
myList.add_new_node(4)

myList.print_list()

myList.remove_node(8)

print(myList.remove_node(12))

print(myList.find_node(5))

myList.remove_duplicates()

myList.print_list()

myList.remove_node(5)
myList.remove_node(4)
myList.remove_node(4)

myList.print_list()

print("\nEnd of Program")
