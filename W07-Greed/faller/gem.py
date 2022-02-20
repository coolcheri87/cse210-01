
import pyray
import random
from .faller import Faller
from .gravity import Gravity

class Gem(Faller):

    def __init__(self,maxHeight):
        super().__init__()
        self._gravity.setMoonGravity()
        self._maxHeight = maxHeight
        # Setup random position in the top two thirds of play
        self._height = random.randint(0,int(maxHeight*2/3))

    def getImpact(self):
        return 1

    def getSymbol(self):
        return '*'

    def getColor(self):
        c = random.randint(0,4)
        if (c==0):
            return pyray.MAGENTA
        if (c==1):
            return pyray.PURPLE
        if (c==2):
            return pyray.GREEN
        if (c==3):
            return pyray.BLUE
        return pyray.YELLOW