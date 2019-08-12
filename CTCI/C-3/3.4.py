from __future__ import print_function

"""
 Prompt 3.4 : Python - Implement a MyQueue Class which implements a queue using two stacks.

                    First-in-First out

            The uniqueness of queue lies in the way items are added and removed. 
            The items are allowed at on end but removed form the other end. 
EX:       
        Input:  
        Output: 

"""

print("3.4")


class MyQueue:
    def __init__(self):
        self.queue = list()

    # add_to_queue
    #   Pushes on a new node
    def add_to_queue(self, new_node, print_io):
        # Insert method to add element
        if print_io is not None:
            print("Adding:", new_node)
        if new_node not in self.queue:
            self.queue.insert(0, new_node)
            return True
        return False

    # remove_from_queue
    #    Pop method to remove element
    def remove_from_queue(self):
        if not self.is_empty():
            return self.queue.pop()
        return "No elements in Queue!"

    # is_empty
    #   Checks to see if the queue is empty
    def is_empty(self):
        if len(self.queue) > 0:
            return False
        print("No elements in Queue!")
        return True

    # print_queue
    #   Prints the entire queue
    def print_queue(self):
        print("\nPRINTING QUEUE")
        for x in range(0, len(self.queue), 1):
            temp = self.queue.pop()
            print(temp)
            self.add_to_queue(temp, None)


print("\nStarting Program\n")

my_queue = MyQueue()

print("Is the que Empty?", my_queue.is_empty())
print("\nIs There something to remove?", my_queue.remove_from_queue())

print("\n")

my_queue.add_to_queue(5, "Display")
my_queue.add_to_queue(4, "Display")
my_queue.add_to_queue(3, "Display")
my_queue.add_to_queue(2, "Display")
my_queue.add_to_queue(1, "Display")

my_queue.print_queue()
my_queue.print_queue()
my_queue.print_queue()

print("\nEnd of Program")

