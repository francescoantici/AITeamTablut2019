class State:
    def __init__(self, playboard):
        self.__turn = 0 #0 = WHITE, 1 = BLACK
        self.__playboard = playboard
    
    def to_move(self):
        if self.turn:
            self.turn=0
        else:
            self.turn=1
        return self.turn