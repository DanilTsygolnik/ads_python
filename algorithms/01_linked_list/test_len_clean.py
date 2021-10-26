import unittest
from linked_list import LinkedList
from linked_list import Node

class TestLenClean(unittest.TestCase):
    
    def setUp(self):
        
        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))

    def tearDown(self):
        self.s_list = None

    def test_len(self):
        self.assertEqual(self.s_list.len(), 6)

    def test_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIs(self.s_list.head, self.s_list.tail)

if __name__ == "__main__":
    unittest.main()
