# Cheri Hansen - han19067@byui.edu
# Program to run HiLo game
# Created 2/1/2022
# CSE 210-02 W03 hilo card game 

from game.interface import Interface

# main function that starts program
def main():
    interface = Interface()
    interface.start_game()


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()
