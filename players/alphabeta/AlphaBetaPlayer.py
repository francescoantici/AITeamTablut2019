from players.Player import Player
from game.TablutAshtonGame import TablutAshtonGame
import numpy as np
from game.ChessBoard import ChessBoard

inf = float('inf')
class AlphaBetaPlayer(Player):
    def __init__(self, isWhite, depth):
        super().__init__(isWhite, False)
        self.depth = depth

    def move(self,game,chessboard,opponent):
        return self.alphabeta_cutoff(game.clone(), opponent)
        
    def euristic(self, chessboard): raise NotImplementedError
    
    def max_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, cutoff_test):
        if cutoff_test(state, depth):
            return self.euristic(state.getBoard())
        v = -inf
        L = self.actions(state)
        for a in L:
            currentState = state.result(*a, False, myTurn)
            v = max(v, self.min_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, cutoff_test))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, cutoff_test):
        if cutoff_test(state, depth):
            return self.euristic(state.getBoard())
        v = inf
        L = opponent.actions(state)
        for a in L:
            currentState = state.result(*a, False, opponentTurn)
            v = min(v, self.max_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, cutoff_test))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def alphabeta_cutoff(self,game, opponent, cutoff_test=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

        # Body of alphabeta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        d = self.depth
        cutoff_test = (cutoff_test or (lambda state, depth: depth > d or state.checkWin()))
        best_score = -inf
        beta = inf
        best_action = None
        myTurn = 0 if self.isWhite() else 1
        opponentTurn = 0 if opponent.isWhite() else 1
        L = self.actions(game)
        for move in L:
            currentState = game.result(*move, False, myTurn)
            v = self.min_value(currentState, best_score, beta, 1, opponent, myTurn, opponentTurn, cutoff_test)
            if v > best_score:
                best_score = v
                best_action = move
        return best_action


        

