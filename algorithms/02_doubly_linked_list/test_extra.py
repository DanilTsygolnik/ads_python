# pylint: disable=c0114,c0115,c0116,c0103
import unittest
from dll_extra import *

def get_linked(nodes):
    s_list = LinkedList2()
    for i in nodes:
        s_list.add_in_tail(i)
    return s_list

class TestAddInHead(unittest.TestCase):
    def test_main(self):
        """
        Add node in empty list
        case 1: empty list;
        case 2: not empty list.
        """
        nodes = [Node(0), Node(1), Node(2)]

        # case 1
        s_list = LinkedList2()
        s_list.add_in_head(nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes[2:]) # [2->]
        self.assertTrue(all([s_list.head.next is nodes[2], s_list.tail.prev is nodes[2]]))
        

        # case 2
        s_list.add_in_head(nodes[1])
        self.assertEqual(s_list.get_all_nodes(), nodes[1:]) # [2->] ==> [1->2->]
        self.assertTrue(all([s_list.head.next is nodes[1], s_list.tail.prev is nodes[2]]))
        s_list.add_in_head(nodes[0])
        self.assertEqual(s_list.get_all_nodes(), nodes) # [1->2->] ==> [0->1->2->] 
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[2]]))

class TestAddInTail(unittest.TestCase):
    def test_main(self):
        """
        Add node in empty list
        case 1: empty list;
        case 2: not empty list.
        """
        nodes = [Node(0), Node(1), Node(2)]

        # case 1
        s_list = LinkedList2()
        s_list.add_in_tail(nodes[0])
        self.assertEqual(s_list.get_all_nodes(), [nodes[0]]) # [0->]
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[0]]))

        # case 2
        s_list.add_in_tail(nodes[1])
        self.assertEqual(s_list.get_all_nodes(), nodes[:2]) # [0->1->]
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[1]]))
        s_list.add_in_tail(nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes) # [0->1->2->]
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[2]]))

class TestInsert(unittest.TestCase):

    def test_case_1(self):
        """
        Case 1.1: Linked list is empty; afterNode is in list.
        Case 1.2: Linked list is empty; afterNode is not in list.

        Checked result:
            self.head.next=self.tail.prev=newNode
        """
        nodes = [Node(0)]
        s_list = LinkedList2()
        # case 1.1
        s_list.insert(None, nodes[0])
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[0]]))
        s_list.clean()
        # case 1.2
        s_list.insert(Node(1), nodes[0])
        self.assertTrue(all([s_list.head.next is nodes[0], s_list.tail.prev is nodes[0]]))

    def test_case_2(self):
        """
        Linked list contains a single node: [0->]
        Case 2.1: afterNode is not in list -- no changes.
        Case 2.2: afterNode=None -- add newNode in tail.
        Case 2.3: afterNode is in list (the last node) -- add newNode in tail.
        Case 2.4: as prev case; afterNode=None -- add newNode in tail.
        Case 2.5: afterNode is inside long list.
        """
        # case 2.1
        nodes = [Node(0), Node(1), Node(2)]
        s_list = LinkedList2()
        s_list.add_in_tail(nodes[0])
        s_list.insert(Node(5), nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes[:1])

        # case 2.2
        s_list.insert(None, nodes[1])
        self.assertEqual(s_list.get_all_nodes(), nodes[:2])
        self.assertIs(s_list.tail.prev, nodes[1])

        # case 2.3
        s_list.insert(nodes[1], nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes)
        self.assertIs(s_list.tail.prev, nodes[2])

        # case 2.4
        nodes.append(Node(3)) # nodes = [Node(0), Node(1), Node(2), Node(3)]
        s_list.insert(None, nodes[3])
        self.assertEqual(s_list.get_all_nodes(), nodes)
        self.assertIs(s_list.tail.prev, nodes[3])

        # case 2.5
        inp_node = Node(5)
        nodes.insert(2, inp_node) # nodes = [Node(0), Node(1), Node(5), Node(2), Node(3)]
        self.assertNotEqual(s_list.get_all_nodes(), nodes)
        s_list.insert(nodes[1], nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes)

if __name__=="__main__":
    unittest.main()
