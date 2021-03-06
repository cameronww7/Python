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
        self.set_of_stacks = [[]]
        self.stack_limit = 5

    # is_empty
    #   Checks if the set of stacks is empty
    def is_empty(self):
        if not self.set_of_stacks:
            return True
        else:
            return False

    # is_last_node_empty
    #   Checks to see if the very last node or stack is empty
    def is_last_node_empty(self):
        if not self.set_of_stacks[-1]:
            return True
        else:
            return False

    # push
    #   Puts a new node on top of the stack
    def push(self, data):
        # Checks to see if current stack is at limit
        if len(self.set_of_stacks[-1]) == self.stack_limit:
            # If stack is at limit appends a new stack
            self.set_of_stacks.append([])

        # adds node to the latest stack
        self.set_of_stacks[-1].append(data)

    # pop
    #   Returns the last element in the stack
    def pop(self):
        # Checks to see if the stack is empty
        if not self.is_last_node_empty():
            # Moves to the last stack on the set of stacks and pops node from that stack
            node = self.set_of_stacks[-1].pop()

            # current stack is empty
            if self.is_empty():
                self.set_of_stacks.pop()

                # entire stack is empty so resets it to an empty stack of stacks
                if self.is_empty():
                    self.set_of_stacks = [[]]
            return node
        else:
            return None

    # __str__
    #   Used to Print the Entire Stack of Stacks
    def __str__(self):
        for s in self.set_of_stacks:
            print(s)
        return ""

    # pop_at_index_
    #   Pops a node a specified section
    def pop_at_index_(self, x_index):
        node = self.set_of_stacks[x_index].pop()

        for index in range(x_index, len(self.set_of_stacks)-1):
            self.set_of_stacks[index].append(self.set_of_stacks[index + 1].pop(0))

        if self.is_last_node_empty():
            self.set_of_stacks.pop()

            if self.is_empty():
                self.set_of_stacks = [[]]

        return node


print("\nStarting Program\n")

set_of_stacks = StackOfStacks()

list_of_var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for index in list_of_var:
    set_of_stacks.push(index)

print(set_of_stacks)

set_of_stacks.pop_at_index_(0)
print(set_of_stacks)

set_of_stacks.pop_at_index_(1)
print(set_of_stacks)

set_of_stacks.pop()
print(set_of_stacks)

set_of_stacks.pop()
print(set_of_stacks)

print("\nEnd of Program")

