#pylint: disable=c0114,c0115,c0116,c0103
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class LinkedList2:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_all_nodes(self, as_val=False):
        """
        Метод отладочного вывода значений всех узлов связного списка
        По умолчанию выводит на экран значение каждого узла
        При as_list=True возвращает список значений узлов
        """
        nodes = []
        nodes_values = []
        node = self.head.next
        while node is not self.tail:
            nodes.append(node)
            nodes_values.append(node.value)
            node = node.next
        if as_val:
            return nodes_values
        return nodes

    def add_in_head(self, newNode):
        if self.tail.prev is self.head:
            self.tail.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode

    def add_in_tail(self, newNode):
        if self.tail.prev is self.head:
            self.head.next = newNode
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        newNode.next = self.tail
        self.tail.prev = newNode

    def insert(self, afterNode, newNode):
        if self.tail.prev is self.head:
            self.add_in_head(newNode)
        else:
            if (afterNode is None) or (afterNode is self.tail.prev):
                self.add_in_tail(newNode)
            else:
                node = self.head.next
                while node is not self.tail:
                    if node is afterNode:
                        newNode.next = node.next
                        node.next.prev = newNode
                        newNode.prev = node
                        node.next = newNode
                        break
                    node = node.next

    def delete(self, val, rm_all=False):
        node = self.head.next
        did_rm = False
        while (node is not self.tail) and (not all([not rm_all, did_rm])):
            if node.value == val:
                if self.head.next is self.tail.prev: # the only node from the list
                    self.clean()
                else:
                    if node is self.head.next:
                        self.head.next = node.next # self.head -- node.next
                        node.next.prev = self.head # node.next -- self.head
                    elif node is self.tail.prev:
                        self.tail.prev = node.prev # self.tail -- node.prev
                        node.prev.next = self.tail # node.prev -- self.tail
                    else:
                        node.next.prev = node.prev # node.next -- node.prev
                        node.prev.next = node.next # node.prev -- node.next
                    did_rm = True
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        length = 0
        node = self.head.next
        while node is not self.tail:
            length += 1
            node = node.next
        return length

    def find(self, val):
        """Метод возвращает первый найденный по значению val узел"""
        return None

    def find_all(self, val):
        """Метод возвращает список всех узлов со значением val"""
        nodes_list = []
        return nodes_list
