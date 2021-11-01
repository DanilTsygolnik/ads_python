import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def make_array(self, new_capacity):
        """Prepare a memory buffer for dynamic array"""
        return (new_capacity * ctypes.py_object)()

    def __len__(self):
        """Return number of items in dynamic array"""
        return self.count

    def __getitem__(self, i):
        """Return an item stored under the index i"""
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        """Change buffer size where the dynamic array is stored"""
        new_array = self.make_array(new_capacity)
        for i, _ in enumerate(self.array):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """Add a new item in the end of the dynamic array"""
        if self.count == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """
        Add a new item under the index i:
        1) shift each item from under index i to the end one 1 step right;
        2) store a new item under index i.
        """
        pass

    def delete(self, i):
        """Delete the item stored under the index i"""
        pass
