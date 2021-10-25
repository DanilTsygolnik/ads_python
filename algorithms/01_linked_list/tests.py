import ctypes
import unittest
from linked_list import LinkedList
from linked_list import Node

class TestLinkedList(unittest.TestCase):
    
    def test_delete(self):
        
        # логика тестов
        # -------------
        # > для каждого из 4-х случаев создать связный список

        # > для каждого случая:
        #    > получить соотв. связный список
        #    > вывести значения узлов в nodes_val_ref
        #    > провести удаление узлов
        #    > вывести значения узлов в nodes_val_after_del
        #    > сравнить nodes_val_after_del и nodes_val_ref -- должны совпасть

        #case_id_list = [1, 2, 3, 4, 5, 6, 7]  # problem at 1
        case_id_list = [1, 2, 3, 4, 5, 6, 7]
        
        for case_id in case_id_list:

            memory_slots = (13*ctypes.py_object)()
            
            memory_slots[0] = Node(0) # node 1
            memory_slots[1] = Node(0) # node 2
            memory_slots[2] = Node(0) # node 3
            memory_slots[3] = Node(1) # node 4
            memory_slots[4] = Node(0) # node 5
            memory_slots[5] = Node(0) # node 6
            memory_slots[6] = Node(0) # node 7
            memory_slots[7] = Node(1) # node 8
            memory_slots[8] = Node(1) # node 9
            memory_slots[9] = Node(1) # node 10
            memory_slots[10] = Node(0) # node 11
            memory_slots[11] = Node(0) # node 12
            memory_slots[12] = Node(0) # node 13
            
            #case_id = 1, remove_all=False -- удаление первого найденного узла со значением node.value == 1
            #.....| 0 -> 0 -> 0 -> 1 -> 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> 0 -> 0 -> 0 ->|.....
            #список значений до удаления [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
            #список значений после удаления первого найденного [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
            
            if case_id == 1:
                s_list = LinkedList()
                for i in range(13):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
                s_list.delete(1, remove_all=False)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True) 
            
            #case_id = 2, remove_all=True -- удаление всех найденных узлов со значением node.value == 1
            #.....| 0 -> 0 -> 0 -> 1 -> 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> 0 -> 0 -> 0 ->|.....
            #список значений до удаления [ 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
            #список значений после удаления всех узлов [ 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
            if case_id == 2:
                s_list = LinkedList()
                for i in range(13):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                s_list.delete(1, remove_all=True)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
            
            #case_id = 3, remove_all=False
            #.....| 1 -> 1 -> 1 -> 0 -> 0 -> 0 -> |.....
            #список значений после удаления первого найденного [1, 1, 0, 0, 0]
            
            if case_id == 3:
                s_list = LinkedList()
                for i in range(7, 13):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [1, 1, 0, 0, 0]
                s_list.delete(1, remove_all=False)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
        
            #case_id = 4, remove_all=True
            #.....| 1 -> 1 -> 1 -> 0 -> 0 -> 0 -> |.....
            #список значений узлов после удаления всех узлов [0, 0, 0]
            
            if case_id == 4:
                s_list = LinkedList()
                for i in range(7, 13):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [0, 0, 0]
                s_list.delete(1, remove_all=True)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
            
            #case_id = 5, remove_all=False
            #.....| 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> |..... 4,10
            #список значений после удаления первого найденного [0, 0, 0, 1, 1]
            
            if case_id == 5:
                s_list = LinkedList()
                for i in range(4, 10):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [0, 0, 0, 1, 1]
                s_list.delete(1, remove_all=False)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
            
            #case_id = 6, remove_all=True
            #.....| 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> |..... 4,10
            #список значений узлов после удаления всех узлов (X = 1) [0, 0, 0]
            
            if case_id == 6:
                s_list = LinkedList()
                for i in range(4, 10):
                    s_list.add_in_tail(memory_slots[i])
                nodes_val_ref = [0, 0, 0]
                s_list.delete(1, remove_all=True)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
            
            #case_id = 7 -- 1) remove_all=False; 2) remove_all
            #.....| 1 -> 1 -> 1 -> |..... 7,10
            #список значений после удаления первого найденного [1, 1]
            #список значений узлов после удаления всех узлов []
            
            if case_id == 7:
                s_list = LinkedList()
                for i in range(7, 10):
                    s_list.add_in_tail(memory_slots[i])
                # test remove_all=False
                nodes_val_ref = [1, 1]
                s_list.delete(1, remove_all=False)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
                self.assertEqual(nodes_val_after_del, nodes_val_ref) 
                # test remove_all
                nodes_val_ref = []
                s_list.delete(1, remove_all=True)
                nodes_val_after_del = s_list.print_all_nodes(as_list=True)
            
            # для каждого случая (после if, но в цикле for)
            self.assertEqual(nodes_val_after_del, nodes_val_ref)

    def test_linked_list_len(self):
        memory_slots = (13*ctypes.py_object)()
        
        memory_slots[0] = Node(0) # node 1
        memory_slots[1] = Node(0) # node 2
        memory_slots[2] = Node(0) # node 3
        memory_slots[3] = Node(1) # node 4
        memory_slots[4] = Node(0) # node 5
        memory_slots[5] = Node(0) # node 6
        memory_slots[6] = Node(0) # node 7
        memory_slots[7] = Node(1) # node 8
        memory_slots[8] = Node(1) # node 9
        memory_slots[9] = Node(1) # node 10
        memory_slots[10] = Node(0) # node 11
        memory_slots[11] = Node(0) # node 12
        memory_slots[12] = Node(0) # node 13

        s_list = LinkedList()
        for i in range(13):
            s_list.add_in_tail(memory_slots[i])
        
        self.assertEqual(s_list.len(), 13)
        s_list.clean()
        self.assertEqual(s_list.len(), 0)

if __name__ == "__main__":
    unittest.main()
