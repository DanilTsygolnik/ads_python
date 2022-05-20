# pylint: disable=c0103,c0114,c0115,c0116,c0301,r0903
import unittest
from BST import *

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

        self.node1.replace_with(self.node3, push_kids=True)
        self.assertIs(self.nodeA.RightChild, self.node3)
        self.assertIs(self.node3.Parent, self.nodeA)
        self.assertIs(self.node3.LeftChild, self.node2)
        self.assertIs(self.node3.RightChild, None)
        self.assertIs(self.node1.Parent, None)
        self.assertIs(self.node1.LeftChild, None)
        self.assertIs(self.node1.RightChild, None)


#class TestDeleteNodeByKey(unittest.TestCase):


if __name__=="__main__":
    unittest.main()
