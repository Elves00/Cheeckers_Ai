import unittest

from Game import board


class TestBoard(unittest.TestCase):
    def test_board_init(self):
        """
        Test that it can display a board
        """
        x = board()
        startboard=  [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','.',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]

        self.assertEqual(startboard, x.board)
    
    def test_board_swap(self):
        '''
        Test that swap if a piece can move
        '''
        x=board()
        swapboard=  [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','B',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]

        x.board=swapboard
        print()
        x.display()
        moveList=[]
        # print("Jump one:",x.is_jump_possible(-1,1,1,2,moveList))
        self.assertFalse(x.is_jump_possible(-1,1,1,2,moveList))
        print()
        # print("jump two:",x.is_jump_possible(1,1,3,4,moveList))
        self.assertFalse(x.is_jump_possible(1,1,3,4,moveList))
        print()

        swapboard=  [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','.',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]
        x.board=swapboard
        x.swap_Piece(0,3,0,0)
        
        #Swap 00 and 03 x->R R->x
        self.assertEqual(x.board[0][0],'R')
        self.assertEqual(x.board[0][3],'x')

        x.swap_Piece(0,0,5,4)
         #Swap 00 and 55 R->B B->R
        self.assertEqual(x.board[0][0],'B')
        self.assertEqual(x.board[5][4],'R')
        
    def test_board_is_clear(self):
        '''
        Tests if a space is clear
        '''
        x=board()

        #"." is clear
        self.assertTrue(x.is_clear(2,1))
        #"R" is not clear
        self.assertFalse(x.is_clear(0,3))
        #"x" is not clear
        self.assertFalse(x.is_clear(0,4))


    def test_board_is_move_valid(self):
        '''
        Tests if a move is possible given the current board position
        '''
        x=board()

        # piece 0,3 is 'R' and can jump down left from inital position
        self.assertTrue(x.is_move_possible(-1,-1,0,3))
        # piece 0,3 cannot jump to the right or left as there is an x there
        self.assertFalse(x.is_move_possible(0,1,0,3))
        self.assertFalse(x.is_move_possible(0,-1,0,3))

        #cant move up out of bounds
        self.assertFalse(x.is_move_possible(1,0,0,3))

        #cant move down out of bounds
        self.assertFalse(x.is_move_possible(-1,0,6,3))

        #cant move diagonal into x
        self.assertFalse(x.is_move_possible(1,-1,1,2))


    def test_board_position_value(self):
        x=board()
        #player starts as R evaluate as 2
        self.assertEqual(x.position_evaluator(),2)
        #B starts as 16
        x.swap_Player()
        self.assertEqual(x.position_evaluator(),16)
        #After swap B is 10
        x.swap_Piece(6,3,0,3)
        self.assertEqual(x.position_evaluator(),10)
        #after swap R is 8
        x.swap_Player()
        self.assertEqual(x.position_evaluator(),8)



    def test_board_is_jump_valid(self):
        print("Yikes")
        x=board()
        moveList=[[0,2],[1,2]]
        print(x.is_jump_valid(0,1,1,2,moveList))

    def test_board_max(self):
        x = board()
        x.display()
        x.max()
        x.display()

if __name__ == '__main__':
    unittest.main()
