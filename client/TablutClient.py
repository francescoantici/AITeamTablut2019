from client.SocketClient import SocketClient

class TablutClient(SocketClient):
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

    def readState(self):
        while self.__state is None or self.__state['turn'] != self.__myState:
            self.__state = self.read()
        return self.__state