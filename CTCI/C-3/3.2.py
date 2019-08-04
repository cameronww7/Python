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


class Stack:
    def __init__(self):
        self.items = []
        self.minimum = 0

    # is_empty
    #   Checks and returns true or false is the stack is empty
    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    # push
    #   Puts a new node on top of the stack
    def push(self, item):
        if self.is_empty():
            self.set_minimum(item)
        else:
            if self.minimum > item:
                self.set_minimum(item)

        self.items.append(item)

    # pop
    #   Returns the last element in the stack
    def pop(self):
        return self.items.pop()

    # peek
    #   returns what the top element is in the stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # size
    #   returns the size of the stack
    def size(self):
        return len(self.items)

    # get_minimum
    #   returns minimum element in the stack
    def get_minimum(self):
        return self.minimum

    # set_minimum
    #   sets the minimum as the passed in value
    def set_minimum(self, new_min):
        self.minimum = new_min

    # min
    #   returns the minimum element in the stack
    def min(self):
        return self.get_minimum()


print("\nStarting Program\n")

my_stack = Stack()

my_stack.push(5)
my_stack.push(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
my_stack.push(599)

print(my_stack.peek())
print(my_stack.size())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.size())

print(my_stack.min())

print("\nEnd of Program")

