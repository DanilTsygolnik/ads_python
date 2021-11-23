import unittest
from ordered_list import OrderedList, OrderedStringList


class TestOrderedList(unittest.TestCase):

    def setUp(self):
        self.OL = OrderedList(asc=True)

    def test_compare(self):
        self.assertEqual(self.OL.compare(0, 0), 0)
        self.assertEqual(self.OL.compare(0, 1), -1)
        self.assertEqual(self.OL.compare(1, 0), 1)

    def test_add_asc_True(self):
        values = [3,2,1,4,6,5]
        cnt = 0
        for i in values:
            self.OL.add(i)
            cnt += 1
            current_OL_values = list(j.value for j in self.OL.get_all())
            ref_list = sorted(values[:cnt])
            self.assertEqual(self.OL.len(), cnt)
            self.assertEqual(current_OL_values, ref_list)
 
    def test_add_asc_False(self):
        self.OL.clean(asc=False)
        values = [3,2,1,4,6,5]
        cnt = 0
        for i in values:
            self.OL.add(i)
            cnt += 1
            current_OL_values = list(j.value for j in self.OL.get_all())
            ref_list = sorted(values[:cnt], reverse=True)
            self.assertEqual(self.OL.len(), cnt)
            self.assertEqual(current_OL_values, ref_list)
 
    def test_find_asc_True(self):
        for i in range(1,7):
            self.OL.add(i)
        self.assertIs(self.OL.find(1), self.OL.head)
        self.assertIs(self.OL.find(6), self.OL.tail)
        self.assertIs(self.OL.find(5), self.OL.tail.prev)
        self.assertIsNone(self.OL.find(0))

    def test_find_asc_False(self):
        self.OL.clean(asc=False)
        for i in range(1,7):
            self.OL.add(i)
        self.assertIs(self.OL.find(1), self.OL.tail)
        self.assertIs(self.OL.find(6), self.OL.head)
        self.assertIs(self.OL.find(5), self.OL.head.next)
        self.assertIsNone(self.OL.find(0))

    def test_delete(self):
        ref_list = list(range(1,7))
        for i in ref_list:
            self.OL.add(i)
        cnt = 6
        while cnt > 0:
            self.OL.delete(cnt)
            current_OL_values = list(j.value for j in self.OL.get_all())
            self.assertEqual(current_OL_values, ref_list[:cnt-1])
            cnt -= 1


class TestOrderedStringList(unittest.TestCase):

    def test_compare_string(self):
        SOL = OrderedStringList(asc=True)
        self.assertEqual(SOL.compare('tex', 'text'), -1)
        self.assertEqual(SOL.compare('text', 'tex'), +1)
        self.assertEqual(SOL.compare('text', 'text'), 0)


if __name__ == '__main__':
    unittest.main()
