class State:
    def __init__(self, chessboard):
        self.turn = 0 #0 = WHITE, 1 = BLACK
        self.chessboard = init_state