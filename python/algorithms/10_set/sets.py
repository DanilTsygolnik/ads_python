import ctypes

class PowerSet:

    def __init__(self, stp:int=3, ns:int=5):
        self.num_slots = ns
        self.step = stp
        self.slots = (ctypes.py_object * self.num_slots)()
        for i in range(0,self.num_slots):
            self.slots[i] = []
        self.__num_elem = 0

    def size(self):
        """Show the number of elements in the set"""
        return self.__num_elem

    def hash_fun(self, value:str):
        """Calculate the index based on table size and value"""
        sum_of_bytes = sum(value.encode('utf-8'))
        return sum_of_bytes % self.num_slots

    def put(self, new_item:str):
        """Add a new item to the set"""
        index = self.hash_fun(new_item)
        if new_item not in self.slots[index]:
            self.slots[index].append(new_item)
            self.__num_elem += 1

    def get(self, value:str, index=None) -> bool:
        """Check if there's an element with the value in the set"""
        if index is None:
            index = self.hash_fun(value)
        if value in self.slots[index]:
            return True
        return False

    def remove(self, value:str) -> bool:
        """Remove the element with the value from the set"""
        index = self.hash_fun(value)
        if self.get(value, index):
            self.slots[index].remove(value)
            self.__num_elem -= 1
            return True
        return False

    def get_val(self): # supplemental method
        """Return a sorted list of elements"""
        list_val = []
        for i in self.slots:
            for j in i:
                list_val.append(j)
        return sorted(list_val)

    def copy(self):
        """Return a dublicate of the current PowerSet instance"""
        new_copy = PowerSet()
        for i in self.slots:
            for j in i:
                new_copy.put(j)
        return new_copy

    def intersection(self, set2):
        result = PowerSet()
        for i in self.get_val():
            if set2.get(i):
                result.put(i)
        if result.size() != 0:
            return result
        return None

    def union(self, set2):
        result = self.copy()
        for i in set2.get_val():
            result.put(i)
        if result.size() != 0:
            return result
        return None

    def difference(self, set2):
        """Return a subset containing only elements that don't belong to set2"""
        result = self.copy()
        for i in set2.get_val():
            if result.get(i):
                result.remove(i)
        if result.size() != 0:
            return result
        return None
