def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)

        >>> two_oldest_ages([1, 2])
        (1, 2)

        >>> two_oldest_ages([1, 5, 4, 2, 5, 5])
        (4, 5)

        >>> two_oldest_ages([5, 5, 5])
        'ages array must contain at least two distinct ages'
    """
    if len(set(ages)) == 1:
        return "ages array must contain at least two distinct ages"
    ages.sort()
    oldest = []
    oldest.append(ages[-1])
    second_oldest = ages[-2]
    if second_oldest == oldest[0]:
        i = -3
        while second_oldest == oldest[0]:
            second_oldest = ages[i] # iterate from the end of the list to the front
            i -= 1
    oldest.insert(0, second_oldest)
    
    return tuple(oldest)
    


    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.