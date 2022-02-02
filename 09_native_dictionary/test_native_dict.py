import unittest
from native_dict import NativeDictionary


class TestNativeDict(unittest.TestCase):

    def setUp(self):
        self.ND = NativeDictionary(5)
        # keys and values template for tests
        self.keys = ["", "aa", "bb", "cc", "abcd!"]
        self.values = [0, 4, 1, 3, 2]
        # how self.slots and self.values must look like after calling put(key, val) method
        self.ref_keys = ["", "bb", "abcd!", "cc", "aa"]
        self.ref_values = [0,1,2,3,4]

    def test_hash_fun(self):
        # common case
        hash_fun_output = []
        hash_fun_ref = []
        for i in self.keys:
            hash_fun_output.append(self.ND.hash_fun(i))
            check_sum = 0
            for j in i:
                check_sum += ord(j)
            hash_fun_ref.append(check_sum % self.ND.size)
            self.assertEqual(hash_fun_output, hash_fun_ref)

        # Native Dictionary has 0 slots
        self.ND = NativeDictionary(0)
        hash_fun_output = self.ND.hash_fun("aaa")
        self.assertIsNone(hash_fun_output)

    def test_is_key(self):
        cnt = 0
        while cnt < self.ND.size:
            self.ND.slots[cnt] = self.ref_keys[cnt]
            self.ND.values[cnt] = self.ref_values[cnt]
            cnt += 1
        for i in self.keys:
            self.assertTrue(self.ND.is_key(i))
        self.assertFalse(self.ND.is_key("xxx"))

    def test_put(self):
        cnt = 0
        for i in self.keys:
            self.ND.put(i, self.values[cnt])
            cnt += 1
        self.assertEqual(self.ND.slots, self.ref_keys)
        self.assertEqual(self.ND.values, self.ref_values)

        # test setting a new value for the key
        self.ND.put("", "-")
        self.ND.put("aa", "x")
        self.assertEqual(self.ND.values, ["-",1,2,3,"x"])


if __name__ == '__main__':
    unittest.main()
