# Cheri Hansen - han19067@byui.edu
# Program to run HiLo game
# Created 1/21/2022

from game.interface import Interface

def main():
    interface = Interface()
    interface.start_game()


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()
