# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import *

class TestBSTNode_replace_with(unittest.TestCase):

    def setUp(self):
        self.nodeA = BSTNode('A', 'A', None)
        self.node1 = BSTNode(1, 1, None)
        self.node2 = BSTNode(2, 2, None)

    def test1(self):
        '''
        Узел nodeA - родитель узла node1.
        Узел node1 - наследник nodeA слева.
        Задача: удалить узел node1 из связки с nodeA (замена на None).
        '''
        self.nodeA.LeftChild = self.node1
        self.node1.Parent = self.nodeA
        
        self.node1.replace_with(None)
        self.assertIs(self.nodeA.LeftChild, None)
        self.assertIs(self.node1.Parent, None)

    def test2(self):
        '''
        Узел nodeA - родитель узла node1.
        Узел node1 - наследник nodeA слева.
        Узел node2 - orphan.
        Задача: заменить узел node1 в связке с NodeA на node2.
        '''
        # nodeA--node1
        self.nodeA.LeftChild = self.node1
        self.node1.Parent = self.nodeA
        
        self.node1.replace_with(self.node2)
        # nodeA--node2
        self.assertIs(self.nodeA.LeftChild, node2)
        self.assertIs(self.node2.Parent, nodeA)
        # node1 became orphan
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node1.LeftChild, None)

    def test3(self):
        '''
        Узел nodeA - родитель узла node1.
        Узел node1 - наследник nodeA слева.
        Узел node2 - наследник node1 слева.
        Задача: заменить узел node1 в связке с NodeA на node2.
        '''
        # nodeA--node1
        self.nodeA.LeftChild = self.node1
        self.node1.Parent = self.nodeA
        # node1--node2
        self.node1.LeftChild = self.node2
        self.node2.Parent = self.node1
        
        self.node1.replace_with(self.node2)
        # nodeA--node2
        self.assertIs(self.nodeA.LeftChild, node2)
        self.assertIs(self.node2.Parent, nodeA)
        # node1 became orphan
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node1.LeftChild, None)


'''
Тест 4
_____
Заменить узел n1 с родителем (n1.Parent=nodeA; nodeA.LeftChild=n1) на узел n2 c родителем (n2.Parent.RightChild=nodeB; nodeB.RightChild=n2)
В итоге (на бумаге ок):
nodeA.LeftChild=n2
nodeB.RightChild=None
n2.Parent=nodeA
n1.Parent=None
```


class TestDeleteNodeByKey(unittest.TestCase):

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
