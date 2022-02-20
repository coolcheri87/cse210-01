
import pyray
import sys
sys.path.append('.')
from game.interface import Interface
from player.player import Player

# main function that starts program
def main():
    # Set player username
    player = Player('Cheri')
    print('Welcome to the game ' + player.getName() + '!')

    # Start the game
    io = Interface(player)
    io.start_game()


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()

