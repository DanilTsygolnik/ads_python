# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import *

class TestAddKeyValue(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(10, 10, None)
        self.tree = BST(self.root)


    def test_1(self):
        # empty tree
        self.empty_tree = BST(None)
        result = self.empty_tree.FinMinMax(self.empty_tree.Root, True)
        expected = None
        self.assertIs(expected, result)

        # only root
        result = self.tree.FinMinMax(self.tree.Root, False)
        expected = self.root
        self.assertIs(expected, result)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertIs(expected, result)


    def test_2(self):
        self.tree.AddKeyValue(6, None)
        self.tree.AddKeyValue(4, None)
        self.tree.AddKeyValue(2, None)
        self.tree.AddKeyValue(5, None)
        self.tree.AddKeyValue(8, None)
        self.tree.AddKeyValue(14, None)
        self.tree.AddKeyValue(12, None)
        self.tree.AddKeyValue(16, None)
        # entire tree
        result = self.tree.FinMinMax(self.tree.Root, False).NodeKey
        expected = 2
        self.assertEqual(expected, result)
        result = self.tree.FinMinMax(self.tree.Root, True).NodeKey # max
        expected = 16 
        self.assertEqual(expected, result)
        # left subtree
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, False).NodeKey
        expected = 2
        self.assertEqual(expected, result)
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, True).NodeKey # max
        expected = 8 
        self.assertEqual(expected, result)
        # right subtree
        result = self.tree.FinMinMax(self.tree.Root.RightChild, False).NodeKey
        expected = 12
        self.assertEqual(expected, result)
        result = self.tree.FinMinMax(self.tree.Root.RightChild, True).NodeKey # max
        expected = 16 
        self.assertEqual(expected, result)


if __name__=="__main__":
    unittest.main()
