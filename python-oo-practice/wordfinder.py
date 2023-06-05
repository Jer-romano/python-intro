"""Word Finder: finds random words from a dictionary."""
from random import randint 

class WordFinder:
    def __init__(self, path):
        self.path = path
        self.words = self.readFile(path)
        print(str(len(self.words)) + " words read")
   
    def readFile(self, path):
        with open(path, "r") as file:
            words = [line.strip() for line in file]
        return words
    
    def random(self):
        '''Returns a random word from the read-in file of words'''
        index = randint(0, len(self.words)-1)
        return self.words[index]