from __future__ import print_function

"""
 Prompt 3.1 : Python - Three in One
                Describe how you could use a single array to implement three stacks
                        
    
    - https://stackoverflow.com/questions/4770627/how-to-implement-3-stacks-with-one-array
EX:       
        Input:  
        Output: 

"""

print("3.1")


# Stack
#   Class stack simulates a stack
class Stack:
    # Constructor
    def __int__(self):
        self.stack = []

    # add_node
    #   Adds a node on top of the stack
    def add_node(self, data_to_add):
        if data_to_add not in self.stack:
            self.stack.append(data_to_add)
            return True
        else:
            return False  # Data is already in Stack

    # pop_node
    #   Removes the first node on the stack, and returns it
    def pop_node(self):
        if len(self.stack) <= 0:
            print("Stack is Empty")
            return False
        else:
            return self.stack.pop()

    # peek
    #   Shows the first node
    def peek(self):
        return self.stack[-1]


print("\nStarting Program\n")

my_stack = Stack()


print("\nEnd of Program")

