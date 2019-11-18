class Player:
    def __init__(self, human = False): self.__human = human
    def human(self): return self.__human
    def play(self, chessboard): raise NotImplementedError
    def onWin(self, winner, moves): print(winner, moves); return self
    def onError(self, type, error): return self