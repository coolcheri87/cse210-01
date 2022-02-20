
import random
import sys
sys.path.append('..')
from .keyboardService import KeyboardService
from .screenService import ScreenService
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

        # Setup keyboard and screen stuff
        self._keyboardService = KeyboardService()
        self._screenService = ScreenService(self._width,self._maxHeight,self._fallers)
        self._screenService.open_window()

    def start_game(self):

        while self._screenService.is_window_open():
            # Output screen...
            self.outputScreen()

            # Get user input...
            self._player.moveX(self._width,self._keyboardService.get_direction())

            # Have items fall and reset fallen
            for i in range(0,self._width):
                self._fallers[i].fall()
                if (self._fallers[i].getHeight()==self._maxHeight):
                    if (self._player.getX()==i):
                        self._player.setImpact(self._fallers[i].getImpact())
                    self._fallers[i].resetHeight()

            

    def outputScreen(self):

        # Input stuff in the sky...
        self._screenService.draw_fallers(self._fallers)

        # draw player
        self._screenService.draw_player(self._player)

        print('Score for ' + self._player.getName() + ' is: ' + str(self._player.getScore()))
        print('Player position is: ' + str(self._player.getX()))

