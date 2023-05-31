def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True

        >>> is_palindrome('Race ca r')
        True
    """
    phrase_no_spaces = phrase.replace(" ", "")

    reversed = []
    for char in phrase_no_spaces.lower():
        reversed.insert(0, char)
    reversed_str = "".join(reversed)

    if reversed_str == phrase_no_spaces.lower():
        return True
    else:
        return False