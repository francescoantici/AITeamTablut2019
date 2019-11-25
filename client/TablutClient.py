from client.SocketClient import SocketClient

class TablutClient(SocketClient):

    LETTERS = ('A','B','C','D','E','F','G','H','I')

    def __init__(self, port = 80, host = 'localhost', isWhite = True):
        super().__init__(port, host)
        self.__isWhite = isWhite
        self.__myState = 'WHITE' if self.__isWhite else 'BLACK'
        self.__state = None

    def declarePlayerName(self, player):
        self.send(player)
        return self
    
    def sendAction(self, fromTile, toTile):
        self.send({ "from": fromTile, "to": toTile })
        return self

    def sendMove(self, move):
        return self.sendAction(*self.parseMove(move))

    def parseMove(self, move):
        fromTile = move[0]
        toTile = move[1]
        return TablutClient.LETTERS[fromTile[0]] + str(fromTile[1]+1), TablutClient.LETTERS[toTile[0]] + str(toTile[1]+1)

    def readState(self):
        self.__state = None
        while self.__state is None or self.__state['turn'] != self.__myState:
            self.__state = self.read()
        return self.__state
