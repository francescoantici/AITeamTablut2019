from game.ChessBoard import ChessBoard
from players.alphabeta.AlphaBetaPlayer import AlphaBetaPlayer
import numpy as np

class PlayerWhite(AlphaBetaPlayer):
    def __init__(self, depth): super().__init__(True, depth)

    def euristic(self, state, move, depth):

        chessboard = state.getPawnBoard()

        kingF = 1
        dangerF = 0
        blackF = 0
        whiteF = 0
        blockF = 0
        castleF = 0

        for row in chessboard:
            for pawn in row:
                ##pedina avversaria o cella vuota
                if pawn.empty or pawn.black:
                    blackF -= 1
                    continue
                
                whiteF += 1

                ##pedina bianca
                #vicini pericolosi
                pawnDangerF = -self.danger(chessboard, pawn)

                #re
                if pawn.king:
                    #re in pericolo
                    pawnDangerF *= 5

                    #vicini che bloccano l'uscita del re dal castello
                    if pawn.castle:
                        blockF -= self.blocked(chessboard, pawn)
                        castleF = -0.3

                    if (pawn.x >= 3 and pawn.x <= 5) and (pawn.y >= 3 and pawn.y <= 5):
                        kingF = 1
                    elif (pawn.x, pawn.y) in ChessBoard.EXIT_INDICES:
                        kingF = 90
                    else:
                        kingF = 9
                
                dangerF += pawnDangerF

        distance = (kingF/(depth*depth) + dangerF + blockF + whiteF + blackF) / depth + castleF * depth
        return distance
    
    def danger(self, chessboard, pawn):
        l = 0
        d = 0
        r = 0
        u = 0
        if pawn.x > 0:
            l = int(chessboard[pawn.x - 1][pawn.y].black or ChessBoard.MAP[pawn.x - 1][pawn.y] in ChessBoard.WALLS)
        if pawn.y > 0:
            u = int(chessboard[pawn.x][pawn.y - 1].black or ChessBoard.MAP[pawn.x][pawn.y - 1] in ChessBoard.WALLS)
        if pawn.x < 8:
            r = int(chessboard[pawn.x + 1][pawn.y].black or ChessBoard.MAP[pawn.x + 1][pawn.y] in ChessBoard.WALLS)
        if pawn.y < 8:
            d = int(chessboard[pawn.x][pawn.y + 1].black or ChessBoard.MAP[pawn.x][pawn.y + 1] in ChessBoard.WALLS)
        return l + d + u + r

    def blocked(self, chessboard, pawn):
        l = 0
        d = 0
        r = 0
        u = 0
        if pawn.x > 0:
            l = int(chessboard[pawn.x - 1][pawn.y].white or ChessBoard.MAP[pawn.x - 1][pawn.y] in ChessBoard.WALLS)
        if pawn.y > 0:
            u = int(chessboard[pawn.x][pawn.y - 1].white or ChessBoard.MAP[pawn.x][pawn.y - 1] in ChessBoard.WALLS)
        if pawn.x < 8:
            r = int(chessboard[pawn.x + 1][pawn.y].white or ChessBoard.MAP[pawn.x + 1][pawn.y] in ChessBoard.WALLS)
        if pawn.y < 8:
            d = int(chessboard[pawn.x][pawn.y + 1].white or ChessBoard.MAP[pawn.x][pawn.y + 1] in ChessBoard.WALLS)
        return l + d + u + r