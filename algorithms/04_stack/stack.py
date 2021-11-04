import ctypes

class Stack:

    def __init__(self):
        self.stack = [] # dynamic array to store stack elements

    def size(self):
        """Return the number of elements in stack"""
        return len(self.stack)
