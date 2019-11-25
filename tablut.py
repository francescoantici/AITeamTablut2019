from game.TablutAshtonGame import TablutAshtonGame
from client.WhiteClient import WhiteClient
from client.BlackClient import BlackClient
from game.TablutAshtonGame import TablutAshtonGame
from sym.TablutGui import TablutGui

from players.RandomPlayer import RandomWhitePlayer, RandomBlackPlayer
from players.alphabeta.PlayerWhite import PlayerWhite
from players.alphabeta.PlayerBlack import PlayerBlack
from players.HumanPlayer import HumanPlayer

from time import time
import socket
import sys

print('=======================')
print('=======================')
print('===== TABLUT 2019 =====')
print('=======================')
print('=======================')

### ===== IMPOSTAZIONI ====== ###
TEAM_NAME = 'TEAM_NAME'
WHITE_CLASS = PlayerWhite
BLACK_CLASS = PlayerBlack
DEPTH = 2
print("\nPARAMETERS:\n\tTEAM: {}\n\tWHITE: {}\n\tBLACK: {}\n\tDEPTH: {}".format(TEAM_NAME, WHITE_CLASS.__name__, BLACK_CLASS.__name__, DEPTH))

### ===== INIZIALIZZAZIONE PROGRAMMA ===== ###
argv = sys.argv[1:]
argvl = len(argv)
isWhite = argv[0].lower() == 'white' if argvl > 0 else True
timeout = int(argv[1]) if argvl > 1 else 60
server = (argv[2] if argvl > 2 else 'localhost').split(':')
serverl = len(server)
serverHost = server[0] if serverl > 0 else 'localhost'
serverPort = server[1] if serverl > 1 else None

CLIENT_CLASS = WhiteClient if isWhite else BlackClient
client = CLIENT_CLASS(serverPort, serverHost)
white = WHITE_CLASS(DEPTH, timeout - 10, False)
black = BLACK_CLASS(DEPTH, timeout - 10, False)
player = white if isWhite else black
opponent = black if isWhite else white
game = TablutAshtonGame()

print("\tROLE: {}\n\tTIMEOUT: {}\n\tHOST: {}\n\tPORT: {}".format('White' if isWhite else 'Black', timeout, serverHost, serverPort if serverPort else 'DEFAULT'))

### ===== CONNESSIONE AL SERVER ====== ###
connected = False
while not connected:
    try:
        print("\n*** TRYING TO CONNECT TO SERVER ***")
        client.connect()
        connected = True
    except Exception as ex:
        print('### ERROR: {} ###'.format(ex))
        connected = False

print("*** CONNECTED ***")
client.declarePlayerName(TEAM_NAME)
print("*** SENDING PLAYER NAME: {} ***\n".format(TEAM_NAME))

### ====== CICLO DI GIOCO ====== ###
while True:
    try:
        print('*** READING STATE ***')
        state = client.readState()
        print('# PARSING STATE #')
        game.parseState(state)
        print('# COMPUTING MOVE #')
        start = time()
        move = player.play(game, opponent)
        print('# COMPUTED IN {} s #'.format(start - time()))
        print('*** SENDING MOVE: {} - {} ***'.format(move, client.parseMove(move)))
        client.sendMove(move)
    except socket.error as ex:
        print("#### ERROR: {} ###".format(ex))
        break
    except Exception as ex:
        print("#### ERROR: {} ###".format(ex))
        continue