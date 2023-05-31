def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
        >>> frequency([1, [10, 20], 3], [10, 20])
        1
    """

    freq = 0
    for term in lst:
        if term == search_term:
            freq += 1
    return freq