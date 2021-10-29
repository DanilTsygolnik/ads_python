# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from linked_list import LinkedList
from linked_list import Node
from linked_list import nodes_val_sums_list

class TestPrep(unittest.TestCase):
    def test_case_1(self):
        """Вернуть ошибку, если хотя бы один из аргументов - не связный список"""
        with self.assertRaises(TypeError):
            nodes_val_sums_list(None, LinkedList())
        with self.assertRaises(TypeError):
            nodes_val_sums_list(LinkedList(), None)
        with self.assertRaises(TypeError):
            nodes_val_sums_list(None, None)

    def test_case_2(self):
        """Вернуть ошибку, если длины списков не совпадают"""
        list1 = LinkedList()
        list1.add_in_tail(Node(1))
        self.assertEqual(list1.len(), 1)
        list2 = LinkedList()
        self.assertEqual(list2.len(), 0)

        with self.assertRaises(IndexError):
            nodes_val_sums_list(list1, list2)

class TestMain(unittest.TestCase):
    def setUp(self):
        self.list1 = LinkedList()
        self.list1.add_in_tail(Node(0))
        self.list1.add_in_tail(Node(0))
        self.list1.add_in_tail(Node(0))

        self.list2 = LinkedList()
        self.list2.add_in_tail(Node(1))
        self.list2.add_in_tail(Node(1))
        self.list2.add_in_tail(Node(1))

    def test_value_error_list1(self):
        self.list1.tail.value = '1'
        with self.assertRaises(ValueError):
            nodes_val_sums_list(self.list1, self.list2)

    def test_value_error_list2(self):
        self.list2.tail.value = '1'
        with self.assertRaises(ValueError):
            nodes_val_sums_list(self.list1, self.list2)

    def test_correct_result(self):
        self.assertEqual(nodes_val_sums_list(self.list1, self.list2), [1,1,1])
        self.list1 = LinkedList()
        self.list2 = LinkedList()
        self.assertEqual(nodes_val_sums_list(self.list1, self.list2), [])

if __name__=="__main__":
    unittest.main()
