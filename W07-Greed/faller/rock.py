
import random
from .faller import Faller
from .gravity import Gravity

class Rock(Faller):

    def __init__(self,maxHeight):
        super().__init__()
        self.gravity = Gravity()
        self.gravity.setJupiterGravity
        self._maxHeight = maxHeight
        # Setup random position in the top two thirds of play
        self._height = random.randint(0,maxHeight*2/3)

    def fall(self):
        self._height += self.gravity.getFall()
        if (self._height > self._maxHeight):
            self._height = self._maxHeight
        return self._height

    def getImpact(self):
        return -1

    def getSymbol(self):
        if (self._height<8):
            return '.'
        else:
            return 'x'

