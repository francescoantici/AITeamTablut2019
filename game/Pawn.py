class Pawn:
    def __init__(self, x, y, pawn, map):
        self.value = pawn
        self.map = map
        self.x = x
        self.y = y

        self.white = self.value > 0
        self.black = not self.white
        self.king = self.value == 2

        self.camp = self.map == 2
        self.king = self.map == 4
        self.block = self.camp or self.king