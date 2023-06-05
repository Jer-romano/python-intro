"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''Creates a serialGenerator that begins at the 'start' parameter'''
        self.start = start
        self.counter = 0

    def generate(self):
        '''Prints a unique serial number that is one greater than the previously generated number'''
        print(self.start + self.counter)
        self.counter += 1
    
    def reset(self):
        '''Resets the generator back to the starting number. (The one provided to __init__)''' 
        self.counter = 0