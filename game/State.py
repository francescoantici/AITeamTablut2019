class State:
    def __init__(self, playboard):
        self.turn = 0 #0 = WHITE, 1 = BLACK
        self.playboard = playboard
        self.camps=[(0,3),(0,4),(0,5),(1,4),(3,0),(4,0),(5,0),(4,1),(4,7),(3,8),(4,8),(5,8),(7,4),(8,3),(8,4),(8,5)]
        self.escapes=[(0,1),(0,2),(0,6),(0,7),(1,0),(2,0),(6,0),(7,0),(8,1),(8,2),(8,6),(8,7),(1,8),(2,8),(6,8),(7,8)]
        self.castle=(4,4)
    
    def to_move(self):
        if self.turn:
            self.turn=0
        else:
            self.turn=1
        return self.turn
