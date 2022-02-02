import unittest
from stack_head_opt import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.stack = [4,3,2,1]

    def test_size(self):
        self.assertEqual(self.stack.size(), 4)
        self.stack.stack = []
        self.assertEqual(self.stack.size(), 0)

    def test_push(self):
        self.stack.push(5)
        self.assertEqual(self.stack.size(), 5)
        self.assertEqual(self.stack.stack, [5,4,3,2,1])

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 4)
        self.stack.stack = []
        self.assertTrue(self.stack.peek() is None)

    def test_pop(self):
        for i in range(4,0,-1):
            self.assertEqual(self.stack.size(), i)
            self.assertEqual(self.stack.pop(), i)
        self.assertTrue(self.stack.peek() is None)

if __name__=="__main__":
    unittest.main()
