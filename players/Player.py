from game.ChessBoard import ChessBoard

class Player:
    def __init__(self, isWhite = False, human = False):
        self.__human = human
        self.__isWhite = isWhite

    def isWhite(self): return self.__isWhite
    def human(self): return self.__human
    def play(self, game, opponent): return self.move(game, game.getPawnBoard(), opponent)
    def move(self, game, chessboard, opponent): raise NotImplementedError
    def onWin(self, winner, moves): print(winner, moves); return self
    def onError(self, type, error): return self
    def turn(self): return ChessBoard.WHITE_PLAYER if self.__isWhite else ChessBoard.BLACK_PLAYER

    def actions(self, game, chessboard = None):
        L=[]
        if not chessboard: chessboard = game.getPawnBoard()
        if self.__isWhite:
            L = self.white_actions(game, chessboard)
        else:
            L = self.black_actions(game, chessboard)
        return L

    def white_actions(self, game, chessboard):
        L=[]
        for i in range(9):
            for j in range(9):
                pawn = chessboard[i][j]
                if pawn.empty:
                    continue  #empty position
                elif pawn.black:
                    continue  #black checker
                else:
                    for k in range(9):
                        #check if the poition is valid by avoiding considering moves into camps, other checkers position and the starting one
                        try:
                            game.checkMove((i,j), (k,j))
                            L.append(((i,j), (k,j)))
                        except: pass
                        try:
                            game.checkMove((i,j), (i,k))
                            L.append(((i,j),(i,k)))
                        except: pass
        return L

    def black_actions(self, game, chessboard):
        L=[]
        for i in range(9):
            for j in range(9):
                pawn = chessboard[i][j]
                if pawn.empty:
                    continue  #empty position
                elif pawn.white:
                    continue  #black checker
                else:
                    for k in range(9):
                        #check if the poition is valid by avoiding considering moves into camps, other checkers position and the starting one
                        try: 
                            game.checkMove((i,j), (k,j))
                            L.append(((i,j), (k,j)))
                        except: pass
                        try:
                            game.checkMove((i,j), (i,k))
                            L.append(((i,j),(i,k)))
                        except: pass
        return L