class BloomFilter:

    def __init__(self, f_len:int):
        self.filter_len = f_len
        self.bitarray = [0] * f_len

    def calc_hash(self, rand_num:int, str_input:str) -> int:
        iter_result = 0
        for i in str_input:
            char_code = ord(i)
            iter_result = (iter_result * rand_num + char_code) % self.filter_len
        return iter_result

    def get_mask(self, hash_inp:int) -> str:
        bin_hash = f'{hash_inp:b}'
        mask_templ = (self.filter_len-len(bin_hash))*"0"
        mask = "".join([mask_templ, bin_hash])
        return mask

    def hash1(self, str_inp):
        rn = 17
        return self.calc_hash(rn, str_inp)

    def hash2(self, str_inp):
        rn = 223
        return self.calc_hash(rn, str_inp)

    def add(self, str_inp):
        mask1 = self.get_mask(self.hash1(str_inp))
        mask2 = self.get_mask(self.hash2(str_inp))
        for m in [mask1, mask2]:
            index_cnt = 0
            for i in m: # каждый символ в маске
                self.bitarray[index_cnt] = ( self.bitarray[index_cnt] | int(i) ) # побитовая операция переключения на 1
                index_cnt += 1

    def is_value(self, str1):
        mask1 = self.get_mask(self.hash1(str_inp))
        mask2 = self.get_mask(self.hash2(str_inp))
        for m in [mask1, mask2]:
            index_cnt = 0
            for i in m: # каждый символ в маске
                if i == '1': # на каждую единицу в маске должна найтись единица в фильтре
                    check_result = self.bitarray[index_cnt] & int(i)
                    if check_result != 1:
                        return False
                index_cnt += 1
        return True
