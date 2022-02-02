class Deque:

    def __init__(self):
        self.count = 0
        self.deque = []

    def size(self):
        return self.count

    def addFront(self, item):
        """The head of the deque is the last element in self.deque"""
        self.deque.append(item)
        self.count += 1

    def addTail(self, item):
        """The tail of the deque is the first element in self.deque"""
        self.deque.insert(0, item)
        self.count += 1

    def removeFront(self):
        if self.count > 0:
            curr_head = self.deque[-1]
            self.deque = self.deque[:-1]
            self.count -= 1
            return curr_head
        return None

    def removeTail(self):
        if self.count > 0:
            curr_tail = self.deque[0]
            self.deque = self.deque[1:]
            self.count -= 1
            return curr_tail
        return None
