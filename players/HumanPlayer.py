from players.Player import Player

class HumanPlayer(Player):
    def __init__(self, isWhite = True): super().__init__(isWhite, True)
    def play(self, game, opponent):
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
