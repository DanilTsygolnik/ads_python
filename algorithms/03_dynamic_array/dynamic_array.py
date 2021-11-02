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
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """Add a new item in the end of the dynamic array"""
        if self.count == self.capacity:
            self.resize(self.capacity * 2)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, index, item):
        """
        Add a new item under the index:
        1) shift each item from under index to the end one 1 step right;
        2) store a new item under index.
        """
        if 0 <= index <= self.count:
            if self.count == self.capacity: # если буффер заполнен
                self.resize(self.capacity * 2) # увеличиваем вдвое
            new_array = self.make_array(self.capacity)
            for i in range(self.count):
                if i < index:
                    new_array[i] = self.array[i]
                else:
                    new_array[i+1] = self.array[i]
            new_array[index] = item
            self.array = new_array
            self.count += 1
        else:
            raise IndexError("Index is out of bounds")

    def delete(self, index:int):
        """Delete the item stored under the index i"""
        if self.count != 0 and 0<=index<=self.count:
            for i in range(self.count):
                if i>index:
                    self.array[i-1] = self.array[i]
            self.count -= 1
            if self.count/self.capacity < 0.5:
                if self.capacity != 16:
                    if int(self.capacity/1.5) > 16:
                        self.resize(int(self.capacity/1.5))
                    else:
                        self.resize(16)
        else:
            raise IndexError("Index is out of bounds")
