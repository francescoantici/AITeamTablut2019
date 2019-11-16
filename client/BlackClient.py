from client.TablutClient import TablutClient

class BlackClient(TablutClient):
    def __init__(self, port = 5801, host = 'localhost'):
        super().__init__(port, host, False)

    def declarePlayerName(self, player = "BPlayer"):
        return super().declarePlayerName(player)