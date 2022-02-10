import unittest
from SimpleTree import *
from SimpleTreeNode import *

class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        self.root = SimpleTreeNode(0)
        self.node1 = SimpleTreeNode(1)
        self.node2 = SimpleTreeNode(2)
        self.node3 = SimpleTreeNode(3)

        self.empty_tree = SimpleTree()
        self.tree = SimpleTree(self.root)

    def test_SimpleTree_constructor(self):
        self.assertIs(self.empty_tree.Root, None)        
        self.assertIs(self.tree.Root, self.root)

    def test_AddChild(self):
        self.tree.AddChild(self.tree.Root, self.node1)
        self.assertEqual(self.tree.Root.Children, [self.node1])
        self.assertIs(self.node1.Parent, self.root)

        self.tree.AddChild(self.node1, self.node2)
        self.assertEqual(self.node1.Children, [self.node2])
        self.assertIs(self.node2.Parent, self.node1)

        self.tree.AddChild(self.node1, self.node3)
        self.assertEqual(self.node1.Children, [self.node2, self.node3])
        self.assertIs(self.node3.Parent, self.node1)

 
if __name__=="__main__":
    unittest.main()
