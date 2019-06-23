class Piece():
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def validate_move(oldPos,newPos):
        # Override this method
        pass


class Pawn(Piece):
    first_move = True

    def __init__(self, color):
        self.color = color
        self.type = 'PAWN'

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


class Rook(Piece):

    def __init__(self, color):
        self.color = color
        self.type = 'ROOK'

    def validate_move(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        if (oldColumn != newColumn) and (newRow != oldRow):
            return False

        return True

    def validate_capture(self, oldPos, newPos):
        return self.validate_move(oldPos, newPos)


class Bishop(Piece):

    def __init__(self, color):
        self.color = color
        self.type = 'BISHOP'

    def validate_move(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        row_distance = abs(oldRow - newRow)
        column_distance = abs(oldColumn - newColumn)

        if (oldColumn == newColumn) or (newRow == oldRow):
            return False
        if (row_distance != column_distance):
            return False

        return True

    def validate_capture(self, oldPos, newPos):
        return self.validate_move(oldPos, newPos)

class Queen(Piece):

    def __init__(self,color):
        self.bishop = Bishop(color)
        self.rook = Rook(color)
        self.color = color
        self.type = 'QUEEN'


    def validate_move(self, oldPos, newPos):
        return (self.bishop.validate_move(oldPos, newPos) or self.rook.validate_move(oldPos, newPos))

    def validate_capture(self, oldPos, newPos):
        return (self.bishop.validate_capture(oldPos, newPos) or self.rook.validate_capture(oldPos, newPos))

class Knight(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'KNIGHT'


    def validate_move(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        distanceInRows = abs(oldRow - newRow)
        distanceInCols = abs(oldColumn - newColumn)

        if (distanceInRows == 2 and distanceInCols == 1) or (distanceInRows == 1 and distanceInCols == 2):
            return True

        return False

    def validate_capture(self, oldPos, newPos):
        return self.validate_move(oldPos, newPos)


class King(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'KING'

    def validate_move(self, oldPos, newPos):
        oldRow, oldColumn = oldPos
        newRow, newColumn = newPos

        distanceInRows = abs(oldRow - newRow)
        distanceInCols = abs(oldColumn - newColumn)

        if (distanceInRows > 1 or distanceInCols > 1):
            return False
        
        return True

    def validate_capture(self, oldPos, newPos):
        return self.validate_move(oldPos, newPos)





