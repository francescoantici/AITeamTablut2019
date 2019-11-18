from players.Player import Player
from game.TablutAshtonGame import TablutAshtonGame
import numpy as np

inf = float('inf')
class MyPlayer(Player):
    def move(self,game,chessboard,opponent):
        return self.alphabeta_cutoff(game.clone(),opponent)

        
    def euristic(self,chessboard):
        return np.rand.uniform(0,1)

    def alphabeta_cutoff(game,opponent, d=4, cutoff_test=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

    
    
        # Functions used by alphabeta
        def max_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return self.euristic(state.getPawnBoard())
            v = -inf
            for a in self.actions(state):
                v = max(v, min_value(state.result(*a),
                                    alpha, beta, depth + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(state, alpha, beta, depth):
            if cutoff_test(state, depth):
                return self.euristic(state.getPawnBoard())
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
        for a in game.actions(state):
            v = min_value(game.result(*a), best_score, beta)
            if v > best_score:
                best_score = v
                best_action = a
        return best_action


        

