class BloomFilter:

    def __init__(self, f_len:int):
        self.filter_len = f_len
        self.bit_array = 0

    def calc_hash(self, text_str, rand_num):
        iter_result = 0
        for c in text_str:
            char_code = ord(c)
            iter_result = (iter_result * rand_num + char_code) % self.filter_len
        return iter_result

    def get_bit_mask(self, text_str, rand_num):
        return 1 << self.calc_hash(text_str, rand_num)

    def hash1(self, text_str):
        return self.get_bit_mask(text_str, 17)

    def hash2(self, text_str):
        return self.get_bit_mask(text_str, 223)

    def add(self, text_str):
        mask_to_apply = self.hash1(text_str) | self.hash2(text_str)
        self.bit_array |= mask_to_apply

    def is_value(self, text_str):
        refer_mask = self.hash1(text_str) | self.hash2(text_str)
        test_result = self.bit_array & refer_mask
        return test_result == refer_mask
