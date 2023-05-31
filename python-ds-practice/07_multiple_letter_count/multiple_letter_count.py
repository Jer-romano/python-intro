def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}

        >>> multiple_letter_count('Hello world')
        {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    """
    # Solution that doesn't use string methods
    # freq = {}
    # for char in phrase:
    #     curr_val = freq.get(char)
    #     if curr_val is not None:
    #         freq[char] = curr_val+1
    #     else:
    #         freq[char] = 1
    # return freq

    return {char: phrase.count(char) for char in phrase} #Uses string .count() method, and comprehension
            