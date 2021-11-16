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
        """Return the number of nodes in the list"""
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
 
    def add(self, value):
        """Add a new node with suggested value"""
        node = self.head
        new_node = Node(value)
        if self.len() == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if self.__ascending:
                flag = +1
            else:
                flag = -1
            while node is not None:
                if self.compare(node.value, value) == flag:
                    if node == self.head:
                        new_node.next = self.head
                        self.head.prev = new_node
                        self.head = new_node
                    else:
                        node.prev.next = new_node
                        new_node.prev = node.prev
                        new_node.next = node
                        node.prev = new_node
                    return
                node = node.next
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

class OrderedStringList(OrderedList):

    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        s1 = v1.strip()
        s2 = v2.strip()
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1
        return 0
