def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # copy = lst.copy()
    # for el in copy:
    #     if bool(el) == False:    #Why does this not work? (It doesn't remove the empty list or tuple)
    #         copy.remove(el)
    # return copy
    return [el for el in lst if el]