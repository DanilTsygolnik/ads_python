class Stack:

    def __init__(self):
        self.stack = [] # dynamic array to store stack elements

    def size(self):
        """Return the number of elements in stack"""
        return len(self.stack)

    def push(self, new_elem):
        """Add a new element to stack"""
        self.stack.append(new_elem)

    def peek(self):
        """Return value of the head element"""
        if self.size() != 0:
            return self.stack[-1]
        return None

    def pop(self):
        """Return value of the head and remove it from stack"""
        if self.size() != 0:
            curr_elem = self.stack[-1]
            self.stack = self.stack[:-1]
            return curr_elem
        return None
