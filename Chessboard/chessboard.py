from Pieces.piece import Piece

class ChessBoard():

    def __init__(self):
        self.board = [[None for x in range(0,8)] for y in range(0,8)]


    def noPieceBlocking(self, oldPos, newPos, piece):
        oldRow, oldCol = oldPos
        newRow, newCol = newPos

        if(oldRow == newRow):
            i = oldCol
            while(i != newCol and i>= 0 and i <= len(self.board)):
                if(oldCol > newCol):
                    i = i - 1
                else:
                    i = i + 1
                blockingPiece = self.getPiece((i,oldCol))
                if(blockingPiece is not None and blockingPiece != -1):
                    return False



        if(oldCol == newCol):
            i = oldRow
            while(i != newRow and i >= 0 and i <= len(self.board)):
                if(oldRow > newRow):
                    i = i - 1
                else:
                    i = i + 1
                blockingPiece = self.getPiece((i,oldCol))
                if(blockingPiece is not None and blockingPiece != -1):
                    return False


        
        # Diagonal Conditional
        if(abs(oldRow-newRow) == abs(oldCol-newCol)):
            i = oldRow
            j = oldCol
            while(i != newRow and i>= 0 and i <= len(self.board) and j != newCol and j>= 0 and j <= len(self.board[0])):
                if(oldRow > newRow):
                    i = i - 1
                else:
                    i = i + 1
                if(oldCol > newCol):
                    j = j - 1
                else:
                    j = j + 1

                blockingPiece = self.getPiece((i,j))
                if(blockingPiece is not None and blockingPiece != -1):
                    return False


        # L Conditional
        if(piece.type == 'KNIGHT'):
            return False


        # If we made it here no blocking pieces of same color
        return True
    
    def setPiece(self, piece, pos):
        posRow, posCol = pos

        if(posRow < len(self.board)) and (posCol < len(self.board[0])):
            self.board[posRow][posCol] = piece
            return True
        else:
            return False


    def getPiece(self, pos):
        posRow, posCol = pos
        if(posRow < len(self.board)) and (posCol < len(self.board[0])):
            return self.board[posRow][posCol]
        else:
            return -1

    def validateMove(self, oldPos, newPos):
        oldRow, oldCol = oldPos
        newRow, newCol = newPos

        if(oldRow == newRow and oldCol == newCol):
            return False

        piece = self.getPiece(oldPos)

        if(piece != None and piece != -1):
            if(newRow < len(self.board) and newRow >= 0) and (newCol < len(self.board[0]) and newCol >= 0):
                if(self.noPieceBlocking(oldPos, newPos, piece)):
                    return piece.validate_move(oldPos, newPos)
                else:
                    return False
        else:
            return False

    def validateCapture(self, oldPos, newPos):
        oldRow, oldCol = oldPos
        newRow, newCol = newPos

        movingPiece = self.getPiece(oldPos)
        pieceToBeCaptured = self.getPiece(newPos)

        if(movingPiece != None and movingPiece != -1 and pieceToBeCaptured != None and pieceToBeCaptured != -1):
            if(pieceToBeCaptured.color == movingPiece.color):
                return False
            else:
                if(newRow < len(self.board) and newRow >= 0) and (newCol < len(self.board[0]) and newCol >= 0):
                    posUpTo = (newRow-1, newCol-1)
                    if(self.noPieceBlocking(oldPos, posUpTo, movingPiece)):
                        return movingPiece.validate_move(oldPos, newPos)
                    else:
                        return False
                else:
                    return False
        else:
            return False



