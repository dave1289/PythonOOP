"""Word Finder: finds random words from a dictionary."""
import random

def populate_wordbank(file):
    with open(file, 'r') as f:
        data = f.read()
        word_bank = data.split('\n')
        print(f'{len(word_bank)} words read')
        return word_bank


class WordFinder():
    """Accepts word document and creates list from words (divided at line break)

    >>> s = WordFinder('words.txt')
    235887 words read

    >>> s.WORD_BANK[0] == 'A'
    True

    """

    def __repr__(self):
        return f'<SerialGenerator start={self.org_start} next={self.start}>'

    def __init__(self, file):
        self.file = file
        self.WORD_BANK = populate_wordbank(file)
    
    def random(self):
        return random.choice(self.WORD_BANK)

class SpecialWordFinder(WordFinder):
    """Accepts word document and creates list from words (divided at line break)
    ** NEW SUBCLASS MAKES SURE TO NOT INCLUDE '#' IN RANDOM RESULT**

    >>> s = SpecialWordFinder('words.txt')
    235887 words read

    >>> b = s.random()

    >>> '#' not in b
    True

    """
    def __init__(self, file):
        super().__init__(file)
    
    def random(self):
        rand = '#'
        while '#' in rand:
            rand = random.choice(self.WORD_BANK)
        return rand