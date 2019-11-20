from game.ChessBoard import ChessBoard
from players.alphabeta.AlphaBetaPlayer import AlphaBetaPlayer

class PlayerBlack(AlphaBetaPlayer):
    def __init__(self, depth): super().__init__(False, depth)

    def euristic(self, chessboard):
        return 0