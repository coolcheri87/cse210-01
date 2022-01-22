# Cheri Hansen - han19067@byui.edu
# Program is the Card play
# Created 1/21/2022

import random

class Card:

    def __init__(self):
        self.cardValue = random.randint(1,13)

    def drawCard(self):
        self.cardValue = random.randint(1,13)
        return self.cardValue
