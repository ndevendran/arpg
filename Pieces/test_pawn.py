import unittest
from piece import Piece
from piece import Pawn

class TestPawn(unittest.TestCase):
    def test_cant_move_backward(self):
        pawn = Pawn(color='WHITE')
        is_valid_move = pawn.validate_move((6,1),(7,1))
        self.assertFalse(is_valid_move)


    def test_can_move_forward_one_square(self):
        pawn = Pawn(color='WHITE')
        is_valid_move = pawn.validate_move((6,1), (5,1))
        self.assertTrue(is_valid_move)

    def test_can_move_forward_two_squares_on_first_move(self):
        pawn = Pawn(color='WHITE')
        is_valid_move = pawn.validate_move((7,1),(5,1))
        self.assertTrue(is_valid_move)

    def test_can_capture_diagonally_forward_to_right(self):
        pawn = Pawn(color='WHITE')
        is_valid_capture = pawn.validate_capture((6,1),(5,2))
        self.assertTrue(is_valid_capture)

    def test_cant_validate_capture_as_move(self):
        pawn = Pawn(color='WHITE')
        is_valid_move = pawn.validate_move((6,1),(5,2))
        self.assertFalse(is_valid_move)

    def test_can_capture_diagonally_forward_to_left(self):
        pawn = Pawn(color='WHITE')
        is_valid_capture = pawn.validate_capture((5,2),(4,1))
        self.assertTrue(is_valid_capture)

    def test_bad_moves_forward(self):
        pawn = Pawn(color='WHITE')
        pawn.first_move = False
        is_valid_move = pawn.validate_move((5,2),(3,2))
        self.assertFalse(is_valid_move)

        pawn = Pawn(color='BLACK')
        pawn.first_move = False
        is_valid_move = pawn.validate_move((5,1),(4,1))
        self.assertFalse(is_valid_move)

    def test_bad_captures(self):
        pawn = Pawn(color='WHITE')
        is_valid_capture = pawn.validate_capture((5,1), (5,3))
        self.assertFalse(is_valid_capture)

        pawn = Pawn(color='BLACK')
        is_valid_capture = pawn.validate_capture((4,2), (4,7))
        self.assertFalse(is_valid_capture)





if __name__ == '__main__':
    unittest.main()