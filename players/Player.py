from game.State import State

class Player:
    def __init__(self, isWhite = False, human = False):
        self.__human = human
        self.__isWhite = isWhite

    def isWhite(self): return self.__isWhite
    def human(self): return self.__human
    def play(self, game): return self.move(game, game.getPawnBoard())
    def move(self, game, chessboard): raise NotImplementedError

    def onWin(self, winner, moves): print(winner, moves); return self
    def onError(self, type, error): return self

    def actions(self, game, chessboard):
        L=[]
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
                        if game.checkMove((i,j), (k,j)): 
                            L.append(((i,j), (k,j)))
                        if game.checkMove((i,j), (i,k)):
                            L.append(((i,j),(i,k)))
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
                        if game.checkMove((i,j), (k,j)): 
                            L.append(((i,j), (k,j)))
                        if game.checkMove((i,j), (i,k)):
                            L.append(((i,j),(i,k)))
        return L