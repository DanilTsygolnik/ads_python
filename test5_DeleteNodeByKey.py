# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import BSTNode, BSTFind, BST

class TestBSTNode_replace_with(unittest.TestCase):

    def setUp(self):
        self.nodeA = BSTNode('A', 'A', None)
        self.nodeB = BSTNode('B', 'B', None)
        self.node1 = BSTNode(1, 1, None)
        self.node2 = BSTNode(2, 2, None)
        self.node3 = BSTNode(3, 3, None)
        self.node4 = BSTNode(4, 4, None)
        self.node5 = BSTNode(5, 5, None)
        self.node6 = BSTNode(6, 6, None)

    def test1(self):
        '''
        Узел nodeA - корень.
        Наследники:
          - nodeA.LeftChild = None
          - nodeA.RightChild = node1

        Узел node1 - наследник nodeA справа:
        Наследники:
          - node1.LeftChild = node2
          - node1.RightChild = node3

        Задача: удалить узел node1 из связки с nodeA (замена на None).
        '''
        # nodeA--node1
        self.nodeA.RightChild = self.node1
        self.node1.Parent = self.nodeA
        # node1--node2
        self.node1.LeftChild = self.node2
        self.node2.Parent = self.node1
        # node1--node3
        self.node1.RightChild = self.node3
        self.node3.Parent = self.node1

        self.node1.replace_with(None)
        self.assertIs(self.nodeA.RightChild, None)
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node1.LeftChild, self.node2)
        self.assertIs(self.node1.RightChild, self.node3)

    def test2(self):
        '''
        Узел nodeA - корень.
        Наследники:
          - nodeA.LeftChild = None
          - nodeA.RightChild = node1

        Узел node1 - наследник nodeA справа:
        Наследники:
          - node1.LeftChild = node2
          - node1.RightChild = node3

        Узел nodeB - корень.
        Наследники:
          - nodeB.LeftChild = node4
          - nodeB.RightChild = None

        Узел node4 - наследник nodeB слева:
        Наследники:
          - node4.LeftChild = node5
          - node4.RightChild = node6

        Задача: заменить узел node1 на node4.
        '''
        # nodeA--node1
        self.nodeA.RightChild = self.node1
        self.node1.Parent = self.nodeA
        # node1--node2
        self.node1.LeftChild = self.node2
        self.node2.Parent = self.node1
        # node1--node3
        self.node1.RightChild = self.node3
        self.node3.Parent = self.node1

        # nodeB--node4
        self.nodeB.LeftChild = self.node4
        self.node4.Parent = self.nodeB
        # node4--node5
        self.node4.LeftChild = self.node5
        self.node5.Parent = self.node4
        # node4--node6
        self.node4.RightChild = self.node6
        self.node6.Parent = self.node4

        self.node1.replace_with(self.node4)
        self.assertIs(self.nodeA.RightChild, self.node4)
        self.assertIs(self.node4.Parent, self.nodeA)
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.nodeB.LeftChild, None)


    def test3(self):
        '''
        Узел nodeA - корень.
        Наследники:
          - nodeA.LeftChild = None
          - nodeA.RightChild = node1

        Узел node1 - наследник nodeA справа:
        Наследники:
          - node1.LeftChild = node2
          - node1.RightChild = node3

        Узел node3 - наследник node1 справа:
        Наследники:
          - node3.LeftChild = None
          - node3.RightChild = node4

        Узел node4 - наследник node3 справа.
        Наследники:
          - node4.LeftChild = node5
          - node4.RightChild = node6

        Задача: заменить узел node1 на node4.
        '''
        # nodeA--node1
        self.nodeA.RightChild = self.node1
        self.node1.Parent = self.nodeA
        # node1--node2
        self.node1.LeftChild = self.node2
        self.node2.Parent = self.node1
        # node1--node3
        self.node1.RightChild = self.node3
        self.node3.Parent = self.node1

        # node3--node4
        self.node3.RightChild = self.node4
        self.node4.Parent = self.node3
        # node4--node5
        self.node4.LeftChild = self.node5
        self.node5.Parent = self.node4
        # node4--node6
        self.node4.RightChild = self.node6
        self.node6.Parent = self.node4

        self.node1.replace_with(self.node4)
        self.assertIs(self.nodeA.RightChild, self.node4)
        self.assertIs(self.node4.Parent, self.nodeA)
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node3.LeftChild, None)
        self.assertIs(self.node3.RightChild, None)

    def test4(self):
        '''
        Узел nodeA - корень.
        Наследники:
          - nodeA.LeftChild = None
          - nodeA.RightChild = node1

        Узел node1 - наследник nodeA справа:
        Наследники:
          - node1.LeftChild = node2
          - node1.RightChild = node3

        Задача: заменить узел node1 на node3 и передать
                наследников node1 узлу node3.
        '''
        # nodeA--node1
        self.nodeA.RightChild = self.node1
        self.node1.Parent = self.nodeA
        # node1--node2
        self.node1.LeftChild = self.node2
        self.node2.Parent = self.node1
        # node1--node3
        self.node1.RightChild = self.node3
        self.node3.Parent = self.node1

        self.node1.replace_with(self.node3, pass_kids_on=True)
        self.assertIs(self.nodeA.RightChild, self.node3)
        self.assertIs(self.node3.Parent, self.nodeA)
        self.assertIs(self.node3.LeftChild, self.node2)
        self.assertIs(self.node3.RightChild, None)
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node1.LeftChild, None)
        self.assertIs(self.node1.RightChild, None)


