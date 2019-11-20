from game.ChessBoard import ChessBoard
from players.alphabeta.AlphaBetaPlayer import AlphaBetaPlayer
import numpy as np

class PlayerWhite(AlphaBetaPlayer):
    def __init__(self, depth): super().__init__(True, depth)

    def euristic(self, chessboard):
        k=tuple(np.array(np.where(chessboard==2)).reshape(2))
        if (k[0] >= 3 and k[0] <= 5) and (k[1] >= 3 and k[1] <= 5):
            return 2
        elif k in ChessBoard.EXIT_INDICES:
            return 0
        else:
            return 1