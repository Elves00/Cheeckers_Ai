import unittest

from Game import board


class TestBoard(unittest.TestCase):
    def test_board_init(self):
        """
        Test that it can display a board
        """
        x = board.board()
        startboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # self.assertEqual(startboard, x.board)

    def test_board_swap(self):
        print("testing swap_Piece")
        '''
        Test that swap if a piece can move
        '''
        x = board.board()

        swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', 'B', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        x.board = swapboard
        print()
        x.display()
        moveList = []
        # print("Jump one:",x.is_jump_possible(-1,1,1,2,moveList))
        self.assertFalse(x.is_jump_possible(-1, 1, 1, 2, moveList))
        print()
        # print("jump two:",x.is_jump_possible(1,1,3,4,moveList))
        self.assertFalse(x.is_jump_possible(1, 1, 3, 4, moveList))
        print()

        swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        x.board = swapboard
        x.swap_Piece(0, 3, 0, 0)

        # Swap 00 and 03 x->R R->x
        self.assertEqual(x.board[0][0], 'R')
        self.assertEqual(x.board[0][3], 'x')

        x.swap_Piece(0, 0, 5, 4)
        # Swap 00 and 55 R->B B->R
        self.assertEqual(x.board[0][0], 'B')
        self.assertEqual(x.board[5][4], 'R')

    def test_board_is_clear(self):
        print("testing is_clear")
        '''
        Tests if a space is clear
        '''
        x = board.board()

        # "." is clear
        self.assertTrue(x.is_clear(2, 1))
        # "R" is not clear
        self.assertFalse(x.is_clear(0, 3))
        # "x" is not clear
        self.assertFalse(x.is_clear(0, 4))

    def test_board_is_move_valid(self):
        print("testing is_move_valid")
        '''
        Tests if a move is possible given the current board position
        '''
        x = board.board()

        # BASE POSTITION EVALUATIONS

        # piece 0,3 is 'R' and can jump down left from inital position
        self.assertTrue(x.is_move_possible(-1, -1, 0, 3))
        # piece 0,3 cannot jump to the right or left as there is an x there
        self.assertFalse(x.is_move_possible(0, 1, 0, 3))
        self.assertFalse(x.is_move_possible(0, -1, 0, 3))

        # cant move up out of bounds
        self.assertFalse(x.is_move_possible(1, 0, 0, 3))

        # cant move down out of bounds
        self.assertFalse(x.is_move_possible(-1, 0, 6, 3))

        # cant move diagonal into x
        self.assertFalse(x.is_move_possible(1, -1, 1, 2))

        movesUpDown = [0]
        movesRightLeft = [1, 1]
        for i in movesUpDown:
            for j in movesRightLeft:
                self.assertFalse(x.is_move_possible(i, j, 0, 3))
                self.assertFalse(x.is_move_possible(i, j, 0, 3))

        # mid 6 moves possible up left up right down left down right left right
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # cant move up or down or stay still
        # can move every other direction
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        for i in movesUpDown:
            for j in movesRightLeft:
                if ((i == 1 and j == 0) or (i == -1 and j == 0) or (i == 0 and j == 0)):
                    self.assertFalse(x.is_move_possible(i, j, 3, 2))
                else:
                    print("possible? ", i, " ", j)
                    self.assertTrue(x.is_move_possible(i, j, 3, 2))
                    x.is_jump_valid

    def test_is_jump_possible(self):
        print("checking jump is possible")

        x = board.board()

        # mid 6 moves possible up left up right down left down right left right NO JUMPS
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                self.assertFalse(x.is_jump_valid(i, j, 3, 2, moveList))

        # no jumps
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            'R', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                self.assertFalse(x.is_jump_valid(i, j, 3, 0, moveList))

        # NO JUMPS
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                self.assertFalse(x.is_jump_valid(i, j, 2, 1, moveList))

        # NO JUMPS
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                self.assertFalse(x.is_jump_valid(i, j, 2, 1, moveList))

         # NO JUMPS
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                self.assertFalse(x.is_jump_valid(i, j, 3, 2, moveList))

        x.display()
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                # print("is possible? ",i," ",j)
                if (i == -1 and j == -1):
                    self.assertTrue(x.is_jump_valid(i, j, 1, 2, moveList))
                else:
                    self.assertFalse(x.is_jump_valid(i, j, 1, 2, moveList))

        # Jumping over an x
        x.board = swapboard = [['x', 'x', 'x', '.', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'R', ' ', 'R', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', 'B', ' ', '.', ], ['x', 'R', ' ', 'x', ' ', '.', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', '.', 'x', 'x', 'x', ]]
        self.assertFalse(x.is_jump_valid(0, 1, 4, 1, moveList))

        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', 'R', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.assertTrue(x.is_jump_valid(1, -1, 5, 2, moveList))

    def test_board_jump(self):
        print("testing jump")
        x = board.board()
        # Left right jumps empty move list
        x.board = swapboard = [['x', 'x', 'x', '.', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'R', ' ', 'R', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', 'B', ' ', '.', ], ['x', 'R', ' ', 'x', ' ', '.', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', '.', 'x', 'x', 'x', ]]
        print("Start")
        x.display()
        # Moving all to the right
        moveList = []
        x.jump(0, 1, 2, 1, moveList)
        self.assertEqual(x.board[2][5], 'R')
        x.jump(0, 1, 3, 2, moveList)
        self.assertEqual(x.board[3][6], 'R')
        x.jump(0, 1, 4, 1, moveList)
        self.assertEqual(x.board[4][5], 'R')
        print()
        print("mid")
        x.display()
        # Moving all back to the left
        x.jump(0, -1, 2, 5, moveList)
        self.assertEqual(x.board[2][1], 'R')
        x.jump(0, -1, 3, 6, moveList)
        self.assertEqual(x.board[3][2], 'R')
        x.jump(0, -1, 4, 5, moveList)
        self.assertEqual(x.board[4][1], 'R')
        print()
        print("end")
        x.display()

        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', 'R', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        x.display()
        self.assertTrue(x.jump(1, -1, 5, 2, moveList))
        x.display()
        print("problem")

    def test_board_position_value(self):
        x = board.board()
        x.board= swapboard =[['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]


        # player starts as R evaluate as 2
        self.assertEqual(x.position_evaluator(), 2)
        # B starts as 16
        x.swap_Player()
        self.assertEqual(x.position_evaluator(), 16)
        # After swap B is 10
        x.swap_Piece(6, 3, 0, 3)
        self.assertEqual(x.position_evaluator(), 10)
        # after swap R is 8
        x.swap_Player()
        self.assertEqual(x.position_evaluator(), 8)

    def test_board_is_end_zone(self):
        '''
        Checks to see the boards end zones are functioning correctly
        '''
        print("Testing end zone")
        playingBoard = board.board()
        posRow=6
        posCol=3
        #Current player is R so 6,3 is end zone
        self.assertTrue(playingBoard.is_end_zone(posRow,posCol))

        #B end zone is not 6,3
        playingBoard.swap_Player()
        self.assertFalse(playingBoard.is_end_zone(posRow,posCol))
        
        #0,3 is B end zone
        posRow=0
        posCol=3
        self.assertTrue(playingBoard.is_end_zone(posRow,posCol))

        #0,3 end zone is not R
        playingBoard.swap_Player()
        self.assertFalse(playingBoard.is_end_zone(posRow,posCol))





    def test_board_is_jump_valid(self):

        x = board.board()
        moveList = [[0, 2], [1, 2]]
        print(x.is_jump_valid(0, 1, 1, 2, moveList))

        x.board = swapboard = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', 'B', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        x.display()
        print(x.is_jump_valid(-1, 1, 0, 3, [[0, 3]]))

    # def test_board_max(self):

    #     print("CLEAR------------------------------------------")
    #     x = board()
    #     x.display()

    #     (maxv, px, py) = x.max()
    #     print("maxv=", maxv, " px=", px, " py=", py)
    #     x.display()

    #     for i in range(0, 7):
    #         print(i)


if __name__ == '__main__':
    unittest.main()
