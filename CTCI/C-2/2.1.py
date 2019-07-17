from __future__ import print_function
"""
 Prompt 2.1 : Remove Dups
               Write code to remove duplicates from an unsorted linked list.
        Follow up - Ho would you solve this problem if a temporary buffer is not allowed.
        
        Video Watched - https://www.youtube.com/watch?v=Ast5sKQXxEU
        Site Using - https://www.tutorialspoint.com/python/python_linked_lists For Linked Listed in Python
"""

print("2.1")


class Node:
    def __init__(self, data_value, next_node=None):
        self.data = data_value
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data


class LinkedList (object):
    def __init__(self, root_node=None):
        self.root = root_node
        self.size = 0

    def get_size(self):
        return self.size

    def add_new_node(self, new_data):
        new_node = Node(new_data, self.root)
        self.root = new_node
        self.size += 1

    def remove_node(self, node_to_remove):
        current_node = self.root
        previous_node = None
        while current_node:
            if current_node.get_data() == node_to_remove:
                if previous_node:
                    previous_node.set_next_node(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True  # data is removed
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        return False  # data was not found/removed

    def find_node(self, data_to_find):
        current_node = self.root

        while current_node:
            if current_node.get_data() == data_to_find:
                return data_to_find
            else:
                current_node = current_node.get_next()
        return None

    def print_list(self):
        print("Need to Build")

    def remove_duplicates(self):
        print("Need to Build")


print("Starting Program")

myList = LinkedList()

myList.add_new_node(5)
myList.add_new_node(8)
myList.add_new_node(12)

myList.remove_node(8)

print(myList.remove_node(12))

print(myList.find_node(5))


print("\nEnd of Program")
