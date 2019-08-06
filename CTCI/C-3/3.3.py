from __future__ import print_function

"""
 Prompt 3.3 : Python - Stack of Plates
                        Imagine a (literal)stack of plates. If the stack gets too high, it might topple. 
                        Therefore, in real life, we would likely start a new stack when the previous 
                        stack exceeds some threshold. implement a data structure SetOfStacks that mimics 
                        this. SetOfStacks should be composed of several stacks and should create a new 
                        stack once the previous one exceeds capacity. SetOfStacks.push() and 
                        SetOfStacks,pop()) should behave identically to a single stack.
                        Implement a function popAT(int Index) which performs a pop operation on a specific sub stack.


    - https://stackoverflow.com/questions/4770627/how-to-implement-3-stacks-with-one-array
    - https://www.geeksforgeeks.org/efficiently-implement-k-stacks-single-array/
EX:       
        Input:  
        Output: 

"""

print("3.3")


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


class StackOfStacks:
    def __init__(self):
        self.SetOfStacks = Stack(Stack())

    # push
    #   Puts a new node on top of the stack
    def push(self, item):
        self.stacksOfStacks.push(item)

    # pop
    #   Returns the last element in the stack
    def pop(self):
        return self.stacksOfStacks.pop()


print("\nStarting Program\n")


print("\nEnd of Program")

