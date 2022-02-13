# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import *

class TestFindNodeByKey(unittest.TestCase):

    def setUp(self):
        self.root = BSTNode(10, None, None)
        self.node6 = BSTNode(6, None, None)
        self.node8 = BSTNode(8, None, None)
        self.node12 = BSTNode(12, None, None)
        self.node14 = BSTNode(14, None, None)
        self.empty_tree = BST(None)
        self.tree = BST(self.root)


    def test_1(self):
        result = self.empty_tree.FindNodeByKey(10)
        expected = BSTFind()
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)


    def test_2(self):
        result = self.tree.FindNodeByKey(10)
        expected = BSTFind(self.root, True, False)
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)


    def test_3(self):
        result = self.tree.FindNodeByKey(8)
        expected = BSTFind(self.root, False, True)
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)

        self.root.LeftChild = self.node8
        self.node8.Parent = self.root

        result = self.tree.FindNodeByKey(6)
        expected = BSTFind(self.node8, False, True)
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)


    def test_4(self):
        result = self.tree.FindNodeByKey(12)
        expected = BSTFind(self.root, False, False)
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)

        self.root.RightChild = self.node12
        self.node12.Parent = self.root

        result = self.tree.FindNodeByKey(14)
        expected = BSTFind(self.node12, False, False)
        self.assertIs(expected.Node, result.Node)
        self.assertIs(expected.NodeHasKey, result.NodeHasKey)
        self.assertIs(expected.ToLeft, result.ToLeft)


if __name__=="__main__":
    unittest.main()
