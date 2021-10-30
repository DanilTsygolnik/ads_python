# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from doubly_linked_list import LinkedList2
from doubly_linked_list import Node

def get_linked(nodes):
    s_list = LinkedList2()
    for i in nodes:
        s_list.add_in_tail(i)
    return s_list

class TestFind(unittest.TestCase):

    def test_setup_check(self):
        nodes = [Node(0), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.get_all_nodes(), nodes)
        self.assertEqual(s_list.get_all_nodes(True), [0,0,1,0])

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), None)

    def test_even_nodes_num1(self):
        nodes = [Node(0), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[2])

    def test_even_nodes_num2(self):
        nodes = [Node(0), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[1])

    def test_odd_nodes_num1(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[3])

    def test_odd_nodes_num2(self):
        nodes = [Node(0), Node(0), Node(1), Node(0), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[2])

    def test_odd_nodes_num2(self):
        nodes = [Node(0), Node(0), Node(0), Node(0), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[4])

if __name__=="__main__":
    unittest.main()
