import unittest
from piece import Piece
from piece import Queen

class TestQueen(unittest.TestCase):
    def test_can_move_diagonally(self):
        bishop = Queen(color='BLACK')
        is_valid_move = bishop.validate_move((4,2), (5,3))
        self.assertTrue(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (3,1))
        self.assertTrue(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (3,3))
        self.assertTrue(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (5,1))
        self.assertTrue(is_valid_move)


        is_valid_move = bishop.validate_move((4,2), (3,1))
        self.assertTrue(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (7,1))
        self.assertFalse(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (7,5))
        self.assertTrue(is_valid_move)

        is_valid_move = bishop.validate_move((4,2), (5,1))
        self.assertTrue(is_valid_move)

    def test_can_capture_diagonally(self):
        bishop = Queen(color='WHITE')
        is_valid_capture = bishop.validate_capture((4,2), (5,3))
        self.assertTrue(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (3,1))
        self.assertTrue(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (3,3))
        self.assertTrue(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (5,1))
        self.assertTrue(is_valid_capture)


        is_valid_capture = bishop.validate_capture((4,2), (3,1))
        self.assertTrue(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (7,1))
        self.assertFalse(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (3,3))
        self.assertTrue(is_valid_capture)

        is_valid_capture = bishop.validate_capture((4,2), (5,1))
        self.assertTrue(is_valid_capture)

    def test_can_move_forward(self):
        rook = Queen(color='BLACK')
        is_valid_move = rook.validate_move((7,2),(4,2))
        self.assertTrue(is_valid_move)

    def test_can_move_sideways(self):
        rook = Queen(color='BLACK')
        is_valid_move = rook.validate_move((7,2), (7,4))
        self.assertTrue(is_valid_move)

    def test_can_move_backward(self):
        rook = Queen(color='BLACK')
        is_valid_move = rook.validate_move((4,2), (7,2))
        self.assertTrue(is_valid_move)

    def test_can_capture_forward(self):
        rook = Queen(color='WHITE')
        is_valid_capture = rook.validate_capture((7,2), (4,2))
        self.assertTrue(is_valid_capture)

    def test_can_capture_sideways(self):
        rook = Queen(color='BLACK')
        is_valid_capture = rook.validate_capture((7,2), (7,4))
        self.assertTrue(is_valid_capture)

    def test_can_capture_backward(self):
        rook = Queen(color='WHITE')
        is_valid_capture = rook.validate_capture((4,2), (7,2))
        self.assertTrue(is_valid_capture)


    def test_queen_cant_move_L_shapes(self):
        queen = Queen('WHITE')
        is_valid_move = queen.validate_move((1,3),(3,2))
        self.assertFalse(is_valid_move)

        is_valid_move = queen.validate_move((1,3),(2,5))
        self.assertFalse(is_valid_move)

        is_valid_move = queen.validate_move((2,3), (1,5))
        self.assertFalse(is_valid_move)

        is_valid_move = queen.validate_move((2,3), (3,5))
        self.assertFalse(is_valid_move)

        is_valid_move = queen.validate_move((2,3), (4,4))
        self.assertFalse(is_valid_move)








if __name__ == '__main__':
    unittest.main()