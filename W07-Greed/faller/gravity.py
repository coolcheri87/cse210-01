
import random

class Gravity:

    # Default to Earth Gravity
    def __init__(self):
        self._min=2
        self._max=3;

    # Getter
    def getFall(self):
        return random.randint(self._min,self._max)

    # Setters
    def setJupiterGravity(self):
        self._min=3
        self._max=4

    def setEarthGravity(self):
        self._min=2
        self._max=3;

    def setMoontGravity(self):
        self._min=1
        self._max=2

