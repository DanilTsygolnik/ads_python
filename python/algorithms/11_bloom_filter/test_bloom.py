import unittest
from bloom import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_main(self):

        # filter length = 32
        f_len = 32
        BF = BloomFilter(f_len)

        # calc_hash test
        # test string "xx"; expected char code for "x"=120; random number = 1
        expected_hash = ((120%32) + 120) % 32
        self.assertEqual(BF.calc_hash(1, "xx"), expected_hash)

        #print(f'Expected output: {expected_hash}')
        #print(f'Expected bin_hash: {f"{expected_hash:b}"}')

        # get_mask test
        expected_mask = "".join([27*"0", "10000"])
        self.assertEqual(BF.get_mask(BF.calc_hash(1, "xx")), expected_mask)

        # test add
        mask1 = BF.get_mask(BF.hash1("xx"))
        mask2 = BF.get_mask(BF.hash2("xx"))
        expected_add_result = list(int(i) for i in "00000000000000000000000000010000")
        BF.add("xx")
        self.assertEqual(BF.bitarray, expected_add_result)
        
        # test is_value
        self.assertFalse(BF.is_value("x"))
        self.assertTrue(BF.is_value("xx"))

        # -------
        curr_str  = "".join(str(i) for i in range(0,10))
        str_for_tests = [curr_str]
        index_cnt = 0
        while index_cnt < 9:
            curr_str = "".join([curr_str[1:], curr_str[0]])
            str_for_tests.append(curr_str)
            index_cnt += 1
 

if __name__ == '__main__':
    unittest.main()
