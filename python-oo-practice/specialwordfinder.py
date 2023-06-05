"""Special Word Finder: finds random words from a dictionary, ignoring blank lines and lines beginning with "#"."""
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        self.path = path
        self.words = self.readFile(path)
        print(str(len(self.words)) + " words read")

    def readFile(self, path):
        with open(path, "r") as file:
            words = [line.strip() for line in file if line.strip() and line[:1] != "#"]
        return words