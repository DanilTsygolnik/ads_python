import unittest
from hash_table import HashTable


class Test_Hash_Table(unittest.TestCase):

    def setUp(self):
        self.HT = HashTable(5, 2)
        self.strings = ["", "aaa", "abcd!"]

    def test_hash_fun(self):   
        # common case
        for i in self.strings:
            hash_fun_sum = self.HT.hash_fun(i)
            check_sum = 0
            for j in i:
                check_sum += ord(j)
            check_sum = check_sum % self.HT.size
            self.assertEqual(hash_fun_sum, check_sum)

        # Hash Table has 0 slots
        self.HT = HashTable(0,2)
        hash_fun_sum = self.HT.hash_fun("aaa")
        self.assertIsNone(hash_fun_sum)

    def test_seek_slot(self):
        ref_list = [0,1,2]
        ref_cnt = 0
        for i in self.strings:
            seek_result = self.HT.seek_slot(i)
            self.assertEqual(seek_result, ref_list[ref_cnt])
            ref_cnt += 1

    def test_put(self):
        self.strings = ["", "aaa", "abcd!", "aaa", "abcd!"]
        cnt = 0
        for i in self.strings:
            curr_index = self.HT.put(i)
            self.assertEqual(curr_index, cnt)
            cnt += 1
        self.assertEqual(self.HT.slots, self.strings)

        # no free slots
        self.assertIsNone(self.HT.put("xxx"))

    def test_seek_find(self):
        self.strings = ["aa", "bb", "cc", "dd", "ee"]
        indices_found = [] # must be [4,1,3,0,2]
        indices_ref = []
        for i in self.strings:
            self.HT.put(i)
            indices_found.append(self.HT.find(i))
            indices_ref.append(self.HT.hash_fun(i))
        self.assertEqual(indices_found, indices_ref)
        self.assertIsNone(self.HT.find("xxx"))

if __name__ == '__main__':
    unittest.main()
