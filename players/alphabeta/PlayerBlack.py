from game.ChessBoard import ChessBoard
from players.alphabeta.AlphaBetaPlayer import AlphaBetaPlayer

class PlayerBlack(AlphaBetaPlayer):
    def __init__(self, depth, timer = 50, verbose = False): super().__init__(False, depth, timer, verbose)

    def euristic(self, state, move, depth):
        chessboard = state.getPawnBoard()

        bloccaUscita = 0

        #mangiaPedina = 0

        mangiaRe = 0
        kingF = 0
        dangerF = 0
        blackF = 0
        whiteF = 0
        blockF = 0
        #mangiare re
        #bloccare l'uscita al re - circondare re
        #numero pedine b/n
        #salvare la pedina

        for row in chessboard:
            for pawn in row:
                ##pedina avversaria o cella vuota
                if pawn.empty: continue

                #re
                if pawn.king:
                    kingPawn = pawn
                    #re in pericolo
                    dangerTuple = self.danger(chessboard, pawn)
                    mangiaRe += (dangerTuple[0] ** 5) + (dangerTuple[1] ** 5)

                    #vicini che bloccano l'uscita del re dal castello
                    if pawn.castle:
                        mangiaRe -= 30
                        #mangiaPedina += 5

                    if (pawn.x >= 3 and pawn.x <= 5) and (pawn.y >= 3 and pawn.y <= 5):
                        kingF -= 1
                        mangiaRe *= 2
                    elif (pawn.x, pawn.y) in ChessBoard.EXIT_INDICES:
                        kingF -= 90
                    else:
                        kingF -= 9

                if pawn.white:
                    whiteF -= 1
                    continue
                

                ##pedina nera
                blackF += 1
                pos = (pawn.x, pawn.y)
                if pos in ChessBoard.EXIT_INDICES_MAX: blockF -= 1
                elif pos in ChessBoard.EXIT_INDICES: blockF -= 0.5

                #vicini pericolosi
                dangerTuple = self.danger(chessboard, pawn)
                pawnDangerF = -(dangerTuple[0] + dangerTuple[1])
                
                dangerF += pawnDangerF

        distance = (kingF/(depth*depth) + dangerF/blackF + mangiaRe + whiteF + blackF) / depth
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
        return (l + r, u + d)

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