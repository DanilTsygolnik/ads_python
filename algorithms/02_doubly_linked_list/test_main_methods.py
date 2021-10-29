# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from doubly_linked_list import LinkedList2
from doubly_linked_list import Node

class TestFind(unittest.TestCase):
    def setUp(self):
        self.nodes = [Node(0), Node(0), Node(1), Node(0)]
        self.s_list = LinkedList2()
        for i in self.nodes:
            self.s_list.add_in_tail(i)

    def test_setup_check(self):
        self.assertEqual(self.s_list.get_all_nodes(), self.nodes)
        self.assertEqual(self.s_list.get_all_nodes(True), [0,0,1,0])

    def test_empty(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.find_bin(1), None)

    def test_one_node(self):
        self.s_list.clean()
        node = Node(1)
        self.s_list.add_in_tail(node)
        self.assertEqual(self.s_list.find_bin(1), node)
        node = Node(0)
        self.s_list.clean()
        self.s_list.add_in_tail(node)
        self.assertEqual(self.s_list.find_bin(1), None)

    def test_even_nodes_num1(self):
        self.assertEqual(self.s_list.find_bin(1), self.nodes[2])

    def test_even_nodes_num2(self):
        self.nodes = [Node(0), Node(1), Node(0), Node(0)]
        self.s_list = LinkedList2()
        for i in self.nodes:
            self.s_list.add_in_tail(i)
        self.assertEqual(self.s_list.find_bin(1), self.nodes[1])

    def test_odd_nodes_num1(self):
        self.s_list.add_in_tail(Node(0))
        self.assertEqual(self.s_list.find_bin(1), self.nodes[2])

if __name__=="__main__":
    unittest.main()
