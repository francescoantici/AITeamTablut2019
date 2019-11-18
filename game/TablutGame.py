from game.ChessBoard import ChessBoard
from game.Errors import WonGameMove
import numpy as np

class TablutGame:
    def __init__(self, initial = None):
        self.chessboard = ChessBoard(initial)
        self.turn = 0
        self.won = 0

    def getBoard(self): return self.chessboard.copyArray()
    def getPawnBoard(self): return self.chessboard.getBoard()
    def getBoardIterator(self): return self.chessboard.getIteratorList()
    def getTurn(self): return self.turn
    def getPawn(self, x, y): return self.chessboard.get(x, y)
    def getWinner(self): return self.won
    def clone(self): return self.__class__(self.getBoard())
    def __str__(self): return str(self.__chessboard)

    def result(self, start, end): return self.clone().move(start, end)

    def move(self, start, end):
        if self.won: raise WonGameMove(start, end)

        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0 or start[0] > 8 or start[1] > 8 or end[0] > 8 or end[1] > 8: raise OutOfBoardMove(start, end)

        self.checkMove(start, end)
        s = self.chessboard.get(*start)

        self.chessboard.set(start[0], start[1], 0)
        self.chessboard.set(end[0], end[1], s)

        self.checkEatAndWin(*end)

        self.turn += 1
        self.turn %= 2
        return self

    def checkMove(self, start, end): raise NotImplementedError

    def win(self, player):
        self.won = player
        return self

    def eat(self, x, y):
        self.chessboard.set(x, y, 0)
        return self

    def checkEatAndWin(self, x, y):

        eats = [
            self.checkEat(x - 1, y),
            self.checkEat(x + 1, y),
            self.checkEat(x, y - 1),
            self.checkEat(x, y + 1)
        ]

        winner = self.checkWin(self)
        if winner: return self.win(winner)

        return self
    
    def checkWin(self):

        kingpos = np.where(self.getBoard() == 2)

        kingEat = self.checkEat(kingpos[0][0], kingpos[1][0], False)
        if kingEat == 2: return -1
        
        map = self.getBoard()
        filterMap = ChessBoard.MAPARRAY == 1
        boardMap = map[filterMap]
        kingMap = (boardMap == 2)
        if kingMap.any(): return 1

        wCan = False
        bCan = False
        for e, m, i, j in self.chessboard:
            if wCan and bCan: break
            elif e == 0: continue
            elif e > 0 and not wCan: wCan = self.canMove(i, j)
            elif e < 0 and not bCan: bCan = self.canMove(i, j)

        if not wCan: return -1
        elif not bCan: return 1

        return 0

    def canMove(self, x, y):
        nocc = (2, 4)
        eneight = [
            5 if x < 1 else self.chessboard.get(x - 1, y),
            5 if x > 7 else self.chessboard.get(x + 1, y),
            5 if y < 1 else self.chessboard.get(x, y - 1),
            5 if y > 7 else self.chessboard.get(x, y + 1)
        ]
        mneight = [
            5 if x < 1 else self.chessboard.getMap(x - 1, y),
            5 if x > 7 else self.chessboard.getMap(x + 1, y),
            5 if y < 1 else self.chessboard.getMap(x, y - 1),
            5 if y > 7 else self.chessboard.getMap(x, y + 1)
        ]
        neight = [ eneight[i] or mneight[i] in nocc for i in range(4) ]
        return False in neight

    def checkEat(self, x, y, eat = True):
        if x < 0 or y < 0 or x > 8 or y > 8: return 0
        current = self.chessboard.get(x, y)
        if not current: return 0
        elSign = np.sign(current)
        nocc = (2, 4)

        eneight = [
            0 if x < 1 else self.chessboard.get(x - 1, y),
            0 if x > 7 else self.chessboard.get(x + 1, y),
            0 if y < 1 else self.chessboard.get(x, y - 1),
            0 if y > 7 else self.chessboard.get(x, y + 1)
        ]
        mneight = [
            0 if x < 1 else self.chessboard.getMap(x - 1, y),
            0 if x > 7 else self.chessboard.getMap(x + 1, y),
            0 if y < 1 else self.chessboard.getMap(x, y - 1),
            0 if y > 7 else self.chessboard.getMap(x, y + 1),
            self.chessboard.getMap(x, y)
        ]
        neight = [ (eneight[i] and np.sign(eneight[i]) != elSign) or (mneight[4] != 2 and mneight[i] in nocc) for i in range(4) ]

        isKing = current == 2
        vSupp = neight[0] and neight[1]
        hSupp = neight[2] and neight[3]
        if not isKing:
            if vSupp or hSupp:
                if eat: self.eat(x, y)
                return current
        else:
            isNearCastle = 4 in mneight
            if (isNearCastle and vSupp and hSupp) or (not isNearCastle and (vSupp or hSupp)):
                return current
        return 0

    def checkRange(self, start, end, x, y):
        if start == end: return True
        j = y if x == -1 else x
        i = start
        d = end - start
        e = np.sign(d)
        for v in range(1, abs(d)):
            a = self.chessboard.get(i + v * e, j)
            b = self.chessboard.get(j, i + v * e)
            if x == -1 and a or  y == -1 and b:
                return False
        return True

    def checkRangeMap(self, start, end, x, y, sm):
        if start == end: return True
        j = y if x == -1 else x
        i = start
        d = end - start
        e = np.sign(d)
        occ = (4, ) if sm == 2 else (2, 4)
        for v in range(1, abs(d)):
            a = self.chessboard.getMap(i + v * e, j)
            b = self.chessboard.getMap(j, i + v * e)
            if x == -1 and a in occ or  y == -1 and b in occ:
                return False
        return True