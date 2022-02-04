# Cheri Hansen - han19067@byui.edu
# Program is guess my number game
# Created 1/28/2022 

import random


#ToDo: Create GuessMyNumber class as follows:
""" 
Generates Initial card
compare card enter by user with initial card (high or low)
return 100 pts or -75 pts
"""
# This is a card class
class NumberGuess:

    #This is the function to choose random number from 1 thur 50
    def __init__(self):
        self.cardValue = random.randint(1,1000)
        
    # draw card from 1 to 50
    def drawCard(self):
        self.cardValue = random.randint(1,1000)
        return self.cardValue
