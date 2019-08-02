from __future__ import print_function

"""
 Prompt 3.2 : Python - Stack Min
                        How would you design a stack which, in addition to push a pop, 
                        has a function min which returns the minimum element? push, 
                        pop and min should all operate ion O(1) time.


    - https://stackoverflow.com/questions/4770627/how-to-implement-3-stacks-with-one-array
    - https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/
EX:       
        Input:  
        Output: 

"""

print("3.2")

"""
# Stack
#   Class stack simulates a stack
class Stack:
    # Constructor
    def __int__(self, data_value):
        self.minimum_value = data_value
        self.stack = [0]

    def get_min(self):
        return self.minimum_value

    def set_min(self, new_min):
        self.minimum_value = new_min

    # is_empty
    #   Checks to see if the stack is empty
    def is_empty(self):
        if len(self.stack) <= 0:
            return False
        else:
            return True

    # add_node
    #   Adds a node on top of the stack
    def push_node(self, data_to_add):
        if data_to_add >= self.get_min():
            self.set_min(data_to_add)

        self.stack.append(data_to_add)


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

    def min(self):
        print("cats")
"""
print("\nStarting Program\n")

"""
my_stack = Stack()

my_stack.push_node(1)
my_stack.push_node(2)
my_stack.push_node(3)

my_stack.min()
"""
print("\nEnd of Program")

