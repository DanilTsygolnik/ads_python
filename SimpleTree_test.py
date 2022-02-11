import unittest
from SimpleTree import *
from SimpleTreeNode import *

class TestSimpleTree(unittest.TestCase):

    def setUp(self):
        self.root = SimpleTreeNode(0)
        self.node1 = SimpleTreeNode(1)
        self.node2 = SimpleTreeNode(2)
        self.node3 = SimpleTreeNode(3)
        self.node4 = SimpleTreeNode(4)
        self.node5 = SimpleTreeNode(5)

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

    def test_GetAllNodes(self):
        
        # tree with root
        self.assertEqual(self.tree.GetAllNodes(), [self.root])

        # root--node1
        self.tree.AddChild(self.tree.Root, self.node1)
        expected_result = set([self.root, self.node1])
        self.assertEqual(set(self.tree.GetAllNodes()), expected_result)

        # root--node1
        #    |--node2
        self.tree.AddChild(self.tree.Root, self.node2)
        expected_result.add(self.node2)
        self.assertEqual(set(self.tree.GetAllNodes()), expected_result)
        
        # root--node1
        #    |      |--node3
        #    |      |--node4
        #    |
        #    |--node2
        #           |--node5
        self.tree.AddChild(self.node1, self.node3)
        self.tree.AddChild(self.node1, self.node4)
        self.tree.AddChild(self.node2, self.node5)
        # test
        expected_result = set([self.root, self.node1, self.node2, self.node3, self.node4, self.node5])
        self.assertEqual(set(self.tree.GetAllNodes()), expected_result)


    def test_DeleteNode_assert_not_root(self):
        with self.assertRaises(AssertionError):
            self.tree.DeleteNode(self.root)

    def test_DeleteNode(self):
        # root--node1
        #    |      |--node3
        #    |      |--node4
        #    |
        #    |--node2
        #           |--node5
        self.tree.AddChild(self.tree.Root, self.node1)
        self.tree.AddChild(self.tree.Root, self.node2)
        self.tree.AddChild(self.node1, self.node3)
        self.tree.AddChild(self.node1, self.node4)
        self.tree.AddChild(self.node2, self.node5)

        self.tree.DeleteNode(self.node1)
        # expected result
        # root--node2--node5
        expected_result = set([self.root, self.node2, self.node5])
        self.assertEqual(set(self.tree.GetAllNodes()), expected_result)

    def test_FindNodesByValue(self):
        # root(0)--node1(1)
        #    |      |--node3(3)
        #    |      |--node4(4)
        #    |             |--node5(5)
        #    |
        #    |--node2(2)
        self.tree.AddChild(self.tree.Root, self.node1)
        self.tree.AddChild(self.tree.Root, self.node2)
        self.tree.AddChild(self.node1, self.node3)
        self.tree.AddChild(self.node1, self.node4)
        self.tree.AddChild(self.node4, self.node5)

        # no nodes with value
        self.assertEqual(self.tree.FindNodesByValue(100), [])

        # val==0, root
        self.assertEqual(self.tree.FindNodesByValue(0), [self.root])
 
        # val==5, deepest level node
        self.assertEqual(self.tree.FindNodesByValue(5), [self.node5])

        # all nodes
        self.node1.NodeValue = 0
        self.node2.NodeValue = 0
        self.node3.NodeValue = 0
        self.node4.NodeValue = 0
        self.node5.NodeValue = 0
        self.assertEqual(set(self.tree.FindNodesByValue(0)), set(self.tree.GetAllNodes()))

 
if __name__=="__main__":
    unittest.main()
