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

    def cutoff(self, state, depth, move):
        return depth > self.depth or state.checkWin(move)
    
    def max_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, currentMove):
        if self.cutoff(state, depth, currentMove):
            return opponent.euristic(state, currentMove, depth) if hasattr(opponent, 'euristic') else inf
        v = -inf
        for move in self.actions(state):
            currentState = state.result(*move, True, myTurn)
            v = max(v, self.min_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, currentMove):
        if self.cutoff(state, depth, currentMove):
            return self.euristic(state, currentMove, depth)
        v = inf
        for move in opponent.actions(state):
            currentState = state.result(*move, True, opponentTurn)
            v = min(v, self.max_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def alphabeta_cutoff(self, game, opponent):
        best_score = -inf
        beta = inf
        best_action = None
        myTurn = self.turn()
        opponentTurn = -myTurn
        for move in self.actions(game):
            currentState = game.result(*move, True)
            v = self.min_value(currentState, best_score, beta, 1, opponent, myTurn, opponentTurn, move)
            if v > best_score:
                best_score = v
                best_action = move
        return best_action


        

