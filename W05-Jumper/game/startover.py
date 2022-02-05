




class StartOver:

    
    def __init__(self):
        self.question = 'S'

    def startover(self):
        self.question = 'S'
      
        while ((self.question != 'Y') and (self.question != 'N')):
            self.question = input("Would you like to play again (Y/N)? ")
            self.question = self.question[0].upper()

        if (self.question == 'Y'):
            return False
        
        return True

