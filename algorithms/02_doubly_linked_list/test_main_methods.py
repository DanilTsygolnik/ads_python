# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from doubly_linked_list import LinkedList2
from doubly_linked_list import Node

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
def get_linked(nodes):
    s_list = LinkedList2()
    for i in nodes:
        s_list.add_in_tail(i)
    return s_list

<<<<<<< HEAD
class TestFind(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

class TestFindall(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), nodes)

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3]])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3], nodes[5]])
<<<<<<< HEAD
=======
=======
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
class TestFind(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

<<<<<<< HEAD
    def test_even_nodes_num2(self):
        nodes = [Node(0), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[1])

    def test_odd_nodes_num1(self):
<<<<<<< HEAD
        self.s_list.add_in_tail(Node(0))
        self.assertEqual(self.s_list.find_bin(1), self.nodes[2])
>>>>>>> 995a631 (algo, doubly linked list, wip: add_in_tail(), get_all_nodes(), clean(), find() -- main tests ok)
=======
=======
    def test_long_single_node(self):
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
<<<<<<< HEAD
        self.assertEqual(s_list.find_bin(1), nodes[4])
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
=======
        self.assertEqual(s_list.find(1), nodes[3])
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
=======
>>>>>>> 48ec4e7 (algo, doubly linked list, wip: delete() wip)

class TestDelete(unittest.TestCase):

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        s_list.delete(1)
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)


if __name__=="__main__":
    unittest.main()
