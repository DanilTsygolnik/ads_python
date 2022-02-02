import unittest
from native_cache import NativeCache


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.NC = NativeCache(5)
        keys = ["i", "aa", "bb", "cc", "abcd!"]
        for i in keys:
            self.NC.put(i, self.NC.hash_fun(i))

    def test_templ(self):
        self.assertEqual(self.NC.slots, ["i", "bb", "abcd!", "cc", "aa"])
        self.assertEqual(self.NC.values, [0,1,2,3,4])
        self.assertEqual(self.NC.hits, [1]*5)

    def test_collisions(self):
        alt_keys = ["Z", "G", "H", "S", "E"]
        self.NC.hits = [1]*self.NC.size # сровнять все hits
        slot_to_update = -1
        for i in alt_keys:
            self.NC.hits[slot_to_update] = 0 # накрутка
            self.NC.put(i, slot_to_update) # добавление
            self.NC.hits = [1]*self.NC.size # сровнять все hits
            slot_to_update -= 1
        self.assertEqual(self.NC.slots, ["E", "S", "H", "G", "Z"])
        self.assertEqual(self.NC.values, [-5,-4,-3,-2,-1])
        self.assertEqual(self.NC.hits, [1]*self.NC.size)

        # test hits update
        num_hits_to_write = 4
        for i in ["E", "S", "H", "G", "Z"]:
            cycles_cnt = 0
            while cycles_cnt < num_hits_to_write:
                self.NC.get(i)
                cycles_cnt += 1
            num_hits_to_write -= 1
        self.assertEqual(self.NC.hits, [5,4,3,2,1])


if __name__ == '__main__':
    unittest.main()
