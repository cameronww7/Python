from __future__ import print_function

"""
 Prompt 2.4 : Python - Partition
                Write code to partition a linked list around a value x, such that 
                all nodes less than x come before all nodes greater than or equal 
                to x. if x is contained within the list, the values of x only need 
                to be after the elements less than x. the partition element x can 
                appear anywhere in the right partition; iot does not nee dto 
                appear between the left and right partitions.

EX:       
    Input:  3 -> 5 -> 8 -> 5 -> 1 -> 2 -> 1 [Partition = 5]
    Output: 3 -> 1 -> 2 -> 1 -> 5 -> 5 -> 8

        Video Watched - https://www.youtube.com/watch?v=Ast5sKQXxEU
        Site Using - https://www.tutorialspoint.com/python/python_linked_lists For Linked Listed in Python
"""

print("2.4")

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
    def __init__(self, root_node=None):
        self.root = root_node
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

        new_node = Node(new_data, self.root)  # Create New Node
        self.root = new_node  # adds a New Node in Line
        self.size += 1

    # remove_node - Remove
    #   Removes the passed in node number from the LinkedList
    def remove_node(self, node_to_remove):
        if self.is_empty():
            print("Removing :", node_to_remove)

            current_node = self.root  # Grabs Root Node
            previous_node = None  # Previous Node is Created set to null

            if current_node is not None:  # checks root node is not null
                if current_node.get_data() == node_to_remove:  # checks if root node is node to remove
                    self.root = current_node.get_next()  # set root node to next node
                    current_node = None  # clears old root node
                    print(node_to_remove, "Was Found & Removed")
                    return True

            while current_node:  # Loop Though list
                if current_node.get_data() == node_to_remove:  # checks if current node is node to remove
                    if previous_node:
                        previous_node.set_next_node(current_node.get_next())  # sets previous node to next node
                    else:
                        self.root = current_node  # sets root node to current node
                    self.size -= 1
                    print(node_to_remove, "Was Found & Removed")
                    return True  # data is removed
                else:
                    previous_node = current_node  # Increments previous node
                    current_node = current_node.get_next()  # Increments current node

            print(node_to_remove, "Does not Exist")
            return False  # data was not found/removed
        return False  # data was not found/removed

    # delete_link_list
    #   Deletes the entire linked list
    def delete_link_list(self):
        if self.is_empty():
            while self.root:  # Loop Though list
                current_node = self.root  # Grabs Root Node
                print("Removing :", current_node.get_data(), "Current Size:", self.size)
                self.size -= 1
                self.root = current_node.get_next()  # set root node to next node
                current_node = None  # clears old root node

        return True  # data is removed

    # find_node
    #   Finds the passed in node and returns its Data
    def find_node(self, data_to_find):
        if self.is_empty():
            print("Finding:", data_to_find)

            current_node = self.root

            while current_node:
                if current_node.get_data() == data_to_find:
                    print("Found:", data_to_find)
                    return data_to_find
                else:
                    current_node = current_node.get_next()
            print("Did Not Find:", data_to_find)
            return None
        return None

    # print_list
    #   Prints all the Nodes in the list, Start to End
    def print_list(self):
        if self.is_empty():
            if self.root:
                print("\nPrinting LinkedList Nodes")
                print("--------------------------")

                current_node = self.root
                node_count = 0

                while current_node:
                    print("   Node Count", node_count, ":", current_node.get_data())
                    current_node = current_node.get_next()
                    node_count += 1

                print("--------------------------\n")

    # Removes Duplicates
    #   Searches LinkedList and Removes all Duplicate Nodes
    def remove_duplicates(self):
        if self.is_empty():
            print("Removing all Duplicates")
            current_node = self.root

            while current_node:  # Loops through list
                dup_search = current_node.get_next()  # increments dup_search to 1 node ahead
                while dup_search:  # Loops though dup_search
                    if current_node.get_data() == dup_search.get_data():
                        self.remove_node(current_node.get_data())  # Removes dup Node
                    dup_search = dup_search.get_next()  # increments dup_search to 1 node ahead
                current_node = current_node.get_next()  # increments current_node to 1 node ahead
        else:
            return False

    # return_k_th_to_last
    #   Takes in a index to move to and returns the said data at that location
    def return_k_th_to_last(self, index_to_move):
        if self.is_empty():
            if index_to_move <= self.size:  # If index is out of the size return generic out of range msg
                current_node = self.root

                for x in range(0, index_to_move):  # Loops through list
                    current_node = current_node.get_next()

                print("The node at index", index_to_move, "is", current_node.get_data())
                return True
            else:
                print("The index", index_to_move, "does not exist in the Linked List")
                return False
            return False

    # return_k_th_to_last
    #   Takes in a index to move to and returns the said data at that location
    def return_node_at_index(self, index_to_move):
        if self.is_empty():
            if index_to_move <= self.size:  # If index is out of the size return generic out of range msg
                current_node = self.root

                for x in range(0, index_to_move):  # Loops through list
                    current_node = current_node.get_next()

                print("The node at index", index_to_move, "is", current_node.get_data())
                return current_node.get_data()

    # partition
    #   Takes in a index to partition and partitions the linked list around it
    def partition(self, input_partition):
        if self.is_empty():
            print("\nStarting Partitioning of Linked List")
            if self.find_node(input_partition) == input_partition:
                current_node = self.root

                lower_partition = LinkedList()   # Holds Values Lower than input_partition
                upper_partition = LinkedList()   # Holds Values Equal than input_partition
                middle_partition = LinkedList()  # Holds Values Greater than input_partition

                while current_node:  # Loops through list
                    if current_node.get_data() == input_partition:  # Grabs Values = to input_partition
                        middle_partition.add_new_node(current_node.get_data())
                    elif current_node.get_data() < input_partition:  # Grabs Values < to input_partition
                        lower_partition.add_new_node(current_node.get_data())
                    else:  # Grabs Values > to input_partition
                        upper_partition.add_new_node(current_node.get_data())
                    current_node = current_node.get_next()  # Moves TO next variable

                self.delete_link_list()  # Cleans Linked List

                # Adds values back to self list in upper partition
                upper_size = upper_partition.get_size()
                for x in range(0, upper_size):
                    self.add_new_node(upper_partition.return_node_at_index(x))

                # Adds values back to self list in middle partition
                middle_size = middle_partition.get_size()
                for x in range(0, middle_size):
                    self.add_new_node(middle_partition.return_node_at_index(x))

                # Adds values back to self list in lower partition
                lower_size = lower_partition.get_size()
                for x in range(0, lower_size):
                    self.add_new_node(lower_partition.return_node_at_index(x))
            else:
                return False
        else:
            return False


print("\nStarting Program\n")

myList = LinkedList()

myList.add_new_node(3)
myList.add_new_node(5)
myList.add_new_node(8)
myList.add_new_node(5)
myList.add_new_node(1)
myList.add_new_node(2)
myList.add_new_node(1)

myList.print_list()

myList.partition(5)

myList.print_list()

print("\nEnd of Program")

