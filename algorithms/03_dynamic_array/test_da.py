import unittest
from dynamic_array import DynArray

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

if __name__=="__main__":
    unittest.main()
