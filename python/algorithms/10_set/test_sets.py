import unittest
import datetime
from sets import PowerSet


class TestPowerSetBasicMethods(unittest.TestCase):

    def test_main(self):

        # __init__()
        PS = PowerSet()
        self.assertEqual(PS.size(), 0)

        # put(value)
        PS.put("a")
        self.assertEqual(PS.size(), 1)

        # get(value)
        self.assertTrue(PS.get("a"))
        self.assertFalse(PS.get("b"))

        # get_val
        self.assertEqual(PS.get_val(), ["a"])

        # remove(value)
        self.assertFalse(PS.remove("b"))
        self.assertTrue(PS.remove("a"))
        self.assertEqual(PS.size(), 0)
        self.assertEqual(PS.get_val(), [])

class TestPowerSetMainMethods(unittest.TestCase):

    def setUp(self):
        self.PS_main = PowerSet()
        self.PS_supp = PowerSet()
        self.values = sorted(str(i) for i in range(1,11))
        for i in self.values[:5]:
            self.PS_main.put(i)
        for i in self.values[5:]:
            self.PS_supp.put(i)

    def test_copy(self):
        PS_copy = self.PS_main.copy()
        self.assertEqual(PS_copy.size(), 5)
        self.assertEqual(PS_copy.get_val(), self.values[:5])
        self.assertIsNot(PS_copy, self.PS_main)

    def test_intersection(self):

        # no intersections
        PS_curr = self.PS_main.intersection(self.PS_supp)
        self.assertEqual(PS_curr.size(), 0)

        # add some common elements
        intersect_ref = sorted(str(i) for i in range(1,4))
        for i in intersect_ref:
            self.PS_supp.put(i)
        PS_curr = self.PS_main.intersection(self.PS_supp)
        self.assertEqual(PS_curr.size(), 3)
        self.assertEqual(PS_curr.get_val(), intersect_ref)

    def test_union(self):
        PS_curr = self.PS_main.union(self.PS_supp)
        self.assertEqual(PS_curr.size(), 10)
        self.assertEqual(PS_curr.get_val(), self.values)

    def test_difference(self):
        ref_values = ['3', '4']
        val_to_exclude = ['1', '10', '2']
        for i in val_to_exclude:
            self.PS_supp.put(i)

        # test empty set with set2 containing elements
        PS_curr = PowerSet()
        self.assertIs(PS_curr.difference(self.PS_supp), PS_curr)

        # both sets contain the same elements
        PS_curr = self.PS_main.difference(self.PS_supp)
        self.assertEqual(PS_curr.size(), 2)
        self.assertEqual(PS_curr.get_val(), ref_values)

        # set2 has no elements from the 1st one
        self.assertEqual(PS_curr.difference(self.PS_supp).get_val(), ref_values)

    def test_issubset(self):
        ref_values = ['3', '4']

        # empty-empty (must be True)
        PS_curr = PowerSet()
        PS_empty = PowerSet()
        self.assertTrue(PS_curr.issubset(PS_empty))

        # empty-filled (must be False)
        self.assertFalse(PS_curr.issubset(self.PS_main))

        # common case
        for i in ref_values:
            PS_curr.put(i)
        self.assertFalse(PS_curr.issubset(self.PS_main))
        self.assertTrue(self.PS_main.issubset(PS_curr))

        # filled-empty (must be True)
        self.assertTrue(self.PS_main.issubset(PS_empty))

    def test_methods_speed(self):

        # insertion test
        PS = PowerSet()
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        for i in range(0, 25000):
            PS.put(i)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"insertion of 25000 elements takes {exec_time:.3f} seconds")

        # intersection test
        PS_1 = PowerSet()
        PS_2 = PowerSet()
        for i in range(0, 40000):
            PS_1.put(i)
        for i in range(12500, 62501):
            PS_2.put(i)
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        result = PS_1.intersection(PS_2)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"intersection() takes {exec_time:.3f} seconds")

        # difference test
        ps_1 = PowerSet()
        ps_2 = PowerSet()
        for i in range(0, 40000):
            ps_1.put(i)
        for i in range(12500, 62501):
            ps_2.put(i)
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        result = ps_1.difference(ps_2)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"difference() takes {exec_time:.3f} seconds")

        # union test 1
        ps_1 = PowerSet()
        for i in range(0, 25000):
            ps_1.put(i)
        ps_2 = ps_1.copy()
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        result = ps_1.union(ps_2)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"union() with 2 equal sets takes {exec_time:.3f} seconds")

        # union test 2
        ps_1 = PowerSet()
        ps_2 = PowerSet()
        for i in range(0, 25000):
            ps_1.put(i)
        for i in range(25000, 50001):
            ps_2.put(i)
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        result = ps_1.difference(ps_2)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"union() with 2 different sets takes {exec_time:.3f} seconds")

        # issubset test
        ps_1 = PowerSet()
        ps_2 = PowerSet()
        for i in range(0, 35000):
            ps_1.put(i)
        for i in range(10000, 25001):
            ps_2.put(i)
        exec_start_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        result = ps_1.issubset(ps_2)
        exec_finish_seconds = float(datetime.datetime.now().strftime("%S.%f"))
        exec_time = (exec_finish_seconds-exec_start_seconds) % 60
        self.assertTrue(exec_time < 2)  
        print(f"issubset() takes {exec_time:.3f} seconds")

if __name__ == '__main__':
    unittest.main()
