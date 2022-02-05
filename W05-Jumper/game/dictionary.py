# Cheri Hansen


import random

class Dictionary:
    
    # This is initializing words and the random word
    def __init__(self):
        self._words = ['core','java','micro','sql','electric','circuits','physics','university','analysis','introduction']
        self._word = self._words[random.randint(0,len(self._words)-1)]

    def getWord(self):
        return self._word
