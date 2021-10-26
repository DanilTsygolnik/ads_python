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

if __name__=="__main__":
    unittest.main()
