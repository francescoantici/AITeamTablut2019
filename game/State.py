class State:
    def __init__(self, playboard):
        self.turn = 0 #0 = WHITE, 1 = BLACK
        self.playboard = playboard
        self.camps=[(0,3),(0,4),(0,5),(1,4),(3,0),(4,0),(5,0),(4,1),(4,7),(3,8),(4,8),(5,8),(7,4),(8,3),(8,4),(8,5)]
    
    def to_move(self):
        if self.turn:
            self.turn=0
        else:
            self.turn=1
        return self.turn