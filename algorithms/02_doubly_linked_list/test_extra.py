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

if __name__=="__main__":
    unittest.main()
