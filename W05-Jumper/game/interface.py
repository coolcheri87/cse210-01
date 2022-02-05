# Cheri Hansen - han19067@byui.edu
# Program is the interface for the juumper game
# Created 2/1/2022
# CSE 210-03 W05 Jumper game

from .dictionary import Dictionary
from .jumper import Jumper
from .startover import StartOver


class Interface:

    # This is initializing score and card
    def __init__(self):
        self.dictionary = Dictionary()
        self.jumper = Jumper()
        self.so = StartOver()
        

    def setupDisplayWord(self):
        # Set displayWord to bunch of underscores...
        self.displayWord = []
        for i in range(len(self.dictionary.getWord())):
            self.displayWord.append('_')


    def start_game(self):
        done = False

        # Output first
        self.setupDisplayWord()
        self.jumper.getJumper(0,self.displayWord)

        while (not done):
            x = ''
            while (len(x) == 0):
                x = input('Guess a letter [a-z]: ')

            # See if any letters match...
            guessed = False
            for i in range(len(self.dictionary.getWord())):
                if (self.dictionary.getWord()[i] == x[0]):
                    guessed = True
                    self.displayWord[i] = x[0]

            # See if we won!
            count = 0
            for i in range(len(self.displayWord)):
                if (self.displayWord[i] == '_'):
                    count = count + 1
            
            # If we won, let's celebrate!
            if (count == 0):
                print("You guessed the word. Yahoo!! \n")
                self.jumper.getJumper(0,self.displayWord)
                done = True

            # If not done...
            if (not done):
                if (guessed):
                    done = self.jumper.getJumper(0,self.displayWord)
                else:
                    done = self.jumper.getJumper(1,self.displayWord)

            # If lost or won, do you want to start over
            if (done):
                done = self.so.startover()
                if (not done):
                    self.dictionary = Dictionary()
                    self.jumper = Jumper()
                    self.setupDisplayWord()
                    self.jumper.getJumper(0,self.displayWord)




