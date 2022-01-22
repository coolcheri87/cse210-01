# Cheri Hansen - coolchei87@gmail.com
# CSE 210 - Week 2
# This program plays Tic Tac Toe
# W02 Prove: Developer - Solo Code Submission

# This is a Tic-Tac-Toe Class
class TTTBoard:
    def __init__(self,size):
        self.size = size
        # validate size for 3-9
        if (int(self.size)<3):
            self.size = 3
        if (int(self.size)>9):
            self.size = 9
        # Create dynamic array
        self.ttt = []
        for i in range(1,int(self.size)*int(self.size)+1):
            self.ttt.append(str(i))

    # This is for outputting a 3x3 to 8x8 tic-tac-toe board
    def outputTTT(self):
        line = ''
        for i in range(0,int(self.size)):
            x = int(i)*int(self.size)+1
            if (len(self.ttt[int(x)-1]) == 1):
                line = "  " + self.ttt[int(x)-1]
            else:
                line = " " + self.ttt[int(x)-1]
            for j in range(1,int(self.size)):
                x = int(i)*int(self.size)+int(j)+1
                if (len(self.ttt[int(x)-1]) == 1):
                    line = line + "|  " + self.ttt[int(x)-1]
                else:
                    line = line + "| " + self.ttt[int(x)-1]
            print(line)
            line = "---"
            if (int(i) < (int(self.size)-1)):
                for j in range(1,int(self.size)):
                    line = line + "+---"
                print(line)

    # this is for getting player input...
    def getPlayerInput(self,player):
        square = 1
        squared = int(self.size) ** 2
        validInput = False

        while (validInput == False):
            validInput = True

            # Request square to play
            square = input(player + "'s turn to choose a square (1 - " + str(squared) + "): ")

            # Validate if in range
            if ((int(square)<1) or (int(square)>int(squared))):
                validInput = False
                print("Entry of " + square + " is outside the range of 1 to " + str(squared) + ". Please try again!")
            
            # Validate if already played
            if ((validInput == True) and ((self.ttt[int(square)-1]=='X') or (self.ttt[int(square)-1]=='O')) ):
                validInput = False
                print("Entry of " + square + " has already been played. Please try again!")

        return square

    # This is to see if a game is over...
    def seeIfDone(self):
        done = False

        # Check to find horizontal winners
        for i in range(0,int(self.size)): # rows
            matching = True
            for j in range(0,int(self.size)-1): # columns
                if (self.ttt[j+i*int(self.size)] != self.ttt[j+i*int(self.size)+1]):
                    matching = False
            if (matching == True):
                done = True
                print("Player " + self.ttt[i*int(self.size)] + " has won the game!")

        # Check to find vertical winners
        if (done == False):
            for i in range(0,int(self.size)): # columns
                matching = True
                for j in range(0,int(self.size)-1): # rows
                    if (self.ttt[i+j*int(self.size)] != self.ttt[i+(j+1)*int(self.size)]):
                        matching = False
                if (matching == True):
                    done = True
                    print("Player " + self.ttt[j*int(self.size)] + " has won the game!")

        # Check to find diagonal upper-left to bottom-right winners on odd sized boards
        if ( (done == False) and ( (int(self.size)%2) == 1) ):
            matching = True
            for i in range(0,int(self.size)-1): # rows
                if (self.ttt[i*(int(self.size)+1)] != self.ttt[(i+1)*(int(self.size)+1)]):
                    matching = False
            if (matching == True):
                    done = True
                    print("Player " + self.ttt[0] + " has won the game!")
        
        # Check to find diagonal upper-right to bottom left winners on odd sized boards
        if ( (done == False) and ( (int(self.size)%2) == 1) ):
            matching = True
            for i in range(1,int(self.size)):
                if (self.ttt[(int(i))*(int(self.size)-1)] != self.ttt[(int(i)+1)*(int(self.size)-1)]):
                    matching = False
            if (matching == True):
                    done = True
                    print("Player " + self.ttt[int(self.size)-1] + " has won the game!")
        
        # Check to see if a cat game (or draw or tie)...
        if (done == False):
            done = True
            for i in range(1,int(self.size)*int(self.size)+1):
                if (self.ttt[i-1] == str(i)):
                    done = False
            if (done == True):
                print("All squares used - This is a 'cat' game (or draw or tie).")

        return done


def main():
    # Setup the board
    done = False
    size = input("What size Tic-Tac-Toe Board do you want (3-9):")
    board = TTTBoard(size)
    ttt = board.ttt
    print("This is Cheri's Tic-Tac-Toe game:")

    # Loop until game done
    while(done == False):
    
        # Allow each player to play
        players = ["X","O"]
        for player in players:
            if (done == False):
                # Output Tic-Tac-Toe board
                board.outputTTT()
                # Get validated player input
                square = board.getPlayerInput(player)
                # Set player input
                ttt[int(square) - 1] = player
                print("")
                # Check to see if game done
                done = board.seeIfDone()

    # Output final board
    board.outputTTT()


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()
