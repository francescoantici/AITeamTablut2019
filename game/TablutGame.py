from game.ChessBoard import ChessBoard
from game.Errors import WonGameMove, OutOfBoardMove
import numpy as np

class TablutGame:
    def __init__(self, initial = None):
        self.chessboard = ChessBoard(initial)
        self.turn = ChessBoard.WHITE_PLAYER
        self.won = ChessBoard.NOBODY_PLAYER

    def getBoard(self): return self.chessboard.copyArray()
    def getPawnBoard(self): return self.chessboard.getBoard()
    def getBoardIterator(self): return self.chessboard.getIteratorList()
    def getTurn(self): return self.turn
    def getPawn(self, x, y): return self.chessboard.get(x, y)
    def getWinner(self): return self.won
    def __str__(self): return str(self.__chessboard)
    def clone(self, turn = None):
        result = self.__class__(self.getBoard())
        if turn is None: turn = self.turn
        result.turn = turn
        return result

    def result(self, start, end, checkMove = True, turn = None): return self.clone(turn).move(start, end, checkMove)

    def move(self, start, end, checkMove = True):
        if self.won: raise WonGameMove(start, end)

        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0 or start[0] > 8 or start[1] > 8 or end[0] > 8 or end[1] > 8: raise OutOfBoardMove(start, end)

        if checkMove: self.checkMove(start, end)
        s = self.chessboard.get(*start)

        self.chessboard.set(start[0], start[1], ChessBoard.VOID)
        self.chessboard.set(end[0], end[1], s)

        self.checkEatAndWin(start, end)

        self.turn = -self.turn
        return self

    def checkMove(self, start, end): raise NotImplementedError

    def win(self, player):
        self.won = player
        return self

    def eat(self, x, y):
        self.chessboard.set(x, y, ChessBoard.VOID)
        return self

    def checkEatAndWin(self, start, end):
        move = (start, end)

        winner = self.checkWin(move)

        eats = [
            self.checkEat(*end, end[0] - 1, end[1]),
            self.checkEat(*end, end[0] + 1, end[1]),
            self.checkEat(*end, end[0], end[1] - 1),
            self.checkEat(*end, end[0], end[1] + 1)
        ]

        if winner: return self.win(winner)

        return self
    
    def checkWin(self, move):
        end = move[1]
        kingpos = np.where(self.getBoard() == ChessBoard.KING)

        kingEat = self.checkEat(*end, kingpos[0][0], kingpos[1][0], False)
        if kingEat == ChessBoard.KING: return ChessBoard.BLACK_PLAYER
        
        map = self.getBoard()
        filterMap = ChessBoard.MAPARRAY == ChessBoard.EXIT
        boardMap = map[filterMap]
        kingMap = (boardMap == ChessBoard.KING)
        if kingMap.any(): return ChessBoard.WHITE_PLAYER

        wCan = False
        bCan = False
        for e, m, i, j in self.chessboard:
            if wCan and bCan: break
            elif e == 0: continue
            elif e > 0 and not wCan: wCan = self.canMove(i, j)
            elif e < 0 and not bCan: bCan = self.canMove(i, j)

        if not wCan: return ChessBoard.BLACK_PLAYER
        elif not bCan: return ChessBoard.WHITE_PLAYER

        return ChessBoard.NOBODY_PLAYER

    def canMove(self, x, y):
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
        neight = [ eneight[i] or mneight[i] in ChessBoard.WALLS for i in range(4) ]
        return False in neight

    def checkEat(self, mx, my, cx, cy, eat = True):
        if mx < 0 or my < 0 or mx > 8 or my > 8: raise Exception("Checking eat out of board")
        if cx < 0 or cy < 0 or cx > 8 or cy > 8: return ChessBoard.VOID
        
        vCheck = my == cy
        hCheck = mx == cx

        if vCheck and hCheck: return ChessBoard.VOID

        current = self.chessboard.get(cx, cy)
        if current == ChessBoard.VOID: return ChessBoard.VOID

        elSign = np.sign(current)

        eneight = [
            0 if cx < 1 else self.chessboard.get(cx - 1, cy),
            0 if cx > 7 else self.chessboard.get(cx + 1, cy),
            0 if cy < 1 else self.chessboard.get(cx, cy - 1),
            0 if cy > 7 else self.chessboard.get(cx, cy + 1)
        ]
        mneight = [
            0 if cx < 1 else self.chessboard.getMap(cx - 1, cy),
            0 if cx > 7 else self.chessboard.getMap(cx + 1, cy),
            0 if cy < 1 else self.chessboard.getMap(cx, cy - 1),
            0 if cy > 7 else self.chessboard.getMap(cx, cy + 1),
            self.chessboard.getMap(cx, cy)
        ]
        neight = [ (eneight[i] and np.sign(eneight[i]) != elSign) or (mneight[4] != ChessBoard.CAMP and mneight[i] in ChessBoard.WALLS) for i in range(4) ]

        isKing = current == ChessBoard.KING
        vSupp = neight[0] and neight[1]
        hSupp = neight[2] and neight[3]

        vAtk = vSupp and vCheck
        hAtk = hSupp and hCheck

        if not isKing:
            if vAtk or hAtk:
                if eat: self.eat(cx, cy)
                return current
        else:
            isNearCastle = ChessBoard.CASTLE in mneight
            if (isNearCastle and vSupp and hSupp) or (not isNearCastle and (vAtk or hAtk)):
                return current
        
        return ChessBoard.VOID

    def checkRange(self, start, end, x, y):
        if start == end: return True
        j = y if x == -1 else x
        i = start
        d = end - start
        e = np.sign(d)
        for v in range(1, abs(d)):
            a = self.chessboard.get(i + v * e, j)
            b = self.chessboard.get(j, i + v * e)
            if x == -1 and a or  y == -1 and b: return False
        return True

    def checkRangeMap(self, start, end, x, y, sm):
        if start == end: return True
        j = y if x == -1 else x
        i = start
        d = end - start
        e = np.sign(d)
        walls = (ChessBoard.CASTLE, ) if sm == ChessBoard.CAMP else ChessBoard.WALLS
        for v in range(1, abs(d)):
            if (x == -1 and self.chessboard.getMap(i + v * e, j) in walls) or  (y == -1 and self.chessboard.getMap(j, i + v * e) in walls): return False
        return True

    def parseState(self, state):
        pass