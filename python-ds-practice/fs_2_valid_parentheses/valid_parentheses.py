def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses("((()(()))")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left_par_count = 0
    right_par_count = 0

    for p in parens:
        if p == "(":
            left_par_count += 1
        elif p == ")":
            if left_par_count == 0:
                return False
            else:
                left_par_count -= 1
    return left_par_count == 0