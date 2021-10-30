class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

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

    def find(self, val):
        """Метод возвращает первый найденный по значению val узел"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return []

    def delete(self, val, all=False):
        pass

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return 0

    def insert(self, afterNode, newNode):
        pass

    def add_in_head(self, newNode):
        pass
