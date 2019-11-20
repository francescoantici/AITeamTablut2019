from game.ChessBoard import ChessBoard
from players.alphabeta.AlphaBetaPlayer import AlphaBetaPlayer

class PlayerBlack(AlphaBetaPlayer):
    def __init__(self, depth): super().__init__(False, depth)

    def euristic(self, state, move, depth):
    
        chessboard = state.getPawnBoard()

        kingF = 1
        dangerF = 0
        blockF = 0

        for row in chessboard:
            for pawn in row:
                ##pedina avversaria o cella vuota
                if pawn.empty or pawn.black: continue

                ##pedina bianca
                #vicini pericolosi
                dangerF -= self.danger(chessboard, pawn)

                #re
                if pawn.king:
                    dangerF * 3

                    #vicini che bloccano l'uscita del re dal castello
                    if pawn.castle:
                        blockF -= self.blocked(chessboard, pawn)

                    if (pawn.x >= 3 and pawn.x <= 5) and (pawn.y >= 3 and pawn.y <= 5):
                        kingF = 1
                    elif (pawn.x, pawn.y) in ChessBoard.EXIT_INDICES:
                        kingF = 10
                    else:
                        kingF = 5
                

        distance = kingF * (dangerF + blockF) / depth
        return -distance
    
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