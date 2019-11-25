from client.TablutClient import TablutClient

class WhiteClient(TablutClient):

    DEFAULT_PORT = 5800

    def __init__(self, port = 5800, host = 'localhost'):
        if port is None: port = WhiteClient.DEFAULT_PORT
        super().__init__(port, host, True)

    def declarePlayerName(self, player = "WPlayer"):
        return super().declarePlayerName(player)