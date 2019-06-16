class Piece():
    def validate_move(oldPos,newPos):
        # Override this method
        pass


class Pawn(Piece):
    first_move = True

    def __init__(self, color):
        self.color = color

    def validate_move(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        if oldColumn != newColumn:
            return False
        if ((newRow - oldRow) > 0 and self.color=='WHITE'):
            return False
        if ((newRow - oldRow) < 0 and self.color=='BLACK'):
            return False

        if(abs(newRow-oldRow) > 2):
            return False
        if(abs(newRow-oldRow) == 2 and not self.first_move):
            return False

        return True

    def validate_capture(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        if abs(oldColumn-newColumn) > 1:
            return False

        return True



