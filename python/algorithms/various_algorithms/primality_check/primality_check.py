def is_prime(number):

    def iter_divisor_test(number, divisor):
        if divisor**2 > number:
            return True
        if number % divisor == 0:
            return False
        return iter_divisor_test(number, divisor+1)
 
    if number <= 0:
        raise ValueError("The number must positive integer")
    return iter_divisor_test(number, 2)
