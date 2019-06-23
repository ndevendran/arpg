import unittest
from piece import Piece
from piece import Knight

class TestKnight(unittest.TestCase):
    def test_knight_can_move_L_shapes(self):
        knight = Knight('WHITE')
        is_valid_move = knight.validate_move((1,3),(3,2))
        self.assertTrue(is_valid_move)

        is_valid_move = knight.validate_move((1,3),(2,5))
        self.assertTrue(is_valid_move)

        is_valid_move = knight.validate_move((2,3), (1,5))
        self.assertTrue(is_valid_move)

        is_valid_move = knight.validate_move((2,3), (3,5))
        self.assertTrue(is_valid_move)

        is_valid_move = knight.validate_move((2,3), (4,4))
        self.assertTrue(is_valid_move)

    

    def test_cant_move_forward(self):
        knight = Knight(color='BLACK')
        is_valid_move = knight.validate_move((7,2),(4,2))
        self.assertFalse(is_valid_move)

    def test_cant_move_sideways(self):
        knight = Knight(color='BLACK')
        is_valid_move = knight.validate_move((7,2), (7,4))
        self.assertFalse(is_valid_move)

    def test_cant_move_backward(self):
        knight = Knight(color='BLACK')
        is_valid_move = knight.validate_move((4,2), (7,2))
        self.assertFalse(is_valid_move)


    def test_cannot_move_diagonally(self):
        knight = Knight(color='WHITE')
        is_valid_move = knight.validate_move((4,2), (5,3))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (3,1))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (3,3))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (5,1))
        self.assertFalse(is_valid_move)


        is_valid_move = knight.validate_move((4,2), (1,3))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (7,1))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (7,3))
        self.assertFalse(is_valid_move)

        is_valid_move = knight.validate_move((4,2), (1,1))
        self.assertFalse(is_valid_move)


    def test_knight_can_capture(self):
        knight = Knight('WHITE')
        is_valid_capture = knight.validate_capture((1,3),(3,2))
        self.assertTrue(is_valid_capture)

        is_valid_capture = knight.validate_capture((1,3),(2,5))
        self.assertTrue(is_valid_capture)

        is_valid_capture = knight.validate_capture((2,3), (1,5))
        self.assertTrue(is_valid_capture)

        is_valid_capture = knight.validate_capture((2,3), (3,5))
        self.assertTrue(is_valid_capture)

        is_valid_capture = knight.validate_capture((2,3), (4,4))
        self.assertTrue(is_valid_capture)        








if __name__ == '__main__':
    unittest.main()