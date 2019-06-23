import unittest
import chessboard
from Pieces.piece import Queen, Pawn, Knight, Bishop, Rook

class TestChessBoard(unittest.TestCase):
    def test_can_set_piece_on_board(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')
        pawn = Pawn('WHITE')

        isPieceSet = board.setPiece(queen, (7,4))
        self.assertTrue(isPieceSet)
        
        isPieceSet = board.setPiece(pawn, (7,1))
        self.assertTrue(isPieceSet)


    def test_can_set_and_retrieve_piece(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')

        isPieceSet = board.setPiece(queen, (7,4))

        self.assertTrue(isPieceSet)

        setPiece = board.getPiece((7,4))

        self.assertEqual(queen.color, setPiece.color)


    def test_retrieve_correct_value_when_fails_to_retrieve(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')

        isPieceSet = board.setPiece(queen, (10,10))

        self.assertFalse(isPieceSet)

        setPiece = board.getPiece((10,10))

        self.assertEqual(-1, setPiece)

    def test_validate_move_returns_false_when_off_board(self):
        board = chessboard.ChessBoard()
        queen = Queen('BLACK')

        isPieceSet = board.setPiece(queen, (7,4))

        self.assertTrue(isPieceSet)

        isValidMove = board.validateMove((7,4), (10,10))

        self.assertFalse(isValidMove)

    def test_validate_move_returns_false_when_invalid_piece_move(self):
        board = chessboard.ChessBoard()
        queen = Queen('BLACK')

        isPieceSet = board.setPiece(queen, (7,4))

        self.assertTrue(isPieceSet)

        isValidMove = board.validateMove((7,4), (4,4))

        self.assertTrue(isValidMove)


    def test_invalidate_move_when_same_color_piece_blocking(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')
        pawn = Pawn('WHITE')

        isPieceSet = board.setPiece(queen, (7,4))
        self.assertTrue(isPieceSet)
        isPieceSet = board.setPiece(pawn, (6,4))
        self.assertTrue(isPieceSet)

        isValidMove = board.validateMove((7,4), (4,4))

        self.assertFalse(isValidMove)

    def test_valid_move_when_piece_not_blocking(self):
        board = chessboard.ChessBoard()
        queen = Queen('BLACK')
        pawn = Pawn('WHITE')

        isPieceSet = board.setPiece(queen, (7,4))
        self.assertTrue(isPieceSet)
        isPieceSet = board.setPiece(pawn, (6,3))
        self.assertTrue(isPieceSet)

        isValidMove = board.validateMove((7,4), (4,4))

        self.assertTrue(isValidMove)

    def test_invalid_move_when_different_color_piece_blocking(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')
        knight = Knight('BLACK')

        isPieceSet = board.setPiece(queen, (3,4))
        self.assertTrue(isPieceSet)
        isPieceSet = board.setPiece(knight, (3,2))
        isValidMove = board.validateMove((3,4),(3,1))
        self.assertFalse(isValidMove)

        board = chessboard.ChessBoard()
        bishop = Bishop('BLACK')

        board.setPiece(bishop, (2,5))
        board.setPiece(queen, (3,6))

        isValidMove = board.validateMove((2,5), (4,7))

        self.assertFalse(isValidMove)

    def test_invalid_move_for_diagonal_piece_moving_four_directions_when_blocked(self):
        board = chessboard.ChessBoard()
        queen = Queen('WHITE')
        pawn = Pawn('WHITE')
        knight = Knight('WHITE')
        bishop = Bishop('BLACK')

        board.setPiece(bishop, (3,4))
        board.setPiece(queen, (2,3))
        board.setPiece(pawn, (4,5))
        board.setPiece(knight, (2,5))
        board.setPiece(pawn, (4,3))

        self.assertFalse(board.validateMove((3,4), (1,2)))
        self.assertFalse(board.validateMove((3,4), (5,6)))
        self.assertFalse(board.validateMove((3,4), (1,6)))
        self.assertFalse(board.validateMove((3,4), (5,2)))

    def test_invalid_move_for_rook_in_four_directions_when_blocked(self):
        board = chessboard.ChessBoard()
        rook = Rook('BLACK')
        pawn = Pawn('WHITE')

        board.setPiece(rook, (5,5))
        board.setPiece(pawn, (2,5))
        board.setPiece(pawn, (6,5))
        board.setPiece(pawn, (5,2))
        board.setPiece(pawn, (5,6))

        self.assertFalse(board.validateMove((5,5), (1,5)))
        self.assertFalse(board.validateMove((5,5), (7,5)))
        self.assertFalse(board.validateMove((5,5), (5,1)))
        self.assertFalse(board.validateMove((5,5), (5,7)))

    def test_valid_move_for_rook_in_four_directions_not_blocked(self):
        board = chessboard.ChessBoard()
        rook = Rook('BLACK')

        board.setPiece(rook, (5,5))


        self.assertTrue(board.validateMove((5,5), (1,5)))
        self.assertTrue(board.validateMove((5,5), (7,5)))
        self.assertTrue(board.validateMove((5,5), (5,1)))
        self.assertTrue(board.validateMove((5,5), (5,7)))

    def test_invalid_move_when_same_position(self):
        board = chessboard.ChessBoard()
        rook = Rook('BLACK')

        board.setPiece(rook, (5,5))

        self.assertFalse(board.validateMove((5,5), (5,5)))

    def test_falling_off_edge_is_invalid_move_for_bishop(self):
        board = chessboard.ChessBoard()
        bishop = Bishop('BLACK')

        board.setPiece(bishop, (5,5))

        self.assertFalse(board.validateMove((5,5), (10,10)))
        self.assertFalse(board.validateMove((5,5), (-1,-1)))
        self.assertFalse(board.validateMove((5,5), (0,10)))


    def test_falling_off_edge_is_invalid_move_for_knight(self):
        board = chessboard.ChessBoard()
        knight = Knight('BLACK')

        board.setPiece(knight, (0,6))

        self.assertFalse(board.validateMove((0,6), (1,8)))


    def test_validate_capture_when_no_piece_blocking_for_queen(self):
        board = chessboard.ChessBoard()
        knight = Knight('BLACK')
        queen = Queen('WHITE')

        board.setPiece(queen, (5,5))
        board.setPiece(knight, (7,5))

        self.assertTrue(board.validateCapture((5,5), (7,5)))


    def test_validate_capture_for_pawn(self):
        pass




if __name__ == '__main__':
    unittest.main()


