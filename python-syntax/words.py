def print_upper_words(words, must_start_with):
    '''Prints out the given list of words, converted to uppercase'''
    for word in words:
        for let in must_start_with:
            if word.lower().startswith(let.lower()):
                print(word.upper())


print_upper_words(['hello', 'world'], {"b", "W"})