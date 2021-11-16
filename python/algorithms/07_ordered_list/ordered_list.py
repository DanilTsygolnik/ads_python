#pylint: disable=c0114,c0115,c0116,c0103
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class OrderedList:

    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def get_all(self):
        """Return a list of all nodes in OrderedList"""
        node = self.head
        all_nodes = []
        while node is not None:
            all_nodes.append(node)
            node = node.next
        return all_nodes

    def find(self, val):
        """Return the first found node with node.value == val"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def delete(self, val, rm_all=False):
        node = self.head
        did_rm = False
        while (node is not None) and (not all([not rm_all, did_rm])):
            if node.value == val:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                else:
                    if node is self.head:
                        node.next.prev = None
                        self.head = node.next
                    elif node is self.tail:
                        node.prev.next = None
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                        node.prev.next = node.next
                    did_rm = True
            node = node.next

    def clean(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        """Compare two values"""
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0
        
    def add_in_tail(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.add_in_tail(newNode)
        else:
            if (afterNode is None) or (self.tail is afterNode):
                self.add_in_tail(newNode)
            else:
                node = self.head
                while node is not None:
                    if node is afterNode:
                        node.next.prev = newNode
                        newNode.next = node.next
                        node.next = newNode
                        newNode.prev = node
                        break
                    node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode
