import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.stack = [1,2,3,4]
        self.assertEqual(stack.size(), 4)
