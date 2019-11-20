from game.ChessBoard import ChessBoard
from game.TablutGame import TablutGame
from game.Errors import *
import numpy as np

class TablutAshtonGame(TablutGame):
    def checkMove(self, start, end):
        s = self.chessboard.get(*start)
        e = self.chessboard.get(*end)

        sm = self.chessboard.getMap(*start)
        em = self.chessboard.getMap(*end)

        #presa pedina vuota
        if s == ChessBoard.VOID: raise EmptyMove(start, end)
        #mossa pedina in posto occupato
        elif e != ChessBoard.VOID: raise OccupyMove(start, end)
        #mossa sul castello
        elif em == ChessBoard.CASTLE: raise CastleMove(start, end)
        #mossa su un campo
        elif sm != ChessBoard.CAMP and em == ChessBoard.CAMP: raise CitadelMove(start, end)
        #mossa pedina avversaria
        elif np.sign(self.turn) != np.sign(s): raise WrongPawnMove(start, end)
        #mossa pedina in diagonale
        elif start[0] != end[0] and start[1] != end[1]: raise DiagonalMove(start, end)
        #mossa attraverso un'altra pedina
        elif (start[0] != end[0] and not self.checkRange(start[0], end[0], -1, start[1])) or (start[1] != end[1] and not self.checkRange(start[1], end[1], start[0], -1)): raise PassThroughMove(start, end)
        #mossa attraverso un castello o un campo
        elif (start[0] != end[0] and not self.checkRangeMap(start[0], end[0], -1, start[1], sm)) or (start[1] != end[1] and not self.checkRangeMap(start[1], end[1], start[0], -1, sm)): raise PassThroughBlockMove(start, end)
        
        return self