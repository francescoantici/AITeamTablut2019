from game.TablutAshtonGame import TablutAshtonGame
from game.Errors import MoveError
from sym.TablutGui import TablutGui


class GameSym:
    PLAYER = ('WHITE', 'BLACK')

    def __init__(self,whitePlayer, blackPlayer, guiEnabled = False, gameRule = None):
        self.__game_type = gameRule or TablutAshtonGame
        self.__gui = None
        self.__verbose = True
        if guiEnabled: self.enableGui()
        self.__players = ( whitePlayer, blackPlayer )
        self.reset()

    def enableGui(self):
        self.__gui = TablutGui()
        return self
    
    def move(self, start, end):
        self.__game.move(start, end)
        return self

    def __play(self):
        turn = self.__game.getTurn()
        player = self.__players[turn]
        if player.human() and self.__gui: return self
        move = None
        try: move = player.play(self.__game.getPawnBoard())
        except Exception as ex:
            player.onError('calculation', ex)
            if self.__verbose: print("ERRORE NEL CALCOLO MOSSA: ", ex)
            return self

        try: self.move(*move)
        except MoveError as ex:
            player.onError('move', ex)
            if self.__verbose: print("MOSSA ERRATA: ", ex, ex.__class__.__name__);
            return self
        except Exception as ex:
            player.onError('execution', ex)
            if self.__verbose: print("ERRORE NELL'ESECUZIONE MOSSA: ", ex);
            return self

        self.__moves.append(move)

        return self

    def __win(self):
        if not self.__won:
            self.__won = True
            winner = self.__game.getWinner()
            
            try:
                self.__players[0].onWin(winner > 0, tuple(self.__moves))
            except Exception as exb:
                if self.__verbose: print("ERRORE NELL'APPRENDIMENTO - BIANCO: ", exb)

            try:
                self.__players[1].onWin(winner < 0, tuple(self.__moves))
            except Exception as exn:
                if self.__verbose: print("ERRORE NELL'APPRENDIMENTO - NERO: ", exn)
            
        return self

    def __draw(self):
        winner = self.__game.getWinner()
        self.__gui.clear()
        self.__gui.drawTable(self.__game.getBoardIterator())
        if winner:
            self.__gui.drawWin(0 if winner == 1 else 1)
            self.__win()
        else:
            self.__gui.drawTurn(self.__game.getTurn())
            if self.__selected: self.__gui.drawSelection(*self.__selected)
        return self

    def __update(self, ticks):
        if self.__gui: self.__draw()
        winner = self.__game.getWinner()
        if not winner: self.__play()
        else: self.__gui.stop()
        return self

    def __click(self, x, y):
        if self.__won: return self
        if self.__selected:
            if self.__selected != (x, y):
                try:
                    move = ((self.__selected[0], self.__selected[1]), (x, y))
                    self.move(*move)
                    self.__moves.append(move)
                except MoveError as ex:
                    if self.__verbose: print(ex, ex.__class__.__name__)
            self.__selected = None
        elif self.__game.getPawn(x, y): self.__selected = (x, y)
        return self

    def reset(self):
        self.__game = self.__game_type()
        self.__selected = None
        self.__moves = []
        self.__won = False
        return self

    def start(self, verbose = True):
        self.__verbose = verbose
        self.reset()
        if self.__gui:
            self.__gui.onUpdate(self.__update)
            self.__gui.onClick(self.__click)
            self.__gui.start()
        else:
            winner = self.__game.getWinner()
            while not winner:
                turn = self.__game.getTurn()
                if self.__verbose: print('TURN {}'.format('WHITE' if turn == 0 else 'BLACK'))
                self.__play()
                winner = self.__game.getWinner()
            print('THE WINNER IS: {}'.format('WHITE' if winner > 0 else 'BLACK'))
            self.__win()

        return self
        



    