
from .gravity import Gravity

class Faller:

    def __init__(self):
        self._height = 0
        self._gravity = Gravity()

    def getHeight(self):
        return self._height

    def resetHeight(self):
        self._height = 0
        return 0

    def fall(self):
        self._height += self._gravity.getFall()
        if (self._height > self._maxHeight):
            self._height = self._maxHeight
        return self._height
