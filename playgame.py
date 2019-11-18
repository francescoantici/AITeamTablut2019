from game.TablutAshtonGame import TablutAshtonGame
from game.State import State
from players.RandomPlayer import RandomWhitePlayer, RandomBlackPlayer
from sym.GameSym import GameSym
from ptvsd import enable_attach

#debug vs code
enable_attach(address=('localhost', 5678))


white = RandomWhitePlayer()
black = RandomBlackPlayer()

sym = GameSym(white, black)

sym.enableGui()

x = True
while x:
    sym.start()
    x = input('Giocare ancora? (y/n) ').lower() == 'y'