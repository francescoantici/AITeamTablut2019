from players.Player import Player
import numpy as np

class RandomPlayer(Player):
    def __init__(self, isWhite = False):
        super().__init__()
        self.__isWhite = isWhite
    
    def isWhite(self): return self.__isWhite

    def play(self, chessboard):
        elSign = 1 if self.__isWhite else -1
        act = []
        for row in chessboard:
            for pawn in row:
                if np.sign(pawn.value) != elSign: continue
                act.append((pawn.x, pawn.y, self.__getMoves(pawn, chessboard)))

        np.random.shuffle(act)
        act = act[0]
        np.random.shuffle(act[2])
        return ((act[0], act[1]), (act[2][0][0], act[2][0][1]))
    
    def __getMoves(self, pawn, chessboard):
        M = []
        for i in range(1, 9):
            xi = pawn.x + i
            if xi >= 0 and xi <= 8:
                if chessboard[xi][pawn.y].value == 0: M.append((xi, pawn.y))
                else: break

        for i in range(1, 9):
            xi = pawn.x - i
            if xi >= 0 and xi <= 8:
                if chessboard[xi][pawn.y].value == 0: M.append((xi, pawn.y))
                else: break

        for i in range(1, 9):
            yi = pawn.y + i
            if yi >= 0 and yi <= 8:
                if chessboard[pawn.x][yi].value == 0: M.append((pawn.x, yi))
                else: break
        
        for i in range(1, 9):
            yi = pawn.y - i
            if yi >= 0 and yi <= 8:
                if chessboard[pawn.x][yi].value == 0: M.append((pawn.x, yi))
                else: break

        return M

    def onWin(self, winner, moves):
        if winner:
            f = open('./data/games.random.tablut', 'a')
            f.write(str(moves) + '\n')
        return self


class RandomWhitePlayer(RandomPlayer):
    def __init__(self): super().__init__(True)

class RandomBlackPlayer(RandomPlayer):
    def __init__(self): super().__init__(False)