# Cheri Hansen  - han19067@byui.edu
# Program is the interface for the juumper game
# Created 2/1/2022


class Jumper:
    
    # This is initializing number of unsuccessful tries
    def __init__(self):
        self._tries = 0

    # Display word guessing status and our jumper graphic
    def getJumper(self,guess,displayWord):

        # Output displayWord list in a nice format
        output = ''
        for i in range(len(displayWord)):
            output += ' ' + displayWord[i]
        print(output + "\n")

        # Track wrong guesses
        self._tries += guess

        if (self._tries == 0):
            print (' ---  ')
            print ('/   \ ')
            print (' ---  ')
            print ('\   / ')
            print (' \ /  ')
            print ('  O   ')
        if (self._tries == 1):
            print ('/   \ ')
            print (' ---  ')
            print ('\   / ')
            print (' \ /  ')
            print ('  O   ')
        if (self._tries == 2):
            print (' ---  ')
            print ('\   / ')
            print (' \ /  ')
            print ('  O   ')
        if (self._tries == 3):
            print ('\   / ')
            print (' \ /  ')
            print ('  O   ')
        if (self._tries == 4):
            print (' \ /  ')
            print ('  O   ')
        if (self._tries > 4):
            print ('  X   ')
            print (' /|\  ')
            print (' / \  ')
            print ('^^^^^^')
            print ()
            print ("Sorry your jumper didn't make it...\n")
            return True
        print (' /|\  ')
        print (' / \  ')
        print ()
        print ('^^^^^^')
        return False

