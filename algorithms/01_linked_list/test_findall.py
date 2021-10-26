import ctypes
import unittest
from linked_list import LinkedList
from linked_list import Node

class TestFindall(unittest.TestCase):
    def test_findall(self):
        s_list = LinkedList()
        nodes = (6 * ctypes.py_object)()
        nodes[0] = Node(0)
        nodes[1] = Node(1)
        nodes[2] = Node(0)
        nodes[3] = Node(1)
        nodes[4] = Node(0)
        nodes[5] = Node(1)
        nodes_ref = [nodes[1], nodes[3], nodes[5]]

        self.assertEqual(s_list.find_all(1), [])

        for i in nodes:
            s_list.add_in_tail(i)

        self.assertEqual(s_list.find_all(1), nodes_ref)

if __name__=="__main__":
    unittest.main()
