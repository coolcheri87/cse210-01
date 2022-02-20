
import pyray
import random
from .faller import Faller
from .gravity import Gravity

class Gem(Faller):

    def __init__(self,maxHeight):
        super().__init__()
        self.gravity = Gravity()
        self.gravity.setMoontGravity
        self._maxHeight = maxHeight
        # Setup random position in the top two thirds of play
        self._height = random.randint(0,maxHeight*2/3)

    def fall(self):
        self._height += self.gravity.getFall()
        if (self._height > self._maxHeight):
            self._height = self._maxHeight
        return self._height

    def getImpact(self):
        return 1

    def getSymbol(self):
        if (self._height<8):
            return '*'
        else:
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