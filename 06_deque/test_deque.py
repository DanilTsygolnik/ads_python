import unittest
from deque import Deque

class TestDeque(unittest.TestCase):

    def setUp(self):
        self.dq = Deque()

    def test_main_methods(self):

        # check the template
        self.assertEqual(self.dq.size(), 0)
        self.assertEqual(self.dq.deque, [])

        # addFront, addTail tests
        ref = [1,2,3,4,5,6]
        for i in ref[3:]:
            self.dq.addFront(i)
        self.assertEqual(self.dq.size(), 3)
        self.assertEqual(self.dq.deque, [4,5,6])
        for i in range(3,0,-1):
            self.dq.addTail(i)
        self.assertEqual(self.dq.size(), 6)
        self.assertEqual(self.dq.deque, [1,2,3,4,5,6])

        # removeFront, removeTail tests
        cnt = len(ref) 
        while self.dq.size() > 0:
            self.dq.removeFront()
            self.dq.removeTail()
            ref.pop(0) # remove the first item in ref list
            ref.pop() # remove the last item in ref list
            cnt -= 2
            self.assertEqual(self.dq.size(), cnt)
            self.assertEqual(self.dq.deque, ref)
        self.assertIs(self.dq.removeFront(), None)
        self.assertIs(self.dq.removeTail(), None)

if __name__=="__main__":
    unittest.main()
