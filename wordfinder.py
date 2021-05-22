
# from _typeshed import OpenTextMode, OpenTextModeReading
import random, string

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.count = 0
        self.wordlist = []

    
        with open(self.filepath, "r") as f:
            for line in f:
                stripped_line = line.rstrip("\n")
                self.wordlist.append(stripped_line)
                self.count += 1
    def __str__(self):
        return f'There are {self.count} words in this file'
    
    def random(self):
        idx = random.randint(0, len(self.wordlist))
        return self.wordlist[idx]

class SpecialWordFinder(WordFinder):
    "Finds random words from dictionary but ignores comments and blank lines"
    def __init__(self, filepath):
        super().__init__(filepath)
        self.wordlist = []
        
        with open(self.filepath, "r") as f:
            for line in f:
                stripped_line = line.rstrip("\n")
                if stripped_line in string.whitespace or stripped_line.startswith("#"):
                    continue
                self.wordlist.append(stripped_line)
                self.count += 1
   
