from game.TablutAshtonGame import TablutAshtonGame
from players.RandomPlayer import RandomWhitePlayer, RandomBlackPlayer
from players.alphabeta.PlayerWhite import PlayerWhite
from players.alphabeta.PlayerBlack import PlayerBlack
from players.HumanPlayer import HumanPlayer
from sym.GameSym import GameSym
from ptvsd import enable_attach, wait_for_attach

enable_attach(address=('localhost', 5678)) # debug vs code
# print("Aspettando il debugger"); wait_for_attach() # attendi debugger

white = RandomWhitePlayer()
# white = PlayerWhite(2, 40)
# black = HumanPlayer(False)
# white = HumanPlayer(True)
black = PlayerBlack(2, 40)

sym = GameSym(white, black)

sym.enableGui()

x = True
while x:
    sym.start()
    x = input('Giocare ancora? (y/n) ').lower() == 'y'