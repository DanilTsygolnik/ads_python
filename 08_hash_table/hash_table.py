class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size

    def hash_fun(self, value:str):
        """Calculate the index based on table size and value"""
        if self.size == 0:
            result = None
        else:
            sum_of_bytes = sum(value.encode('utf-8'))
            result = sum_of_bytes % self.size
        return result

    def seek_slot(self, value:str):
        """Find a free slot for the new value"""
        checked_indices = set()
        curr_index = self.hash_fun(value)
        while len(checked_indices) != self.size:
            if self.slots[curr_index] is None:
                return curr_index
            checked_indices.add(curr_index)
            curr_index = (curr_index + self.step) % self.size
        return None

    def put(self, value:str):
        """Put the new value in a free slot if there's one"""
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return index

    def find(self, value:str):
        """Find out if there's a value in the table"""
        checked_indices = set()
        curr_index = self.hash_fun(value)
        while len(checked_indices) != self.size:
            if self.slots[curr_index] == value:
                return curr_index
            checked_indices.add(curr_index)
            curr_index = (curr_index + self.step) % self.size
        return None
