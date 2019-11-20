from players.Player import Player
from game.TablutAshtonGame import TablutAshtonGame
import numpy as np
from game.ChessBoard import ChessBoard

inf = float('inf')
class AlphaBetaPlayer(Player):
    def __init__(self, isWhite, depth):
        super().__init__(isWhite, False)
        self.depth = depth
        self.infinite = inf

    def move(self,game,chessboard,opponent):
        return self.alphabeta_cutoff(game.clone(), opponent)
    
    #FUNZIONE EURISTICA -> MOSSA + CONVENIENTE HA IL PUNTEGGIO MAGGIORE
    def euristic(self, chessboard, move, depth): raise NotImplementedError

    def cutoff(self, state, depth):
        return depth > self.depth or state.checkWin()
    
    def max_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, currentMove):
        if self.cutoff(state, depth):
            return opponent.euristic(state, currentMove, depth) if hasattr(opponent, 'euristic') else inf
        v = -inf
        L = self.actions(state)
        for move in L:
            currentState = state.result(*move, False, myTurn)
            v = max(v, self.min_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, currentMove):
        if self.cutoff(state, depth):
            return self.euristic(state, currentMove, depth)
        v = inf
        L = opponent.actions(state)
        for move in L:
            currentState = state.result(*move, False, opponentTurn)
            v = min(v, self.max_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def alphabeta_cutoff(self,game, opponent):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

        # Body of alphabeta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        d = self.depth
        best_score = -inf
        beta = inf
        best_action = None
        myTurn = 0 if self.isWhite() else 1
        opponentTurn = 0 if opponent.isWhite() else 1
        L = self.actions(game)
        M = []
        for move in L:
            currentState = game.result(*move, False, myTurn)
            v = self.min_value(currentState, best_score, beta, 1, opponent, myTurn, opponentTurn, move)
            M.append((*move, v))
            if v > best_score:
                best_score = v
                best_action = move
        return best_action


        

