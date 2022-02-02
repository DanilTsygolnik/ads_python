import unittest
from bloom import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def test_templ(self):

        # filter length = 32
        f_len = 32
        BF = BloomFilter(f_len)

        # calc_hash test
        # test string "xx"; expected char code for "x"=120; random number = 1
        expected_hash = ((120%32) + 120) % 32
        self.assertEqual(BF.calc_hash("xx", 1), expected_hash)

        # get_bit_mask test
        expected_mask = 1 << 16 
        self.assertEqual(BF.get_bit_mask("xx", 1), expected_mask)

        # test add
        mask1 = BF.get_bit_mask("xx", 17)
        mask2 = BF.get_bit_mask("xx", 223)
        expected_add_result = 0 | (mask1 | mask2)
        BF.add("xx")
        self.assertEqual(BF.bit_array, expected_add_result)
        
        # test is_value
        self.assertFalse(BF.is_value("x"))
        self.assertTrue(BF.is_value("xx"))

    def test_suggested_strings(self):

        BF = BloomFilter(32)

        tests_input = [
                        ('0123456789', 1 << 13, 1 << 5),
                        ('1234567890', 1 << 29, 1 << 27),
                        ('2345678901', 1 << 13, 1 << 5),
                        ('3456789012', 1 << 29, 1 << 27),
                        ('4567890123', 1 << 13, 1 << 5),
                        ('5678901234', 1 << 29, 1 << 27),
                        ('6789012345', 1 << 13, 1 << 5),
                        ('7890123456', 1 << 29, 1 << 27),
                        ('8901234567', 1 << 13, 1 << 5),
                        ('9012345678', 1 << 29, 1 << 27)
                      ]

        for t in tests_input:
            text_str = t[0]
            refer_hash1 = t[1]
            refer_hash2 = t[2]

            # hash functions test
            self.assertEqual(BF.hash1(text_str), refer_hash1)
            self.assertEqual(BF.hash2(text_str), refer_hash2)
            
            # add(), is_value() test
            BF.add(text_str)
            self.assertTrue(BF.is_value(text_str))
            BF.bit_array = 0


if __name__ == '__main__':
    unittest.main()
