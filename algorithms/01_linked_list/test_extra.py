# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from linked_list import LinkedList
from linked_list import Node
from linked_list import nodes_val_sums_list

class TestFunc(unittest.TestCase):
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
        list2 = LinkedList()
        self.assertEqual(list1.len(), 1)
        self.assertEqual(list2.len(), 0)
        with self.assertRaises(IndexError):
            nodes_val_sums_list(list1, list2)

if __name__=="__main__":
    unittest.main()
