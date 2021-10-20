import ctypes
import unittest
import linked_list

class TestLinkedList(unittest.TestCase):
    
    def test_linked_list_len(self):
        memory_slots = (8*ctypes.py_object)()
        
        memory_slots[0] = linked_list.Node(0) # node 1
        memory_slots[1] = linked_list.Node(0) # node 2
        memory_slots[2] = linked_list.Node(0) # node 3
        memory_slots[3] = linked_list.Node(1) # node 4
        memory_slots[4] = linked_list.Node(0) # node 5
        memory_slots[5] = linked_list.Node(0) # node 6
        memory_slots[6] = linked_list.Node(0) # node 7
        
        # newNode
        memory_slots[7] = linked_list.Node(9) # node 8

        s_list = linked_list.LinkedList()
        for i in range(7):
            s_list.add_in_tail(memory_slots[i])
        
        newNode = memory_slots[7]

        # test 1 - insert as a new head
        s_list.insert(None, newNode)
        ref_list = [9, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(s_list.print_all_nodes(as_list=True), ref_list)
        s_list.delete(9, True)

        # test 2 - insert after random node
        afterNode = memory_slots[3]
        s_list.insert(afterNode, newNode)
        ref_list = [0, 0, 0, 1, 9, 0, 0, 0]
        self.assertEqual(s_list.print_all_nodes(as_list=True), ref_list)
        s_list.delete(9, True)

        # test 3 - insert as a new tail
        afterNode = s_list.tail
        s_list.insert(afterNode, newNode)
        ref_list = [0, 0, 0, 1, 0, 0, 0, 9]
        self.assertEqual(s_list.print_all_nodes(as_list=True), ref_list)
        s_list.delete(9, True)


if __name__ == "__main__":
    unittest.main()
