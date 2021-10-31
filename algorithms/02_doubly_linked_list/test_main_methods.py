# pylint: disable=c0114,c0115,c0116,c0103
import unittest
import ctypes
from doubly_linked_list import LinkedList2
from doubly_linked_list import Node

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
def get_linked(nodes):
    s_list = LinkedList2()
    for i in nodes:
        s_list.add_in_tail(i)
    return s_list

<<<<<<< HEAD
class TestFind(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

class TestFindall(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), nodes)

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [])

    def test_long_single_node(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3]])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_all(1), [nodes[3], nodes[5]])
<<<<<<< HEAD
=======
=======
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
class TestFind(unittest.TestCase):

    def test_empty(self):
        nodes = []
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

    def test_one_node_pos(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[0])

    def test_one_node_neg(self):
        nodes = [Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), None)

<<<<<<< HEAD
    def test_even_nodes_num2(self):
        nodes = [Node(0), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find_bin(1), nodes[1])

    def test_odd_nodes_num1(self):
<<<<<<< HEAD
        self.s_list.add_in_tail(Node(0))
        self.assertEqual(self.s_list.find_bin(1), self.nodes[2])
>>>>>>> 995a631 (algo, doubly linked list, wip: add_in_tail(), get_all_nodes(), clean(), find() -- main tests ok)
=======
=======
    def test_long_single_node(self):
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(0), Node(0)]
        s_list = get_linked(nodes)
        self.assertEqual(s_list.find(1), nodes[3])

    def test_long_multiple_nodes(self):
        nodes = [Node(0), Node(0), Node(0), Node(1), Node(0), Node(1), Node(0)]
        s_list = get_linked(nodes)
<<<<<<< HEAD
        self.assertEqual(s_list.find_bin(1), nodes[4])
>>>>>>> eff4bf6 (algo, doubly linked list, wip: find_bin(): tests updated; done)
=======
        self.assertEqual(s_list.find(1), nodes[3])
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
=======
>>>>>>> 48ec4e7 (algo, doubly linked list, wip: delete() wip)

class TestDelete(unittest.TestCase):

    def test_single_node(self):
        nodes = [Node(1)]
        s_list = get_linked(nodes)
        s_list.delete(5)
        self.assertEqual(s_list.get_all_nodes(), nodes)
        s_list.delete(1)
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

    def test_long_multiple_nodes(self):
        nodes = [Node(1), Node(1), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        s_list.delete(1) # delete a single node from head ( [1->1->1->0->0->] >>> [1->1->0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[1:])
        self.assertIs(s_list.head, nodes[1])

        nodes = [Node(1), Node(1), Node(0), Node(0)]
        s_list = get_linked(nodes)
        s_list.delete(1, True) # delete multiple nodes from head ( [1->1->0->0->] >>> [0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[2:])
        self.assertIs(s_list.head, nodes[2])

        nodes = [Node(0), Node(0), Node(1), Node(1)]
        s_list = get_linked(nodes)
        s_list.delete(1, True) # delete nodes from tail ( [0->0->1->1->] >>> [0->0->] )
        self.assertEqual(s_list.get_all_nodes(), nodes[:2])
        self.assertIs(s_list.tail, nodes[1])

        s_list.delete(0, True) # delete all nodes from the list ( [0->0->] >>> [] )
        self.assertEqual(s_list.get_all_nodes(), [])
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

class TestLenClean(unittest.TestCase):
    def setUp(self):
        nodes = [Node(1), Node(1), Node(1), Node(0), Node(0)]
        self.s_list = get_linked(nodes)

    def tearDown(self):
        self.s_list = None

    def test_len(self):
        self.assertEqual(self.s_list.len(), 5)

    def test_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIs(self.s_list.head, self.s_list.tail)

class TestInsert(unittest.TestCase):

    def test_insert_empty_after_none(self):
        nodes = [Node(0)]
        s_list = LinkedList2()
        s_list.insert(None, nodes[0])
        self.assertIs(s_list.head, nodes[0])
        self.assertIs(s_list.tail, nodes[0])

    def test_insert_empty_after_not_none(self):
        s_list = LinkedList2()
        s_list.insert(Node(1), Node(0))
        self.assertIs(s_list.head, None)
        self.assertIs(s_list.tail, None)

    def test_insert_single_after_none(self):
        nodes = [Node(0), Node(1), Node(2)]
        s_list = LinkedList2()
        s_list.add_in_tail(nodes[0])
        s_list.insert(Node(5), nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes[:1])
        s_list.insert(None, nodes[1])
        self.assertEqual(s_list.get_all_nodes(), nodes[:2])
        s_list.insert(nodes[1], nodes[2])
        self.assertEqual(s_list.get_all_nodes(), nodes)

        s_list.insert(Node(5), Node(5))
        self.assertEqual(s_list.get_all_nodes(), nodes)
        nodes.append(Node(3))
        s_list.insert(None, nodes[3])
        self.assertEqual(s_list.get_all_nodes(), nodes)

class TestInsertFromPrev(unittest.TestCase):
    def setUp(self):
        self.memory_slots = (4*ctypes.py_object)()
        self.memory_slots[0] = Node(0) # node 1
        self.memory_slots[1] = Node(0) # node 2
        self.memory_slots[2] = Node(0) # node 3
        self.memory_slots[3] = Node(1) # newNode
        self.s_list = LinkedList2()
        for i in range(3):
            self.s_list.add_in_tail(self.memory_slots[i])
        self.newNode = self.memory_slots[3]

    def test_check_setup(self):
        val_list = []
        for i in self.memory_slots:
            val_list.append(str(i.value))
        values_str = "".join(val_list)

        self.assertEqual(values_str, "0001") # memory_slots fill check

        self.assertEqual(self.newNode.value, 1) # newNode check
        self.assertIsNone(self.newNode.next) # newNode check

        s_list_val_ref = [0,0,0] # s_list fill check
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), s_list_val_ref)

    def test_case_1(self): # список пустой, afterNode=None
        self.s_list.clean()
        self.s_list.insert(None, self.newNode)
        ref_list = [1]
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), ref_list)
        self.assertTrue(self.s_list.head is self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

    def test_case_2(self): # список пустой, afterNode!=None
        self.s_list.clean()
        afterNode = self.memory_slots[2]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [1]
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), ref_list)
        self.assertTrue(self.s_list.head is self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

    def test_case_4_1(self): # список не пустой, afterNode!=None -- 1st node
        afterNode = self.memory_slots[0]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,1,0,0]
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is not self.newNode)

    def test_case_4_2(self): # список не пустой, afterNode!=None -- 2nd node
        afterNode = self.memory_slots[1]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,0,1,0]
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is not self.newNode)

    def test_case_4_3(self): # список не пустой, afterNode!=None -- last node
        afterNode = self.memory_slots[2]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,0,0,1]
        self.assertEqual(self.s_list.get_all_nodes(as_val=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

if __name__=="__main__":
    unittest.main()
