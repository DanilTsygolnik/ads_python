import ctypes
import unittest
import linked_list

class TestLinkedList(unittest.TestCase):
    
    # Cases for the tests:
    # _case_1 список пустой, afterNode=None
    # _case_2 список пустой, afterNode!=None
    # _case_3 список не пустой, afterNode=None
    # _case_4 список не пустой, afterNode!=None
    
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


    #def test_linked_list_len(self):

    #    # test 1 - insert as a new head
    #    s_list.insert(None, newNode)
    #    ref_list = [9, 0, 0, 0, 1, 0, 0, 0]
    #    self.assertEqual(s_list.print_all_nodes(as_list=True), ref_list)
    #    s_list.delete(9, True)


if __name__ == "__main__":
    unittest.main()
