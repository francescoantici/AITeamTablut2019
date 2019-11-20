from players.Player import Player
import numpy as np

class RandomPlayer(Player):
    def __init__(self, isWhite = False):
        super().__init__(isWhite, False)
    
    def move(self, game, chessboard, opponent):
        elSign = 1 if self.isWhite() else -1
        act = self.actions(game, chessboard)
        np.random.shuffle(act)
        return act[0]

    def onWin(self, winner, moves):
        if winner:
            f = open('./data/games.random.tablut', 'a')
            f.write(str(moves) + '\n')
        return self


class RandomWhitePlayer(RandomPlayer):
    def __init__(self): super().__init__(True)

class RandomBlackPlayer(RandomPlayer):
    def __init__(self): super().__init__(False)