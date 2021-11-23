class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size

    def hash_fun(self, value):
        sum_of_bytes = sum(value.encode('utf-8'))
        return sum_of_bytes % self.size

    def seek_slot(self, value):
        checked_indices = set()
        curr_index = self.hash_fun(value)
        while len(checked_indices) != self.size:
            if self.slots[curr_index] is None:
                return curr_index
            checked_indices.add(curr_index)
            curr_index = (curr_index + self.step) % self.size
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value):
        checked_indices = set()
        curr_index = self.hash_fun(value)
        while len(checked_indices) != self.size:
            if self.slots[curr_index] == value:
                return curr_index
            checked_indices.add(curr_index)
            curr_index = (curr_index + self.step) % self.size
        return None
