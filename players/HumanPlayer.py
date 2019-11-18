from players.Player import Player

class HumanPlayer(Player):
    def __init__(self): super().__init__(True)
    def play(self, chessboard):
        return (
            (
                int(input('START x: ')),
                int(input('START y: '))
            ),
            (
                int(input('END x: ')),
                int(input('END y: '))
            )
        )
