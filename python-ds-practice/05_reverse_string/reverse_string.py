def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed = []
    for char in phrase:
        reversed.insert(0, char)
    return "".join(reversed)

