# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import BSTNode, BST

class TestCount(unittest.TestCase):

    def test1_empty_tree_root_none(self):
        empty_tree = BST(None)
        self.assertEqual(empty_tree.Count(), 0)

    def test2_root_only(self):
        node10 = BSTNode(10, 10, None)
        tree = BST(node10)
        self.assertEqual(tree.Count(), 1)

    def test3_two_nodes(self):
        root = BSTNode(10, 10, None)
        node6 = BSTNode(6, 6, root)
        root.LeftChild = node6
        tree_child_at_left = BST(root)
        self.assertEqual(tree_child_at_left.Count(), 2)

        node14 = BSTNode(14, 14, root)
        root.LeftChild = None
        root.RightChild = node14
        tree_child_at_right = BST(root)
        self.assertEqual(tree_child_at_right.Count(), 2)

    def test_4(self):
        root = BSTNode(10, 10, None)
        node6 = BSTNode(6, 6, root)
        node14 = BSTNode(14, 14, root)
        root.LeftChild = node6
        root.RightChild = node14
        tree = BST(root)
        self.assertEqual(tree.Count(), 3)

    def test_5(self):
        root = BSTNode(10, 10, None)
        node2 = BSTNode(2, 2, root)
        node14 = BSTNode(14, 14, root)
        root.LeftChild = node2
        root.RightChild = node14
        node6 = BSTNode(6, 6, node2)
        node2.RightChild = node6
        node8 = BSTNode(8, 8, node6)
        node6.RightChild = node8
        tree = BST(root)
        self.assertEqual(tree.Count(), 5)


if __name__=="__main__":
    unittest.main()
