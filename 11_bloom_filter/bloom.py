class BloomFilter:

    def __init__(self, f_len=32):
        self.filter_len = f_len
        self.bit_array = 0

    def calc_hash(self, text_str, rand_num):
        """Calculate an index based on the text_str and the random parameter"""
        iter_result = 0
        for c in text_str:
            char_code = ord(c)
            iter_result = (iter_result * rand_num + char_code) % self.filter_len
        return iter_result

    def get_bit_mask(self, text_str, rand_num):
        """Calculate a bit mask using calc_hash function output"""
        return 1 << self.calc_hash(text_str, rand_num)

    def hash1(self, text_str):
        """1st hash function calculating a bit mask based on text_str"""
        return self.get_bit_mask(text_str, 17)

    def hash2(self, text_str):
        """2nd hash function calculating a bit mask based on text_str"""
        return self.get_bit_mask(text_str, 223)

    def add(self, new_elem:str):
        """Add a new element to the filter"""
        mask_to_apply = self.hash1(new_elem) | self.hash2(new_elem)
        self.bit_array |= mask_to_apply

    def is_value(self, element:str):
        """Check if there is the element in the filter"""
        refer_mask = self.hash1(element) | self.hash2(element)
        test_result = self.bit_array & refer_mask
        return test_result == refer_mask
