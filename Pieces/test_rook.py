import unittest
from piece import Piece
from piece import Rook

class TestRook(unittest.TestCase):
    def test_can_move_forward(self):
        rook = Rook(color='BLACK')
        is_valid_move = rook.validate_move((7,2),(4,2))
        self.assertTrue(is_valid_move)

    def test_can_move_sideways(self):
        rook = Rook(color='BLACK')
        is_valid_move = rook.validate_move((7,2), (7,4))
        self.assertTrue(is_valid_move)

    def test_can_move_backward(self):
        rook = Rook(color='BLACK')
        is_valid_move = rook.validate_move((4,2), (7,2))
        self.assertTrue(is_valid_move)

    def test_cannot_move_diagonally(self):
        rook = Rook(color='WHITE')
        is_valid_capture = rook.validate_move((4,2), (5,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (3,1))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (3,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (5,1))
        self.assertFalse(is_valid_capture)


        is_valid_capture = rook.validate_move((4,2), (1,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (7,1))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (7,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_move((4,2), (1,1))
        self.assertFalse(is_valid_capture)


    def test_can_capture_forward(self):
        rook = Rook(color='WHITE')
        is_valid_capture = rook.validate_move((7,2), (4,2))
        self.assertTrue(is_valid_capture)

    def test_can_capture_sideways(self):
        rook = Rook(color='BLACK')
        is_valid_capture = rook.validate_capture((7,2), (7,4))
        self.assertTrue(is_valid_capture)

    def test_can_capture_backward(self):
        rook = Rook(color='WHITE')
        is_valid_capture = rook.validate_capture((4,2), (7,2))
        self.assertTrue(is_valid_capture)

    def test_cant_capture_diagonally(self):
        rook = Rook(color='WHITE')
        is_valid_capture = rook.validate_capture((4,2), (5,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (3,1))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (3,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (5,1))
        self.assertFalse(is_valid_capture)


        is_valid_capture = rook.validate_capture((4,2), (3,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (3,1))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (5,3))
        self.assertFalse(is_valid_capture)

        is_valid_capture = rook.validate_capture((4,2), (3,1))
        self.assertFalse(is_valid_capture)


    def test_rook_cant_move_L_shapes(self):
        rook = Rook('WHITE')
        is_valid_move = rook.validate_move((1,3),(3,2))
        self.assertFalse(is_valid_move)

        is_valid_move = rook.validate_move((1,3),(2,5))
        self.assertFalse(is_valid_move)

        is_valid_move = rook.validate_move((2,3), (1,5))
        self.assertFalse(is_valid_move)

        is_valid_move = rook.validate_move((2,3), (3,5))
        self.assertFalse(is_valid_move)

        is_valid_move = rook.validate_move((2,3), (4,4))
        self.assertFalse(is_valid_move)








if __name__ == '__main__':
    unittest.main()