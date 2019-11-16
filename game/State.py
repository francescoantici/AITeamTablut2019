class State:
    def __init__(self, playboard):
        self.turn = 0 #0 = WHITE, 1 = BLACK
        self.playboard = init_state