class TestDeleteNodeByKey(unittest.TestCase):

    def setUp(self):
        # 0 lnl
        self.node4 = BSTNode(4, '4', None)

        # 1 lvl
        # self.node4--self.node2
        self.node2 = BSTNode(2, '2', self.node4)
        self.node4.LeftChild = self.node2
        # self.node4--self.node6
        self.node6 = BSTNode(6, '6', self.node4)
        self.node4.RightChild = self.node6

        # 2 lvl
        # self.node2--self.node1
        self.node1 = BSTNode(1, '1', self.node2)
        self.node2.LeftChild = self.node1
        # self.node2--self.node3
        self.node3 = BSTNode(3, '3', self.node2)
        self.node2.RightChild = self.node3
        # self.node6--self.node5
        self.node5 = BSTNode(5, '5', self.node6)
        self.node6.LeftChild = self.node5
        # self.node6--self.node7
        self.node7 = BSTNode(7, '7', self.node6)
        self.node6.RightChild = self.node7

        # 3 lvl
        # self.node1--self.node0
        self.node0 = BSTNode(0, '0', self.node1)
        self.node1.LeftChild = self.node0
        # self.node7--self.node8
        self.node8 = BSTNode(8, '8', self.node7)
        self.node7.RightChild = self.node8


        self.bst = BST(self.node4)

    def tests(self):
        self.assertIs(self.bst.DeleteNodeByKey(9),False)
        self.assertEqual(self.bst.Count(),9)

        self.assertIs(self.bst.DeleteNodeByKey(3),True)
        self.assertEqual(self.bst.Root,self.node4)
        self.assertIs(self.node2.RightChild,None)
        self.assertEqual(self.node2.LeftChild,self.node1)
        self.assertIs(self.node3.Parent,None)
        self.assertIs(self.node3.LeftChild,None)
        self.assertIs(self.node3.RightChild,None)
        self.assertEqual(self.node1.LeftChild.NodeKey,0)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.bst.Count(),8)

        self.assertIs(self.bst.DeleteNodeByKey(2),True)
        self.assertEqual(self.bst.Root,self.node4)
        self.assertIs(self.node2.Parent,None)
        self.assertIs(self.node2.LeftChild,None)
        self.assertIs(self.node2.RightChild,None)
        self.assertEqual(self.node1.Parent,self.node4)
        self.assertEqual(self.node1.LeftChild.NodeKey,0)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.node4.LeftChild,self.node1)
        self.assertEqual(self.node4.RightChild,self.node6)
        self.assertEqual(self.bst.Count(),7)

        self.assertIs(self.bst.DeleteNodeByKey(6),True)
        self.assertEqual(self.bst.Root,self.node4)
        self.assertEqual(self.node4.LeftChild,self.node1)
        self.assertEqual(self.node4.RightChild,self.node7)
        self.assertEqual(self.node1.Parent,self.node4)
        self.assertEqual(self.node1.LeftChild.NodeKey,0)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.node7.Parent,self.node4)
        self.assertEqual(self.node5.Parent,self.node7)
        self.assertIs(self.node5.LeftChild,None)
        self.assertIs(self.node5.RightChild,None)
        self.assertEqual(self.node7.LeftChild,self.node5)
        self.assertEqual(self.node7.RightChild.NodeKey,8)
        self.assertIs(self.node6.Parent,None)
        self.assertIs(self.node6.LeftChild,None)
        self.assertIs(self.node6.RightChild,None)
        self.assertEqual(self.bst.Count(),6)

        self.assertIs(self.bst.DeleteNodeByKey(4),True)
        self.assertEqual(self.node5.LeftChild,self.node1)
        self.assertEqual(self.node1.Parent,self.node5)
        self.assertEqual(self.node1.LeftChild.NodeKey,0)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.node5.RightChild,self.node7)
        self.assertEqual(self.node7.RightChild.NodeKey,8)
        self.assertIs(self.node7.LeftChild,None)
        self.assertIs(self.node6.Parent,None)
        self.assertIs(self.node6.LeftChild,None)
        self.assertIs(self.node6.RightChild,None)
        self.assertEqual(self.bst.Root,self.node5)
        self.assertIs(self.node5.Parent,None)
        self.assertIs(self.node4.Parent,None)
        self.assertIs(self.node4.LeftChild,None)
        self.assertIs(self.node4.RightChild,None)
        self.assertEqual(self.bst.Count(),5)

        self.assertIs(self.bst.DeleteNodeByKey(8),True)
        self.assertEqual(self.node5.LeftChild,self.node1)
        self.assertEqual(self.node1.Parent,self.node5)
        self.assertEqual(self.node1.LeftChild.NodeKey,0)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.node5.RightChild,self.node7)
        self.assertIs(self.node7.RightChild,None)
        self.assertIs(self.node7.LeftChild,None)
        self.assertIs(self.node6.Parent,None)
        self.assertIs(self.node6.LeftChild,None)
        self.assertIs(self.node6.RightChild,None)
        self.assertEqual(self.bst.Root,self.node5)
        self.assertIs(self.node5.Parent,None)
        self.assertIs(self.node4.Parent,None)
        self.assertIs(self.node4.LeftChild,None)
        self.assertIs(self.node4.RightChild,None)
        self.assertEqual(self.bst.Count(),4)

        self.assertIs(self.bst.DeleteNodeByKey(0),True)
        self.assertEqual(self.node5.LeftChild,self.node1)
        self.assertEqual(self.node1.Parent,self.node5)
        self.assertIs(self.node1.LeftChild,None)
        self.assertIs(self.node1.RightChild,None)
        self.assertEqual(self.node5.RightChild,self.node7)
        self.assertIs(self.node7.RightChild,None)
        self.assertIs(self.node7.LeftChild,None)
        self.assertIs(self.node6.Parent,None)
        self.assertIs(self.node6.LeftChild,None)
        self.assertIs(self.node6.RightChild,None)
        self.assertEqual(self.bst.Root,self.node5)
        self.assertIs(self.node5.Parent,None)
        self.assertIs(self.node4.Parent,None)
        self.assertIs(self.node4.LeftChild,None)
        self.assertIs(self.node4.RightChild,None)
        self.assertEqual(self.bst.Count(),3)

        self.bst.DeleteNodeByKey(1)

        self.assertIs(self.bst.DeleteNodeByKey(7),True)
        self.assertEqual(self.bst.Root,self.node5)
        self.assertIs(self.node5.RightChild,None)
        self.assertIs(self.node5.LeftChild,None)
        self.assertIs(self.node7.Parent,None)
        self.assertIs(self.node7.LeftChild,None)
        self.assertIs(self.node7.RightChild,None)
        self.assertIs(self.node1.Parent,None)

        self.assertIs(self.bst.DeleteNodeByKey(5),True)
        self.assertIs(self.bst.Root,None)
        self.assertIs(self.node5.LeftChild,None)
        self.assertIs(self.node5.RightChild,None)
        self.assertIs(self.node5.Parent,None)
        self.assertEqual(self.bst.Count(),0)

        self.assertIs(self.bst.DeleteNodeByKey(5),False)


if __name__=="__main__":
    unittest.main()
