import unittest
from dynamic_array import DynArray

def get_all_items(array):
    """Return a list of dynamic array items"""
    items = []
    for i in range(array.__len__()):
        items.append(array.array[i])
    return items

def mk_dyn_arr(iterable):
    dyn_arr = DynArray()
    for i in iterable:
        dyn_arr.append(i)
    return dyn_arr

class TestDynArray(unittest.TestCase):

    def test_template(self):
        """
        The methods are being tested:
        - append(itm);
        - __len__();
        - __getitem__(i);
        """
        dyn_arr = DynArray()
        self.assertEqual(dyn_arr.count, 0)
        self.assertEqual(dyn_arr.capacity, 16)
        ref = [1,2,3]
        for i in ref:
            dyn_arr.append(i)
        dyn_arr_items = []
        for i in range(dyn_arr.__len__()):
            dyn_arr_items.append(dyn_arr.__getitem__(i))
        self.assertEqual(dyn_arr_items, ref)

    def test_insert(self):
        """
        Test cases:
        - index out of bounds
        - case 1: with index=0 -- [] >> [18] >> [2,18] >> [1,2,18]
        - case 2: with index=2 -- [1,2,18] >> [1,2,3,18] >> .. >> [1,2, ..., 17, 18]
        """
        dyn_arr = DynArray()

        # index out of bounds
        with self.assertRaises(IndexError):
            dyn_arr.insert(-1, 4)
        with self.assertRaises(IndexError):
            dyn_arr.insert(1, 4)

        # case 1
        dyn_arr.insert(0, 18)
        self.assertEqual(get_all_items(dyn_arr), [18])
        dyn_arr.insert(0, 2)
        self.assertEqual(get_all_items(dyn_arr), [2,18])
        dyn_arr.insert(0, 1)
        self.assertEqual(get_all_items(dyn_arr), [1,2,18])

        # case 2
        cnt = 17
        ref = [1,2,18]
        while cnt > 2:
            dyn_arr.insert(2, cnt)
            ref.insert(2, cnt)
            self.assertEqual(get_all_items(dyn_arr), ref)
            if len(ref) <= 16:
                self.assertEqual(dyn_arr.capacity, 16)
            if len(ref) > 16:
                self.assertEqual(dyn_arr.capacity, 32)
            cnt -= 1

    def test_delete(self):
        """
        Test cases:
        - index out of bounds
        - case 1: delete from middle; from head and tail;
        - case 2: check buffer resizing.
        """
        dyn_arr = DynArray()
        # index out of bounds
        with self.assertRaises(IndexError):
            dyn_arr.delete(-1)
        with self.assertRaises(IndexError):
            dyn_arr.delete(0)
        with self.assertRaises(IndexError):
            dyn_arr.delete(40)

        # case 1
        dyn_arr = mk_dyn_arr(list(i for i in range(3)))
        dyn_arr.delete(1)
        self.assertEqual(get_all_items(dyn_arr), [0,2])
        self.assertEqual(dyn_arr.count, 2)
        self.assertEqual(dyn_arr.capacity, 16)
        dyn_arr.delete(0)
        self.assertEqual(get_all_items(dyn_arr), [2])
        self.assertEqual(dyn_arr.count, 1)
        dyn_arr.delete(0)
        self.assertEqual(get_all_items(dyn_arr), [])
        self.assertEqual(dyn_arr.count, 0)
        self.assertEqual(dyn_arr.capacity, 16)

        dyn_arr = mk_dyn_arr(list(i for i in range(33)))
        self.assertEqual(dyn_arr.__len__(), 33)
        self.assertEqual(get_all_items(dyn_arr), list(i for i in range(33)))
        self.assertEqual(dyn_arr.capacity, 64)

        # case 2
        while dyn_arr.count != 0:
            dyn_arr.delete(0)
            if 20<dyn_arr.count<=31:
                self.assertEqual(dyn_arr.capacity, 42)
            if 13<dyn_arr.count<=20:
                self.assertEqual(dyn_arr.capacity, 28)
            if 8<dyn_arr.count<=13:
                self.assertEqual(dyn_arr.capacity, 18)
            if 0<dyn_arr.count<=8:
                self.assertEqual(dyn_arr.capacity, 16)

if __name__=="__main__":
    unittest.main()
