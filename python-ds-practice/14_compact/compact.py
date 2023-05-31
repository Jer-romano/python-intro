def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy = lst.copy()
    for el in copy:
        if not el or len(el) == 0:
            copy.remove(el)
    return copy