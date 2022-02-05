# Cheri Hansen


class Jumper:
    
    # This is initializing score and card
    def __init__(self):
        self._tries = 0

    def getJumper(self,guess):
        self._tries -= guess
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
            return True
        print (' /|\  ')
        print (' / \  ')
        print ()
        print ('^^^^^^')
        return False

