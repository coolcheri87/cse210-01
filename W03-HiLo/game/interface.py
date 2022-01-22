# Cheri Hansen - han19067@byui.edu
# Program is the interface for the game
# Created 1/21/2022

from .card import Card

class Interface:

    def __init__(self):
        self.score = int(300)
        self.card = Card()


    def start_game(self):
        done = False
        while (not done):
            # Get the previous drawn card and output
            prevValue = int(self.card.cardValue)
            print("The card is: " + str(prevValue))

            # Guess whether the card is lower or higher
            hl = input("Higher or lower? [h/l] ")

            # Get next card value and see if we get or lose points
            newValue = int(self.card.drawCard())
            print("Next card was: " + str(newValue))
            if ((hl == 'h') and (newValue>prevValue)):
                self.score += 100
            if ((hl == 'h') and (newValue<prevValue)):
                self.score -= 75
            if ((hl == 'l') and (newValue<prevValue)):
                self.score += 100
            if ((hl == 'l') and (newValue>prevValue)):
                self.score -= 75
            print("Your score is: " + str(self.score))

            # Check to see if game is over due to running out of points
            if (self.score <= 0):
                print("You've lost all your points. Game over!")
                done = True

            # See if the player wants to play again
            if (not done):
                again = input("Play again? [y/n] ")
                if (again == 'n'):
                    done = True
