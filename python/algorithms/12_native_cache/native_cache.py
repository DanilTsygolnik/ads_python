class NativeCache:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None]*self.size
        self.values = [None]*self.size
        self.hits = [0]*self.size

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
        key_is_here = self.is_key(key)
        index = self.hash_fun(key)
        checked_slots = set()
        no_empty_slot = True # допустить возникновение коллизии
        while len(checked_slots) != self.size:
            if (key_is_here and self.slots[index] == key) or \
               ((not key_is_here) and self.slots[index] is None):
                self.slots[index] = key
                self.values[index] = value
                self.hits[index] += 1
                no_empty_slot = False # если пару записали, после выхода из цикла никаких действий
                break
            checked_slots.add(index)
            index = (index + 1) % self.size
        if no_empty_slot: # когда нет пустого слота
            min_hits = min(self.hits)
            index_min_hits  = 0
            for i in self.hits:
                if i == min_hits:
                    break
                index_min_hits += 1
            self.slots[index_min_hits] = key
            self.values[index_min_hits] = value
            self.hits[index_min_hits] = 1

    def get(self, key):
        """Get a value using the key"""
        index = self.hash_fun(key)
        checked_slots = set()
        while len(checked_slots) != self.size:
            if self.slots[index] == key:
                self.hits[index] += 1 # обновить счетчик обращений для данного ключа
                return self.values[index]
            checked_slots.add(index)
            index = (index + 1) % self.size
        return None
