
import sys
sys.path.append('..')
from player.score import Score


class Player:

    def __init__(self,name):
        self._name = name
        self._x = 0
        self._score = Score()

    # Getters
    def getName(self):
        return self._name

    def getScore(self):
        return self._score.getScore()

    def getSymbol(self):
        return '#'

    def getX(self):
        return self._x

    # Setters
    def setImpact(self,impact):
        return self._score.setImpact(impact)

    def moveX(self,width,move):
        self._x += move
        if (self._x < 0):
            self._x = 0
        if (self._x >= width):
            self._x = width -1



