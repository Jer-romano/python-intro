def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2

        >>> mode([1, 2, 3, 2, 4, 5, 3, 6, 6, 7, 6, 8])
        6
    """
    uniques = set(nums)
    max = 1
    mode = nums[0]
    for el in uniques:
        if nums.count(el) > max:
            max = nums.count(el)
            mode = el
    return mode
