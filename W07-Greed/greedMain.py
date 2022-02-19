import sys
sys.path.append('.')
from game.interface import Interface
from player.player import Player

# main function that starts program
def main():
    # Get username
    name = 'player'
    while ( (name == 'player') or (len(name) == 0) ):
        name = input('What is your name? ')
    player = Player(name)
    print('Welcome to the game ' + player.getName() + '!')

    # Start the game
    interface = Interface(player)
    interface.start_game()


# Required for main to work correctly when called directly
if __name__ == "__main__":
    main()

