import ctypes
import unittest
import linked_list

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.memory_slots = (4*ctypes.py_object)()
        self.memory_slots[0] = linked_list.Node(0) # node 1
        self.memory_slots[1] = linked_list.Node(0) # node 2
        self.memory_slots[2] = linked_list.Node(0) # node 3
        self.memory_slots[3] = linked_list.Node(1) # newNode
        self.s_list = linked_list.LinkedList()
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

        s_list_val_ref = [0,0,0]
        self.assertEqual(self.s_list.print_all_nodes(as_list=True), s_list_val_ref) # s_list fill check

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

if __name__ == "__main__":
    unittest.main()
