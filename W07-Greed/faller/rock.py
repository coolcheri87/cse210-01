
import pyray
import random
from .faller import Faller
from .gravity import Gravity

class Rock(Faller):

    def __init__(self,maxHeight):
        super().__init__()
        self._gravity.setJupiterGravity
        self._maxHeight = maxHeight
        # Setup random position in the top two thirds of play
        self._height = random.randint(0,int(maxHeight*2/3))

    def getImpact(self):
        return -1

    def getSymbol(self):
        return 'o'

    def getColor(self):
        return pyray.BROWN