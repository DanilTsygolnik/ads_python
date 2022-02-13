# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import *

class TestAddKeyValue(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(10, 10, None)
        self.empty_tree = BST(None)
        self.tree = BST(self.root)


    def test_1(self):
        result = self.tree.AddKeyValue(10, 10)
        expected = False 
        self.assertIs(expected, result)


    def test_2(self):
        result = self.empty_tree.AddKeyValue(10, 10)
        expected = True
        self.assertIs(expected, result)
        self.assertEqual(self.empty_tree.Root.NodeKey, 10)
        self.assertEqual(self.empty_tree.Root.NodeValue, 10)
        self.assertIs(self.empty_tree.Root.Parent, None)


    def test_3(self):
        result = self.tree.AddKeyValue(8,8)
        expected = True
        self.assertIs(expected, result)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 8)
        self.assertEqual(self.tree.Root.LeftChild.NodeValue, 8)
        self.assertIs(self.tree.Root.LeftChild.Parent, self.root)


    def test_4(self):
        result = self.tree.AddKeyValue(12,12)
        expected = True
        self.assertIs(expected, result)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.tree.Root.RightChild.NodeValue, 12)
        self.assertIs(self.tree.Root.RightChild.Parent, self.root)


if __name__=="__main__":
    unittest.main()
