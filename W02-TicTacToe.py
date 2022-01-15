# Cheri Hansen - coolchei87@gmail.com
# CSE 210 - Week 2
# This program plays Tic Tac Toe
# W02 Prove: Developer - Solo Code Submission


# This is the Tic-Tac-Toe output function
def outputTTT(ttt):
    print(" " + ttt[0] + " | " + ttt[1] + " | " + ttt[2])
    print("---+---+---")
    print(" " + ttt[3] + " | " + ttt[4] + " | " + ttt[5])
    print("---+---+---")
    print(" " + ttt[6] + " | " + ttt[7] + " | " + ttt[8])


# This is the function to see if the game is over
def seeIfDone(ttt):
    done = False
    
    # This is to find horizsontal winners
    if ((ttt[0]==ttt[1]) and (ttt[1]==ttt[2])):
        print("Player " + ttt[0] + " has won the game!")
        done = True
    elif ((ttt[3]==ttt[4]) and (ttt[4]==ttt[5])):
        print("Player " + ttt[3] + " has won the game!")
        done = True
    elif ((ttt[6]==ttt[7]) and (ttt[7]==ttt[8])):
        print("Player " + ttt[6] + " has won the game!")
        done = True
        
    # This is to find vertical winners
    if ((ttt[0]==ttt[3]) and (ttt[3]==ttt[6])):
        print("Player " + ttt[0] + " has won the game!")
        done = True
    elif ((ttt[1]==ttt[4]) and (ttt[4]==ttt[7])):
        print("Player " + ttt[1] + " has won the game!")
        done = True
    elif ((ttt[2]==ttt[5]) and (ttt[5]==ttt[8])):
        print("Player " + ttt[2] + " has won the game!")
        done = True
        
    # This is to find diagonal winners
    if ((ttt[0]==ttt[4]) and (ttt[4]==ttt[8])):
        print("Player " + ttt[0] + " has won the game!")
        done = True
    elif ((ttt[2]==ttt[4]) and (ttt[4]==ttt[6])):
        print("Player " + ttt[2] + " has won the game!")
        done = True

    # Find a cat game
    if ((ttt[0]!="1") and (ttt[1]!="2") and (ttt[2]!="3") and (ttt[3]!="4") and (ttt[4]!="5") and (ttt[5]!="6") and(ttt[6]!="7") and (ttt[7]!="8") and (ttt[8]!="9")):
        print("It's a cat game (a draw). Nobody won...")
        done = True

    return done
    

# Validate input
def getPlayerInput(ttt,player):
    square = 1
    validInput = False

    while (validInput == False):
        validInput = True

        square = input(player + "'s turn to choose a square (1-9):")

        # Validate if in range or not already played
        if ((int(square)<1) or (int(square)>9)):
            validInput = False
            print("Entry of " + square + " is outside the range of 1 to 9.")
        else:
            if ((ttt[int(square)-1]=='X') or (ttt[int(square)-1]=='O')):
                validInput = False
                print("That location has been played before.Please try again!")

    return square


def main():
    # Setup the board
    done = False
    ttt = ["1","2","3","4","5","6","7","8","9"]
    print("This is Cheri's Tic-Tac-Toe game:")

    # Loop until game done
    while(done == False):
    
        # Allow each player to play
        players = ["X","O"]
        for player in players:
            if (done == False):
                # Output Tic-Tac-Toe board
                outputTTT(ttt)
                # Get validated player input
                square = getPlayerInput(ttt,player)
                # Set player input
                ttt[int(square) - 1] = player
                print("")
                # Check to see if game done
                done = seeIfDone(ttt)


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()
