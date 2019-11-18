class MoveError(Exception):
    def __init__(self, start, end): super().__init__("Errore nella mossa: {} -> {}".format(start, end))
class EmptyMove(MoveError): pass
class OccupyMove(MoveError): pass
class WrongPawnMove(MoveError): pass
class DiagonalMove(MoveError): pass
class PassThroughMove(MoveError): pass
class PassThroughBlockMove(MoveError): pass
class WonGameMove(MoveError): pass
class OutOfBoardMove(MoveError): pass
class CastleMove(MoveError): pass
class CitadelMove(MoveError): pass