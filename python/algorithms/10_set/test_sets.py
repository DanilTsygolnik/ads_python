import unittest
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
        PS_result = self.PS_main.intersection(self.PS_supp)
        self.assertIsNone(PS_result)

        # add some common elements
        intersect_ref = sorted(str(i) for i in range(1,4))
        for i in intersect_ref:
            self.PS_supp.put(i)
        PS_result = self.PS_main.intersection(self.PS_supp)
        self.assertEqual(PS_result.size(), 3)
        self.assertEqual(PS_result.get_val(), intersect_ref)

    def test_union(self):
        PS_result = self.PS_main.union(self.PS_supp)
        self.assertEqual(PS_result.size(), 10)
        self.assertEqual(PS_result.get_val(), self.values)

        self.assertEqual(self.PS_main.get_val(), self.values[:5])
        self.assertEqual(self.PS_supp.get_val(), self.values[5:])

    def test_difference(self):
        ref_values = ['3', '4']
        diff_values = ['1', '10', '2']
        for i in diff_values:
            self.PS_supp.put(i)

        # both sets contain elements
        PS_result = self.PS_main.difference(self.PS_supp)
        self.assertEqual(PS_result.size(), 2)
        self.assertEqual(PS_result.get_val(), ref_values)
        # set2 has no elements from the 1st one
        self.assertEqual(PS_result.difference(self.PS_supp).get_val(), ref_values)

        # test empty set with set2 containing elements
        PS_result = PowerSet()
        self.assertEqual(PS_result.size(), 0)
        self.assertIsNone(PS_result.difference(self.PS_supp))

if __name__ == '__main__':
    unittest.main()
