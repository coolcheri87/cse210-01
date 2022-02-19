
import pyray
import random
import sys
sys.path.append('..')
from faller.gem import Gem
from faller.rock import Rock
from player.player import Player

class Interface:

    def __init__(self, player):
        # Setup screen size!
        self._width = 40
        self._maxHeight = 15

        # Get player
        self._player = player
        self._player.moveX(self._width,random.randint(0,self._width-1))

        # Setup fallers!
        print('Initializing rocks and gems...')
        self._fallers = []
        for i in range(0,self._width):
            if (random.randint(0,1) == 0):
                self._fallers.append(Rock(self._maxHeight))
            else:
                self._fallers.append(Gem(self._maxHeight))

    def start_game(self):
        loops = 0

        while (loops < 5):
            # Output screen...
            self.outputScreen()
            # Get user input...

            # Have items fall and reset fallen
            for i in range(0,self._width):
                self._fallers[i].fall()
                if (self._fallers[i].getHeight()==self._maxHeight):
                    if (self._player.getX()==i):
                        self._player.setImpact(self._fallers[i].getImpact())
                    self._fallers[i].resetHeight()

            # End game if requested
            loops += 1
            

    def outputScreen(self):
        # Input top line
        line = '+'
        for i in range (0,self._width):
            line += '-'
        print(line + '+')

        # Input stuff in the sky...
        for i in range (0,self._maxHeight):
            line = '|'
            for j in range (0,self._width):
                if (self._fallers[j].getHeight()==i):
                    line +=self._fallers[j].getSymbol()
                else:
                    line += ' '
            print (line + "|")

        # Input stuff on the ground...
        line = '['
        for i in range (0,self._width):
            if (self._player.getX() == i):
                line += '#'
            elif (self._fallers[j].getHeight()==self._maxHeight):
                line +=self._fallers[j].getSymbol()
            else:
                line += ' '
        print(line + ']')

        # Input bottom line
        line = '+'
        for i in range (0,self._width):
            line += '-'
        print(line + '+')
        print('Score for ' + self._player.getName() + ' is: ' + str(self._player.getScore()))
        print('Player position is: ' + str(self._player.getX()))

