from client.SocketClient import SocketClient
import numpy as np
from game.ChessBoard import ChessBoard



#C=SocketClient()
#C.read()


def ChessBoardParsing(D):
    Parser={"WHITE":ChessBoard.WHITE_PAWN,"BLACK":ChessBoard.BLACK_PAWN,"EMPTY":ChessBoard.VOID,"KING":ChessBoard.KING}
    chessboard=np.zeros((9,9))
    L=D["board"]
    for i in range(len(L)):
        row=L[i]
        chessboard[i,:]=[Parser[j] for j in row]
    return chessboard



L={"board":[["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"],
            ["WHITE","BLACK","EMPTY","KING","WHITE","BLACK","EMPTY","KING","EMPTY"]]}

g=ChessBoardParsing(L)
print(g)