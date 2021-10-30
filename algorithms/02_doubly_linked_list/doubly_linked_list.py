<<<<<<< HEAD
#pylint: disable=c0114,c0115,c0116,c0103
=======
>>>>>>> 995a631 (algo, doubly linked list, wip: add_in_tail(), get_all_nodes(), clean(), find() -- main tests ok)
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

<<<<<<< HEAD
    def wipe_links(self):
        self.next = None
        self.prev = None

=======
>>>>>>> 995a631 (algo, doubly linked list, wip: add_in_tail(), get_all_nodes(), clean(), find() -- main tests ok)
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def get_all_nodes(self, as_val=False):
        """
        Метод отладочного вывода значений всех узлов связного списка
        По умолчанию выводит на экран значение каждого узла
        При as_list=True возвращает список значений узлов
        """
        node = self.head
        nodes = []
        nodes_values = []
        while node is not None:
            nodes.append(node)
            nodes_values.append(node.value)
            node = node.next
        if as_val:
            return nodes_values
        return nodes

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
    def find(self, val):
        """Метод возвращает первый найденный по значению val узел"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
<<<<<<< HEAD
        return None

    def find_all(self, val):
        """Метод возвращает список всех узлов со значением val"""
        node = self.head
        nodes_list = []
        while node is not None:
            if node.value == val:
                nodes_list.append(node)
            node = node.next
        return nodes_list

    def delete(self, val, rm_all=False):
        node = self.head
        did_rm = False
        while (node is not None) and (not all([not rm_all, did_rm])):
            did_rm = True
            if node is self.head:
                node.next.prev = None
                self.head = node.next
            if node is self.tail:
                node.prev.next = None
                self.tail = node.prev
            node.next.prev = node.prev
            node.prev.next = node.next
            node = node.next
=======
    def find_bin(self, val):
        if self.head is not None:
            node_L = self.head
            node_R = self.tail
            while (node_L.prev is not node_R) and (node_L is not node_R):
                if node_L.value == val:
                    return node_L
                if node_R.value == val:
                    return node_R
                node_L = node_L.next
                node_R = node_R.prev
            if node_L.value == val:
                return node_L
=======
>>>>>>> d9f544d (algo, doubly linked list, wip: switched sol & test to find() - the solution from LinkedList())
        return None

    def find_all(self, val):
        return []

    def delete(self, val, all=False):
        pass
>>>>>>> 995a631 (algo, doubly linked list, wip: add_in_tail(), get_all_nodes(), clean(), find() -- main tests ok)

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return 0

    def insert(self, afterNode, newNode):
        pass

    def add_in_head(self, newNode):
        pass
