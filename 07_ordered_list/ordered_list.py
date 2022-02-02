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
        """Clean the list and set a new self.__ascending value if needed"""
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
        new_node = Node(value)
        if self.head is None: # addition to an empty ordered list
            self.head = new_node
            self.tail = new_node
        else:
            node = self.head
            while node is not None:
                if self.__ascending:
                    if self.compare(value, node.value) == -1: # if value < node.value:
                        break
                else:
                    if self.compare(value, node.value) == 1: # if value > node.value:
                        break
                node = node.next
            # inserting new_node before node (new_node -> node.prev)
            if node is self.head:
                self.head.prev = new_node # bind self.head.prev with new_node
                new_node.next = self.head # bind new_node with self.head
                self.head = new_node      # renew self.head
            elif node is None:
                self.tail.next = new_node # bind self.tail with new_node
                new_node.prev = self.tail # bind new_node with self.tail
                self.tail = new_node      # renew self.tail
            else:
                node.prev.next = new_node # bind node.prev with new_node
                new_node.prev = node.prev # bind new_node with node.prev
                node.prev = new_node      # bind node with new_node
                new_node.next = node      # bind new_node with node

class OrderedStringList(OrderedList):

    def __init__(self, asc):
        # super(OrderedStringList, self).__init__(asc)
        # R1725: pylint suggests using Python3 style super() without arguments
        super().__init__(asc)

    def compare(self, v1, v2):
        s1 = v1.strip()
        s2 = v2.strip()
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1
        return 0
