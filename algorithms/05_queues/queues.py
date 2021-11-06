class Queue:

    def __init__(self):
        self.count = 0
        self.queue = []

    def size(self):
        return self.count
 
    def enqueue(self, item):
        """Add an item to queue"""
        self.queue.append(item)
        self.count += 1
 
    def dequeue(self):
        """Return queue head value and delete the item"""
        if self.count > 0:
            head = self.queue[0]
            self.queue = self.queue[1:]
            self.count -= 1
            return head
        return None
