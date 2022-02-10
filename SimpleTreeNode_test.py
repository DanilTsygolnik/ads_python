import unittest
from SimpleTreeNode import *

class TestConstructor(unittest.TestCase):

    def test_root_node_no_value(self):
        root = SimpleTreeNode()
        self.assertIs(root.NodeValue, None)
        self.assertIs(root.Parent, None)
        self.assertEqual(root.Children, [])
        self.assertEqual(root.NodeLevel, 0)

    def test_root_node_with_value(self):
        root = SimpleTreeNode(5)
        self.assertEqual(root.NodeValue, 5)
        self.assertIs(root.Parent, None)
        self.assertEqual(root.Children, [])
        self.assertEqual(root.NodeLevel, 0)

    def test_node_with_parameters(self):
        root = SimpleTreeNode()
        node = SimpleTreeNode(5, root)
        self.assertEqual(node.NodeValue, 5)
        self.assertIs(node.Parent, root)
        self.assertEqual(node.Children, [])
        self.assertEqual(node.NodeLevel, 1) # the most important
        
    def test_node_level(self):
        node = SimpleTreeNode(5)
        node.NodeLevel = 3 # set up another level
        
        # validate node parameters
        self.assertEqual(node.NodeValue, 5)
        self.assertIs(node.Parent, None)
        self.assertEqual(node.Children, [])
        self.assertEqual(node.NodeLevel, 3)

        # main test
        test_node = SimpleTreeNode(3, node)
        self.assertEqual(test_node.NodeValue, 3)
        self.assertIs(test_node.Parent, node)
        self.assertEqual(test_node.Children, [])
        self.assertEqual(test_node.NodeLevel, 4) # the most important
        

if __name__=="__main__":
    unittest.main()
