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
