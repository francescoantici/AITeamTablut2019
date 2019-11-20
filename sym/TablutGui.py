import tkinter
from PIL import Image, ImageTk
from game.ChessBoard import ChessBoard

class TablutGui:
    RESOURCES_STRING = {
        'black': 'black3.png',
        'camp': 'camp.png',
        'castle': 'castle.png',
        'cell': 'cell.png',
        'escape': 'escape.png',
        'startCell': 'startcell.png',
        'white': 'White1.png',
        'king': 'king.png',
        'selection': 'selection.png'
    }
    RESOURCE_PAWN = { ChessBoard.BLACK_PAWN: 'black', ChessBoard.WHITE_PAWN: 'white', ChessBoard.KING: 'king' }
    RESOURCE_MAP = { ChessBoard.VOID: 'cell', ChessBoard.EXIT: 'escape', ChessBoard.CAMP: 'camp', ChessBoard.START_WHITE: 'startCell', ChessBoard.CASTLE: 'castle' }

    def __init__(self):
        self.__callbacks = {}
        self.__ticks = 0
        self.__playing = False
        self.__root = tkinter.Tk()
        self.__images = { k: self.__openImage('./resources/' + v) for k,v in TablutGui.RESOURCES_STRING.items() }
        self.__turnsImages = (
            self.__openImage('./resources/' + TablutGui.RESOURCES_STRING['white'], 15),
            self.__openImage('./resources/' + TablutGui.RESOURCES_STRING['black'], 15)
        )
        self.__winImages = (
            self.__openImage('./resources/' + TablutGui.RESOURCES_STRING['castle'], 15),
            self.__openImage('./resources/' + TablutGui.RESOURCES_STRING['camp'], 15)
        )
        self.__canvas = tkinter.Canvas(self.__root, width=500, height=500, bg='black')
        self.__canvas.bind("<Button-1>", self.__onclick)
        self.__canvas.pack()

    def __openImage(self, path, size = 46):
        pilImg = Image.open(path).resize((size, size), Image.ANTIALIAS)
        return ImageTk.PhotoImage(pilImg)
    
    def __getImagePawn(self, value):
        return self.__images[TablutGui.RESOURCE_PAWN[value]]
    
    def __getImageMap(self, value):
        return self.__images[TablutGui.RESOURCE_MAP[value]]

    def __onclick(self, evt):
        x = int((evt.x - 25) / 50)
        y = int((evt.y - 25) / 50)
        self.__call('click', x, y)
        return self
    
    def __call(self, type, *args):
        type = type.lower().strip()
        if type in self.__callbacks: self.__callbacks[type](*args)
        return self

    def drawTable(self, chessboard):
        for i in range(9):
            ci = i * 50 + 50
            self.__canvas.create_text(ci, 12, text = str(i), font="Times 20", fill='white')
            self.__canvas.create_text(12, ci, text = str(i), font="Times 20", fill='white')
        for e, m, i, j in chessboard:
            ci = i * 50 + 50
            cj = j * 50 + 50
            self.__canvas.create_image(ci, cj, image = self.__getImageMap(m))
            if e != ChessBoard.VOID: self.__canvas.create_image(ci, cj, image = self.__getImagePawn(e))
        return self

    def drawTurn(self, turn):
        self.__canvas.create_image(490, 490, image = self.__turnsImages[turn])
        return self

    def drawWin(self, winner):
        self.__canvas.create_image(490, 490, image = self.__winImages[ChessBoard.PLAYERS_INDICES[winner]])
        return self

    def drawSelection(self, x, y):
        self.__canvas.create_image(x * 50 +50, y * 50 + 50, image = self.__images['selection'])

    def clear(self):
        self.__canvas.delete('all')
        return self

    def update(self):
        self.__root.update_idletasks()
        self.__root.update()
        self.__call('update', self.__ticks)
        self.__ticks += 1
        return self
    
    def start(self):
        self.__playing = True
        while self.__playing: self.update()
        return self

    def on(self, type, callback):
        type = type.lower().strip()
        self.__callbacks[type] = callback
        return self

    def stop(self):
        self.__playing = False
        return self

    def onClick(self, callback): return self.on('click', callback)
    def onUpdate(self, callback): return self.on('update', callback)