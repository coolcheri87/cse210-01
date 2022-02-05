# Cheri Hansen - han19067@byui.edu
# Program is the interface for the game
# Created 2/1/2022

from .dictionary import Dictionary
from .jumper import Jumper


class Interface:

    # This is initializing score and card
    def __init__(self):
        self.dictionary = Dictionary()
        self.jumper = Jumper()
        print(self.dictionary.getWord())


    def start_game(self):
        done = False
        displayWord = ''
        for i in range(len(self.dictionary.getWord())):
            displayWord += '_'

        # Output first
        print(displayWord)
        self.jumper.getJumper(0)

        while (not done):
            x = input('Guess a letter [a-z]: ')

            # See if any letters match...
            guessed = False
            for i in range(len(self.dictionary.getWord())):
                if (self.dictionary.getWord()[i] == x):
                    guessed = True
                    displayWord[i] = x[0]

            print(displayWord)
            if (guessed):
                done = self.jumper.getJumper(0)
            else:
                done = self.jumper.getJumper(1)


            

