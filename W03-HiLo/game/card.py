# Cheri Hansen - han19067@byui.edu
# Program is the Card play  W3 hilo card game
# Created 1/21/2022 

import random
    # This is a card class
class Card:
    
    #This is the function to choose random number from 1 thur 13
    def __init__(self):
        self.cardValue = random.randint(1,13)
        
    # draw card from 1 to 13
    def drawCard(self):
        self.cardValue = random.randint(1,13)
        return self.cardValue
