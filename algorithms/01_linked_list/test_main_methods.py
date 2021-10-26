# pylint: disable=c0114,c0115,c0116,c0103
import ctypes
import unittest
from linked_list import LinkedList
from linked_list import Node

class TestDelete(unittest.TestCase):
    def setUp(self):

        self.s_list_1 = LinkedList()
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(0))
        self.s_list_1.add_in_tail(Node(1))
        self.s_list_1.add_in_tail(Node(0))

        self.s_list_2 = LinkedList()
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(0))
        self.s_list_2.add_in_tail(Node(1))
        self.s_list_2.add_in_tail(Node(1))
        self.s_list_2.add_in_tail(Node(1))

        self.s_list_3 = LinkedList()
        self.s_list_3.add_in_tail(Node(1))
        self.s_list_3.add_in_tail(Node(1))
        self.s_list_3.add_in_tail(Node(1))

    def tearDown(self):
        self.s_list_1 = None
        self.s_list_2 = None
        self.s_list_3 = None

    def test_case_1(self):
        """
        s_list_1 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        remove_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [ 1, 1, 1, 0, 1, 0]
        ожидаемый список значений [1, 1, 0, 1, 0]
        """
        nodes_val_ref = [1, 1, 0, 1, 0]
        self.s_list_1.delete(1, remove_all=False)
        nodes_val_after_del = self.s_list_1.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_2(self):
        """
        s_list_1 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        remove_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [1, 1, 1, 0, 1, 0]
        ожидаемый список значений [0, 0]
        """
        nodes_val_ref = [0, 0]
        self.s_list_1.delete(1, remove_all=True)
        nodes_val_after_del = self.s_list_1.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_3(self):
        """
        s_list_2 .....| 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> |.....

        remove_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [0, 0, 0, 1, 1, 1]
        ожидаемый список значений [0, 0, 0, 1, 1]
        """
        nodes_val_ref = [0, 0, 0, 1, 1]
        self.s_list_2.delete(1, remove_all=False)
        nodes_val_after_del = self.s_list_2.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_4(self):
        """
        s_list_2 .....| 1 -> 1 -> 1 -> 0 -> 1 -> 0 ->|.....

        remove_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [0, 0, 0, 1, 1, 1]
        ожидаемый список значений [0, 0, 0]
        """
        nodes_val_ref = [0, 0, 0]
        self.s_list_2.delete(1, remove_all=True)
        nodes_val_after_del = self.s_list_2.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)

    def test_case_5(self):
        """
        s_list_3 .....| 1 -> 1 -> 1 -> |.....

        remove_all=False -- удаление первого найденного узла со значением node.value == 1
        исходный список значений  [1, 1, 1]
        ожидаемый список значений [1, 1]
        """
        nodes_val_ref = [1, 1]
        self.s_list_3.delete(1, remove_all=False)
        nodes_val_after_del = self.s_list_3.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)
        self.assertIsNot(self.s_list_3.head, self.s_list_3.tail)

    def test_case_6(self):
        """
        s_list_3 .....| 1 -> 1 -> 1 -> |.....

        remove_all=True -- удаление всех найденных узлов со значением node.value == 1
        исходный список значений  [1, 1, 1]
        ожидаемый список значений []
        """
        nodes_val_ref = []
        self.s_list_3.delete(1, remove_all=True)
        nodes_val_after_del = self.s_list_3.print_all_nodes(as_list=True)
        self.assertEqual(nodes_val_ref, nodes_val_after_del)
        self.assertIs(self.s_list_3.head, None)
        self.assertIs(self.s_list_3.tail, None)
        self.assertIs(self.s_list_3.head, self.s_list_3.tail)

class TestFindall(unittest.TestCase):
    def test_findall(self):
        s_list = LinkedList()
        nodes = (6 * ctypes.py_object)()
        nodes[0] = Node(0)
        nodes[1] = Node(1)
        nodes[2] = Node(0)
        nodes[3] = Node(1)
        nodes[4] = Node(0)
        nodes[5] = Node(1)

        nodes_ref = [nodes[1], nodes[3], nodes[5]]

        self.assertEqual(s_list.find_all(1), [])

        for i in nodes:
            s_list.add_in_tail(i)

        self.assertEqual(s_list.find_all(1), nodes_ref)

        s_list = None
        nodes = None

class TestLenClean(unittest.TestCase):
    def setUp(self):
        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(1))

    def tearDown(self):
        self.s_list = None

    def test_len(self):
        self.assertEqual(self.s_list.len(), 6)

    def test_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIs(self.s_list.head, self.s_list.tail)

class TestInsert(unittest.TestCase):
    def setUp(self):
        self.memory_slots = (4*ctypes.py_object)()
        self.memory_slots[0] = Node(0) # node 1
        self.memory_slots[1] = Node(0) # node 2
        self.memory_slots[2] = Node(0) # node 3
        self.memory_slots[3] = Node(1) # newNode
        self.s_list = LinkedList()
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
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), s_list_val_ref)

    def test_case_1(self): # список пустой, afterNode=None
        self.s_list.clean()
        self.s_list.insert(None, self.newNode)
        ref_list = [1]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

    def test_case_2(self): # список пустой, afterNode!=None
        self.s_list.clean()
        afterNode = self.memory_slots[2]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [1]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

    def test_case_3(self): # список не пустой, afterNode=None
        self.s_list.insert(None, self.newNode)
        ref_list = [1,0,0,0]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is self.newNode)
        self.assertTrue(self.s_list.tail is not self.newNode)

    def test_case_4_1(self): # список не пустой, afterNode!=None -- 1st node
        afterNode = self.memory_slots[0]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,1,0,0]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is not self.newNode)

    def test_case_4_2(self): # список не пустой, afterNode!=None -- 2nd node
        afterNode = self.memory_slots[1]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,0,1,0]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is not self.newNode)

    def test_case_4_3(self): # список не пустой, afterNode!=None -- last node
        afterNode = self.memory_slots[2]
        self.s_list.insert(afterNode, self.newNode)
        ref_list = [0,0,0,1]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), ref_list)
        self.assertTrue(self.s_list.head is not self.newNode)
        self.assertTrue(self.s_list.tail is self.newNode)

if __name__=="__main__":
    unittest.main()
