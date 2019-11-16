from client.TablutClient import TablutClient

class WhiteClient(TablutClient):
    def __init__(self, port = 5800, host = 'localhost'):
        super().__init__(port, host, True)

    def declarePlayerName(self, player = "WPlayer"):
        return super().declarePlayerName(player)