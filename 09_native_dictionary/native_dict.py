class NativeDictionary:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None]*self.size
        self.values = [None]*self.size

    def hash_fun(self, value:str):
        """Calculate the index based on the dictionary size"""
        if self.size == 0:
            result = None
        else:
            sum_of_bytes = sum(value.encode('utf-8'))
            result = sum_of_bytes % self.size
        return result

    def is_key(self, key):
        """Find out if there's a key in the dictionary"""
        index = self.hash_fun(key)
        checked_slots = set()
        while len(checked_slots) != self.size:
            if self.slots[index] == key:
                return True
            checked_slots.add(index)
            index = (index + 1) % self.size
        return False

    def put(self, key, value=None):
        """Add a pair key-value if there's an empty slot"""
        index = self.hash_fun(key)
        checked_slots = set()
        while len(checked_slots) != self.size:
            if (self.is_key(key) and self.slots[index] == key) or \
               (self.is_key(key) is False and self.slots[index] is None):
                self.slots[index] = key
                self.values[index] = value
                break
            checked_slots.add(index)
            index = (index + 1) % self.size

    def get(self, key):
        """Get a value using the key"""
        index = self.hash_fun(key)
        checked_slots = set()
        while len(checked_slots) != self.size:
            if self.slots[index] == key:
                return self.values[index]
            checked_slots.add(index)
            index = (index + 1) % self.size
        return None
