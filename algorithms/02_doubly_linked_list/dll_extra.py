#pylint: disable=c0114,c0115,c0116,c0103
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class LinkedList2:
    def __init__(self):
        """So called "dummy nodes" implementation"""
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_all_nodes(self, as_val=False):
        """
        Method returns nodes values (helpful for debugging).
        Returns a list of nodes by default. With as_list=True returns a list of nodes values.
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
        if self.tail.prev is self.head: # if linked list is empty: tail_dummy -- newNode
            self.tail.prev = newNode
        newNode.next = self.head.next # newNode -- head_node
        newNode.prev = self.head # newNode -- head_dummy
        self.head.next = newNode # head_dummy -- newNode

    def add_in_tail(self, newNode):
        if self.tail.prev is self.head: # if linked list is empty: head_dummy -- newNode
            self.head.next = newNode
        newNode.prev = self.tail.prev # newNode -- tail_node 
        self.tail.prev.next = newNode # tail_node -- newNode
        newNode.next = self.tail # newNode -- tail_dummy
        self.tail.prev = newNode # tail_dummy -- newNode

    def insert(self, afterNode, newNode):
        """
        Insert a new node after another one.
        When the linked list is empty, newNode will be added regardless of afterNode value.
        When the linked list is not empty:
        - afterNode=None ==> newNode will be added in the end of the list;
        - afterNode is in the list ==> newNode will be added between afterNode and the next node;
        - afterNode is not in the list ==> nothing will be added.
        """
        if self.tail.prev is self.head:
            self.add_in_head(newNode)
        else:
            if (afterNode is None) or (afterNode is self.tail.prev):
                self.add_in_tail(newNode)
            else:
                node = self.head.next
                while node is not self.tail:
                    if node is afterNode:
                        newNode.next = node.next # newNode -- node.next
                        node.next.prev = newNode # node.next -- newNode
                        newNode.prev = node # newNode -- node
                        node.next = newNode # node -- newNode
                        break
                    node = node.next

    def delete(self, val, rm_all=False):
        """
        Remove a node with node.value=val from the linked list.
        By default, only the first found node will be deleted.
        With rm_all=True all nodes with node.value=val will be removed from the linked list.
        """
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
        """Remove all nodes from the linked list"""
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        """Count nodes in the linked list"""
        length = 0
        node = self.head.next
        while node is not self.tail:
            length += 1
            node = node.next
        return length

    def find(self, val):
        """Return a node with node.value=val"""
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """Return the list of all nodes with node.value=val"""
        node = self.head.next
        nodes_list = []
        while node is not self.tail:
            if node.value == val:
                nodes_list.append(node)
            node = node.next
        return nodes_list
