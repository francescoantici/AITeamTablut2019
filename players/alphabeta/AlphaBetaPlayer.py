from players.Player import Player
from game.TablutAshtonGame import TablutAshtonGame
from game.ChessBoard import ChessBoard
import time
import numpy as np

inf = float('inf')
class AlphaBetaPlayer(Player):
    def __init__(self, isWhite, depth, timer = 50, verbose = False):
        super().__init__(isWhite, False)
        self.depth = depth
        self.infinite = inf
        self.verbose = verbose
        self.timer = timer
        self.__startTime = 0
        
    def now(self): return time.time() - self.__startTime

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
        for move in self.shuffle(self.actions(state)):
            if self.now() >= self.timer: break
            currentState = state.result(*move, True, myTurn)
            v = max(v, self.min_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v >= beta: return v
            alpha = max(alpha, v)
        return v

    def min_value(self, state, alpha, beta, depth, opponent, myTurn, opponentTurn, currentMove):
        if self.cutoff(state, depth, currentMove):
            return self.euristic(state, currentMove, depth)
        v = inf
        for move in self.shuffle(opponent.actions(state)):
            if self.now() >= self.timer: break
            currentState = state.result(*move, True, opponentTurn)
            v = min(v, self.max_value(currentState, alpha, beta, depth + 1, opponent, myTurn, opponentTurn, move))
            if v <= alpha: return v
            beta = min(beta, v)
        return v

    def alphabeta_cutoff(self, game, opponent):
        best_score = -inf
        beta = inf
        best_action = None
        myTurn = self.turn()
        opponentTurn = -myTurn
        self.__startTime = time.time()
        self.now()
        for move in self.shuffle(self.actions(game)):
            if self.now() >= self.timer: break
            currentState = game.result(*move, True)
            v = self.min_value(currentState, best_score, beta, 1, opponent, myTurn, opponentTurn, move)
            if v > best_score:
                best_score = v
                best_action = move
        return best_action

    def shuffle(self, array):
        np.random.shuffle(array)
        return array

    def printMossa(self, parents):
        if self.verbose:
            string = 'MOSSA '
            for parent in parents: string += '{}/{} '.format(*parent)
            print(string, end='\r')


        

