def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]

    This test might take a while, cus python is slow:
    >>> find_factors(123456789)
    [1, 3, 9, 3607, 3803, 10821, 11409, 32463, 34227, 13717421, 41152263, 123456789]
    """
    factors = [num] #All numbers are factors of themselves
    for i in range(num-1, 0, -1):
        if num % i == 0:
            factors.insert(0, i)
    return factors
