from client.TablutClient import TablutClient

class BlackClient(TablutClient):
    
    DEFAULT_PORT = 5801

    def __init__(self, port = 5801, host = 'localhost'):
        if port is None: port = BlackClient.DEFAULT_PORT
        super().__init__(port, host, False)

    def declarePlayerName(self, player = "BPlayer"):
        return super().declarePlayerName(player)