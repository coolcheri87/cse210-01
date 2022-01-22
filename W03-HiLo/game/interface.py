# Cheri Hansen - han19067@byui.edu
# Program is the interface for the game
# Created 1/21/2022

from .card import Card


# This is Interface to play hilo game
class Interface:

    # This is initializing score and card
    def __init__(self):
        self.score = int(300)
        self.card = Card()

    # This is where the game is played
    def start_game(self):
        done = False

        # This is main game loop
        while (not done):
            # Get the previous drawn card and output
            prevValue = int(self.card.cardValue)
            print("The card is: " + str(prevValue))

            # Guess whether the card is lower or higher
            hl = self.getHigherLower()

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
                again = self.playAgain()
                if (again == 'n'):
                    done = True
                else:
                    print()

    def playAgain(self):
        validInput = False
        #loop until player is done with game
        while (not validInput):
            again = input("Play again? [y/n] ").lower()
            if ((again == 'y') or (again == 'n')):
                validInput = False
                return again

    def getHigherLower(self):
        validInput = False
        #loop until player has right input
        while (not validInput):
            hilo = input("higher or lower [h/l] ").lower()
            if ((hilo == 'h') or (hilo == 'l')):
                validInput = False
                return hilo