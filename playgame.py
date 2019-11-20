from game.TablutAshtonGame import TablutAshtonGame
from game.State import State
from players.RandomPlayer import RandomWhitePlayer, RandomBlackPlayer
from players.alphabeta.PlayerWhite import PlayerWhite
from players.alphabeta.PlayerBlack import PlayerBlack
from players.HumanPlayer import HumanPlayer
from sym.GameSym import GameSym
from ptvsd import enable_attach, wait_for_attach


# debug vs code
enable_attach(address=('localhost', 5678))
# attendi debugger


white = PlayerWhite(2)
black = HumanPlayer(False)

sym = GameSym(white, black)

sym.enableGui()

x = True
while x:
    sym.start()
    x = input('Giocare ancora? (y/n) ').lower() == 'y'