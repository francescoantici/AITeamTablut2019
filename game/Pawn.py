class Pawn:
    def __init__(self, x, y, pawn, map):
        self.value = pawn
        self.map = map
        self.x = x
        self.y = y

        self.white = self.value > 0
        self.black = self.value < 0
        self.king = self.value == 2

        self.empty = self.value == 0
        self.occupied = not self.empty


        self.camp = self.map == 2
        self.castle = self.map == 4
        self.escape = self.map == 1
        self.block = self.camp or self.king