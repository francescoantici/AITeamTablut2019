import numpy as np
from game.Pawn import Pawn

class ChessBoard:
    INITIAL = (
        (+0,+0,+0,-1,-1,-1,+0,+0,+0),
        (+0,+0,+0,+0,-1,+0,+0,+0,+0),
        (+0,+0,+0,+0,+1,+0,+0,+0,+0),
        (-1,+0,+0,+0,+1,+0,+0,+0,-1),
        (-1,-1,+1,+1,+2,+1,+1,-1,-1),
        (-1,+0,+0,+0,+1,+0,+0,+0,-1),
        (+0,+0,+0,+0,+1,+0,+0,+0,+0),
        (+0,+0,+0,+0,-1,+0,+0,+0,+0),
        (+0,+0,+0,-1,-1,-1,+0,+0,+0)
    )

    MAP = (
        (0,1,1,2,2,2,1,1,0),
        (1,0,0,0,2,0,0,0,1),
        (1,0,0,0,3,0,0,0,1),
        (2,0,0,0,3,0,0,0,2),
        (2,2,3,3,4,3,3,2,2),
        (2,0,0,0,3,0,0,0,2),
        (1,0,0,0,3,0,0,0,1),
        (1,0,0,0,2,0,0,0,1),
        (0,1,1,2,2,2,1,1,0)
    )
    MAPARRAY = None

    def __init__(self, initial = None):
        self.__board = initial 
        if not self.__board: self.board = np.array(ChessBoard.INITIAL, dtype='byte')
        self.__index = [0, 0]
            

    def get(self, x, y): return self.__board[x, y]
    def set(self, x, y, value): self.__board[x, y] = value; return self
    def getBox(self, start, end): return self.__board[start[0]:start[1], end[0]:end[1]]
    def getMap(self, x, y): return ChessBoard.MAP[x][y]
    
    def getBoard(self):
        board = []
        for i in range(9):
            curr = []
            for j in range(9):
                curr.append(Pawn(i, j, self.__board[i, j], ChessBoard.MAP[i][j]))
            board.append(tuple(curr))
        return tuple(board)

    def copyArray(self): return self.__board.copy()

    def getIteratorList(self):
        iterator = []
        for e,m,i,j in self: iterator.append((e,m,i,j))
        return tuple(iterator)

    def __str__(self):
        res = ''
        for i in range(9):
            for j in range(9):
                res += str(self.__board[i, j]) + '\t'
            res += '\n'
        return res

    def __iter__(self):
        self.__index = [0, 0]
        return self
    def __next__(self):
        i = self.__index[0]
        j = self.__index[1]
        if j == 9: raise StopIteration
        curr = self.__board[i, j]
        currM = ChessBoard.MAP[i][j]
        self.__index[0] += 1
        if self.__index[0] == 9:
            self.__index[0] = 0
            self.__index[1] += 1
        return (curr, currM, i, j)

ChessBoard.MAPARRAY = np.array(ChessBoard.MAP)