import ctypes
import unittest
from linked_list import LinkedList
from linked_list import Node

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.nodes = []

        self.nodes.append(Node(0))
        self.nodes.append(Node(0))
        self.nodes.append(Node(0))
        self.nodes.append(Node(0))

        self.s_list = LinkedList()
        for i in self.nodes:
            self.s_list.add_in_tail(i)

    def tearDown(self):
        self.nodes = None
        self.s_list = None

    def test_linked_lists_no_ctypes(self):
        """
        При объявлении нового связного списка в памяти создается отдельный объект.
        Т.е. вручную резервировать ячейки в памяти под экземпляры связных списков не нужно.
        """
        list_one = LinkedList()
        list_two = LinkedList()
        self.assertIsNot(list_one, list_two)

    def test_nodes_no_ctypes(self):
        """
        При объявлении нового узла в памяти создается отдельный объект.
        Т.е. вручную резервировать ячейки в памяти под экземпляры отдельных узлов не нужно.
        """
        node_one = Node(0)
        node_two = Node(0)
        self.assertIsNot(node_one, node_two)

        node_one.next = node_two
        self.assertIs(node_one.next, node_two)
        self.assertIs(node_two.next, None)
        self.assertIsNot(node_one, node_two)

    def test_nodes_add(self):
        test_list = LinkedList()
        test_list.add_in_tail(Node(0))
        test_list.add_in_tail(Node(1))
        self.assertNotEqual(test_list.print_all_nodes(as_list=True), [0])
        self.assertEqual(test_list.print_all_nodes(as_list=True), [0, 1])

if __name__=="__main__":
    unittest.main()
