from game.TablutGame import TablutGame
from game.Errors import *

class TablutAshtonGame(TablutGame):
    def move(self, start, end):
        if self.won: raise WonGameMove(start, end)

        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0 or start[0] > 8 or start[1] > 8 or end[0] > 8 or end[1] > 8: raise OutOfBoardMove(start, end)

        s = self.chessboard.get(*start)
        e = self.chessboard.get(*end)

        sm = self.chessboard.getMap(*start)
        em = self.chessboard.getMap(*end)

        #presa pedina vuota
        if s == 0: raise EmptyMove(start, end)
        #mossa pedina in posto occupato
        elif e != 0: raise OccupyMove(start, end)
        #mossa sul castello
        elif em == 4: raise CastleMove(start, end)
        #mossa su un campo
        elif sm != 2 and em == 2: raise CitadelMove(start, end)
        #mossa pedina avversaria
        elif (self.turn and s > 0) or (not self.turn and s < 0): raise WrongPawnMove(start, end)
        #mossa pedina in diagonale
        elif start[0] != end[0] and start[1] != end[1]: raise DiagonalMove(start, end)
        #mossa attraverso un'altra pedina
        elif (start[0] != end[0] and not self.checkRange(start[0], end[0], -1, start[1])) or (start[1] != end[1] and not self.checkRange(start[1], end[1], start[0], -1)): raise PassThroughMove(start, end)
        #mossa attraverso un castello o un campo
        elif (start[0] != end[0] and not self.checkRangeMap(start[0], end[0], -1, start[1], sm)) or (start[1] != end[1] and not self.checkRangeMap(start[1], end[1], start[0], -1, sm)): raise PassThroughBlockMove(start, end)

        self.chessboard.set(start[0], start[1], 0)
        self.chessboard.set(end[0], end[1], s)

        self.checkEatAndWin(*end)

        self.turn += 1
        self.turn %= 2
        return self