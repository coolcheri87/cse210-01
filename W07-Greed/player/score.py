

class Score:

    def __init__(self):
        self._score = 0

    def getScore(self):
        return self._score
    
    def setImpact(self,impact):
        self._score += impact
        return self._score
    