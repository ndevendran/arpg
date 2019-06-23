import unittest
from piece import Piece
from piece import King

class TestKing(unittest.TestCase):
    def test_king_can_move_one_space_any_direction(self):
        king = King(color='WHITE')
        is_valid_move = king.validate_move((4,2), (3,1))
        self.assertTrue(is_valid_move)
        
        is_valid_move = king.validate_move((4,2), (3,3))
        self.assertTrue(is_valid_move)

        is_valid_move = king.validate_move((4,2), (5,1))
        self.assertTrue(is_valid_move)

    def test_king_can_capture_one_space_any_direction(self):
        king = King(color='WHITE')
        is_valid_capture = king.validate_capture((4,2), (3,1))
        self.assertTrue(is_valid_capture)
        
        is_valid_capture = king.validate_capture((4,2), (3,3))
        self.assertTrue(is_valid_capture)

        is_valid_capture = king.validate_capture((4,2), (5,1))
        self.assertTrue(is_valid_capture)

    def test_king_cant_move_L_shapes(self):
        king = King('WHITE')
        is_valid_move = king.validate_move((1,3),(3,2))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((1,3),(2,5))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((2,3), (1,5))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((2,3), (3,5))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((2,3), (4,4))
        self.assertFalse(is_valid_move)

    

    def test_cant_move_forward_more_than_one_space(self):
        king = King(color='BLACK')
        is_valid_move = king.validate_move((7,2),(4,2))
        self.assertFalse(is_valid_move)

    def test_cant_move_sideways_more_than_one_space(self):
        king = King(color='BLACK')
        is_valid_move = king.validate_move((7,2), (7,4))
        self.assertFalse(is_valid_move)

    def test_cant_move_backward_more_than_one_space(self):
        king = King(color='BLACK')
        is_valid_move = king.validate_move((4,2), (7,2))
        self.assertFalse(is_valid_move)


    def test_cannot_move_diagonally_more_than_one_space(self):
        king = King(color='WHITE')
        is_valid_move = king.validate_move((4,2), (6,4))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((4,2), (1,3))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((4,2), (7,1))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((4,2), (7,3))
        self.assertFalse(is_valid_move)

        is_valid_move = king.validate_move((4,2), (1,1))
        self.assertFalse(is_valid_move)








if __name__ == '__main__':
    unittest.main()