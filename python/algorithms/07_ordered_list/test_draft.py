import unittest
from ordered_list import OrderedList, OrderedStringList


class TestOrderedListMethods(unittest.TestCase):

    def test_compare(self):
        OL = OrderedList(asc=True)
        self.assertEqual(OL.compare(42, 42), 0)
        self.assertEqual(OL.compare(1, 2), -1)
        self.assertEqual(OL.compare(2, 1), 1)

    def test_add_asc_True(self):
        OL = OrderedList(asc=True)
        OL.add(2)
        self.assertEqual(len(OL.get_all()), 1)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 2)
        OL.add(3)
        self.assertEqual(len(OL.get_all()), 2)
        self.assertEqual(OL.head.next.value, 3)
        OL.add(4)
        self.assertEqual(len(OL.get_all()), 3)
        self.assertEqual(OL.tail.value, 4)
        OL.add(5)
        self.assertEqual(len(OL.get_all()), 4)
        self.assertEqual(OL.tail.value, 5)
        OL.add(1)
        self.assertEqual(len(OL.get_all()), 5)
        self.assertEqual(OL.head.value, 1)
        OL.add(1)
        self.assertEqual(len(OL.get_all()), 6)
        self.assertEqual(OL.head.value, 1)
        OL.add(4)
        self.assertEqual(len(OL.get_all()), 7)
        self.assertEqual(OL.tail.prev.value, 4)
        self.assertEqual(OL.tail.prev.prev.value, 4)
 
    def test_add_asc_False(self):
        OL = OrderedList(asc=False)
        OL.add(2)
        self.assertEqual(len(OL.get_all()), 1)
        self.assertEqual(OL.head.value, 2)
        self.assertEqual(OL.tail.value, 2)
        OL.add(3)
        self.assertEqual(len(OL.get_all()), 2)
        self.assertEqual(OL.head.value, 3)
        OL.add(4)
        self.assertEqual(len(OL.get_all()), 3)
        self.assertEqual(OL.head.value, 4)
        OL.add(5)
        self.assertEqual(len(OL.get_all()), 4)
        self.assertEqual(OL.head.value, 5)
        OL.add(1)
        self.assertEqual(len(OL.get_all()), 5)
        self.assertEqual(OL.tail.value, 1)
        OL.add(1)
        self.assertEqual(len(OL.get_all()), 6)
        self.assertEqual(OL.tail.value, 1)
        self.assertEqual(OL.tail.prev.value, 1)
        OL.add(4)
        self.assertEqual(len(OL.get_all()), 7)
        self.assertEqual(OL.head.next.value, 4)
        self.assertEqual(OL.head.next.next.value, 4)

    def test_find_asc_True(self):
        OL = OrderedList(asc=True)
        OL.add(1)
        OL.add(2)
        OL.add(3)
        OL.add(4)
        OL.add(6)
        self.assertEqual(OL.find(1), OL.head)
        self.assertEqual(OL.find(6), OL.tail)
        self.assertEqual(OL.find(4), OL.tail.prev)
        self.assertIsNone(OL.find(5))

    def test_find_asc_False(self):
        OL = OrderedList(asc=False)
        OL.add(6)
        OL.add(4)
        OL.add(3)
        OL.add(2)
        OL.add(1)
        self.assertEqual(OL.find(1), OL.tail)
        self.assertEqual(OL.find(6), OL.head)
        self.assertEqual(OL.find(4), OL.head.next)
        self.assertIsNone(OL.find(5))

    def test_delete(self):
        OL = OrderedList(asc=True)
        OL.add(1)
        OL.add(2)
        OL.add(3)
        OL.add(4)
        OL.add(6)
        OL.delete(1)
        self.assertEqual(len(OL.get_all()), 4)
        OL.delete(1)
        self.assertEqual(len(OL.get_all()), 4)
        OL.delete(10)
        self.assertEqual(len(OL.get_all()), 4)
        OL.delete(4)
        self.assertEqual(len(OL.get_all()), 3)
        OL.delete(6)
        self.assertEqual(len(OL.get_all()), 2)

    def test_clean(self):
        OL = OrderedList(asc=True)
        OL.add(1)
        OL.add(2)
        OL.add(3)
        OL.add(4)
        OL.add(6)
        OL.clean(asc=False)
        self.assertEqual(len(OL.get_all()), 0)


class TestOrderedStringListMethods(unittest.TestCase):

    def test_compare_string(self):
        SOL = OrderedStringList(asc=True)
        self.assertEqual(SOL.compare('tex', 'text'), -1)
        self.assertEqual(SOL.compare('text', 'tex'), +1)
        self.assertEqual(SOL.compare('text', 'text'), 0)


if __name__ == '__main__':
    unittest.main()
