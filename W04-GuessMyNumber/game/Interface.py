# Cheri Hansen - han19067@byui.edu
# Program is the interface for the game
# Created 1/28/2022

from .card import Card

# This is Interface to play guess my number game
# This is interface class 
class Interface:

    # This is initializing score and guess number
    def __init__(self):
        self.i = 0
        self.card = Card()
    
     

    # This is where the game is played
    def start_game(self):
        done = False

        # This is main game loop
        while (not done):
            # Get the previous drawn guess number and output
            prevValue = int(self.card.cardValue)
            print("The card is: " + str(prevValue))

            # Guess whether the guess number is hot or cold
            hl = self.getHigherLower()

            # Get next card value and see if we get or lose points
            newValue = int(self.card.drawCard())
            print("Next card was: " + str(newValue))
            if ((hl == 'h') and (newValue>prevValue)):
                self.score += 100
            if ((hl == 'h') and (newValue<prevValue)):
                self.score -= 50
            if ((hl == 'l') and (newValue<prevValue)):
                self.score += 100
            if ((hl == 'l') and (newValue>prevValue)):
                self.score -= 50
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
#This is UserNumberGuess class
class UserNumberGuess:

    # This is initializing guess number
    def __init__(self):
        self. i =0


    # This function keeps asking for a response until it gets a y or n...
    def playAgain(self):
        validInput = False
        #loop until player is done with game
        while (not validInput):
            again = input("Play again? [y/n] ").lower()
            if ((again == 'y') or (again == 'n')):
                validInput = False
                return again

    # This function keeps asking for a response until it gets h or l
    def getHigherLower(self):
        validInput = False
        #loop until player has right input
        while (not validInput):
            hilo = input("higher or lower [h/l] ").lower()
            if ((hilo == 'h') or (hilo == 'l')):
                validInput = False
                return hilo