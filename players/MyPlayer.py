from players.Player import Player
from game.TablutAshtonGame import TablutAshtonGame
import numpy as np
from game.ChessBoard import ChessBoard

inf = float('inf')
class MyPlayer(Player):
    def move(self,game,chessboard,opponent):
        return self.alphabeta_cutoff(game.clone(),opponent)

        
    def euristic(self,chessboard):
        
        k=tuple(np.where(chessboard==2).reshape(2))
        if (k[0] >= 3 and k[0] <= 5) and (k[1] >= 3 and k[1] <= 5):
            return 2
        elif k in Chessboard.EXIT_INDICES:
            return 0
        else:
            return 1



        
        

    def alphabeta_cutoff(self,game,opponent, d=4, cutoff_test=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

    
        current=self
        # Functions used by alphabeta
        def max_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return current.euristic(state.getBoard())
            v = -inf
            for a in current.actions(state):
                v = max(v, min_value(state.result(*a),
                                    alpha, beta, depth + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return current.euristic(state.getBoard())
            v = inf
            for a in opponent.actions(state):
                v = min(v, max_value(state.result(*a),
                                    alpha, beta, depth + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        # Body of alphabeta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        cutoff_test = (cutoff_test or
                    (lambda state, depth: depth > d or
                                            game.checkWin()))
        best_score = -inf
        beta = inf
        best_action = None
        for a in current.actions(game):
            v = min_value(game.result(*a), best_score, beta,1)
            if v > best_score:
                best_score = v
                best_action = a
        return best_action


        

