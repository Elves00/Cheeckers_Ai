import unittest

from Game import board
from Game import evaluation

class TestBoard(unittest.TestCase):

    def test_board_mode(self):
        x = board.board()
        starting = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        self.assertEqual(starting, x.board)

        # Swaping the board
        swap = "full"
        x.swap_board(swap)

        starting = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', ' ', 'G'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        self.assertEqual(starting, x.board)

    
    
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
        print("testing is_move_possible")
        '''
        Tests if a move is possible given the current board position
        '''
        x = board.board()

        # BASE POSTITION EVALUATIONS

        # piece 0,3 is 'R' and can jump down left from inital position
        self.assertTrue(x.is_move_valid(-1, -1, 0, 3))
        # piece 0,3 cannot jump to the right or left as there is an x there
        self.assertFalse(x.is_move_valid(0, 1, 0, 3))
        self.assertFalse(x.is_move_valid(0, -1, 0, 3))

        # cant move up out of bounds
        self.assertFalse(x.is_move_valid(1, 0, 0, 3))

        # cant move down out of bounds
        self.assertFalse(x.is_move_valid(-1, 0, 6, 3))

        # cant move diagonal into x
        self.assertFalse(x.is_move_valid(1, -1, 1, 2))

        movesUpDown = [0]
        movesRightLeft = [1, 1]
        for i in movesUpDown:
            for j in movesRightLeft:
                self.assertFalse(x.is_move_valid(i, j, 0, 3))
                self.assertFalse(x.is_move_valid(i, j, 0, 3))

        # mid 6 moves possible up left up right down left down right left right
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # cant move up or down or stay still
        # can move every other direction
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        for i in movesUpDown:
            for j in movesRightLeft:
                if ((i == 1 and j == 0) or (i == -1 and j == 0) or (i == 0 and j == 0)):
                    self.assertFalse(x.is_move_valid(i, j, 3, 2))
                else:
                    self.assertTrue(x.is_move_valid(i, j, 3, 2))
                    x.is_jump_valid

        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', '.', ' ', 'R', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.assertTrue(x.is_move_valid(-1, -1, 4, 3))

    def test_is_jump_possible(self):
        print("checking jump is possible")

        x = board.board()

        # mid 6 moves possible up left up right down left down right left right NO JUMPS
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                self.assertFalse(x.is_jump_valid(i, j, 3, 2, moveList))

        # no jumps
        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            'R', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                self.assertFalse(x.is_jump_valid(i, j, 3, 0, moveList))

        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', 'R', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # no jumps possible
        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
                self.assertFalse(x.is_jump_valid(i, j, 3, 2, moveList))

        movesUpDown = [1, 0, -1]
        movesRightLeft = [1, 0, -1]
        moveList = []
        for i in movesUpDown:
            for j in movesRightLeft:
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
        # Moving all to the right
        moveList = []
        x.jump(0, 1, 2, 1, moveList)
        self.assertEqual(x.board[2][5], 'R')
        x.jump(0, 1, 3, 2, moveList)
        self.assertEqual(x.board[3][6], 'R')
        x.jump(0, 1, 4, 1, moveList)
        self.assertEqual(x.board[4][5], 'R')

        # Moving all back to the left
        x.jump(0, -1, 2, 5, moveList)
        self.assertEqual(x.board[2][1], 'R')
        x.jump(0, -1, 3, 6, moveList)
        self.assertEqual(x.board[3][2], 'R')
        x.jump(0, -1, 4, 5, moveList)
        self.assertEqual(x.board[4][1], 'R')


        x.board = swapboard = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', 'R', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.assertTrue(x.jump(1, -1, 5, 2, moveList))

    
    def test_board_is_end_or_start_zone(self):
        '''
        Checks to see the boards end zones are functioning correctly
        '''
        print("Testing end zone")
        playingBoard = board.board()
        posRow = 6
        posCol = 3
        # Current player is R so 6,3 is end zone
        self.assertTrue(playingBoard.is_end_or_start_zone(posRow, posCol))

        # B end zone 6,3
        playingBoard.next_Player()
        self.assertTrue(playingBoard.is_end_or_start_zone(posRow, posCol))

        # 0,3 is B end zone
        posRow = 0
        posCol = 3
        self.assertTrue(playingBoard.is_end_or_start_zone(posRow, posCol))

        # 0,3 end zone  R
        playingBoard.next_Player()
        self.assertTrue(playingBoard.is_end_or_start_zone(posRow, posCol))

        playingBoard.swap_board("full")
        playingBoard.display()

        rows = [[0], [1], [0, 2], [1, 3]]
        for i in range(0, 4):
            for j in rows[i]:
                if(playingBoard.board[i+13][12-i] != "x" and playingBoard.board[i+13][12-i] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i+13,12-j))
                elif(playingBoard.board[i+13][12+i] != "x" and playingBoard.board[i+13][12+i] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i+13,12+j))
     

        for i in range(0, 4):
            for j in rows[i]:
                if(playingBoard.board[i+9][3-j] != "x" and playingBoard.board[i+9][3-j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i+9,3-j))
                elif(playingBoard.board[i+9][3+j] != "x" and playingBoard.board[i+9][3+j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i+9,3+j))
        

        for i in range(0, 4):
            for j in rows[i]:
                if(playingBoard.board[7-i][3-j] != "x" and playingBoard.board[7-i][3-j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(7-i,3-j))
                elif(playingBoard.board[7-i][3+j] != "x" and playingBoard.board[7-i][3+j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(7-i,3+j))

        for i in range(0, 4):
            for j in rows[i]:
                if(playingBoard.board[i][12-j] != "x" and playingBoard.board[i][12-j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i,12-j))
                elif(playingBoard.board[i][12+j] != "x" and playingBoard.board[i][12+j] !=' '):
                    self.assertTrue(playingBoard.is_end_or_start_zone(i,12+j))


        #Green Start Zone / Orange End Zone
        for i in range(0, 4):
            for j in rows[i]:
                self.assertTrue(playingBoard.is_end_or_start_zone(7-i,21-j))
                self.assertTrue(playingBoard.is_end_or_start_zone(7-i,21+j))

        # Yellow 
        for i in range(0, 4):
            for j in rows[i]:
                self.assertTrue(playingBoard.is_end_or_start_zone(9+i,21-j))
                self.assertTrue(playingBoard.is_end_or_start_zone(9+i,21+j))

        endZones=0
        for i in range(0, playingBoard.boardHeight):
            for j in range(0, playingBoard.boardWidth):
                if(playingBoard.board[i][j]!='x' and playingBoard.board[i][j]!=' '):
                    if(playingBoard.is_end_or_start_zone(i,j)):
                        endZones+=1
                        print(i,j,playingBoard.board[i][j])
                        
        print("end zones total:",endZones)
   

    def test_board_is_jump_valid(self):
        '''Tests the is jump valid method of '''

        x = board.board()
        moveList = [[0, 2], [1, 2]]
        # B can't jump as it's reds turn
        self.assertFalse(x.is_jump_valid(0, 1, 1, 2, moveList))
        # can't jump as it's out of bounds
        x.next_Player()
        self.assertFalse(x.is_jump_valid(0, 1, 1, 2, moveList))
        x.board = swapboard = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', 'B', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        self.assertTrue(x.is_jump_valid(-1, 1, 0, 3, [[0, 3]]))

        x.board = swapboard = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', 'B', 'x', 'x', ], ['x', '.', ' ', '.', ' ', 'R', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        x.next_Player()
        # Able to jump into end zone
        self.assertTrue(x.is_jump_valid(1, -1, 2, 5, [[2, 5]]))

        x.board = swapboard = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', 'B', 'x', 'x', ], ['x', '.', ' ', '.', ' ', 'R', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', 'B', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        # B's move
        x.next_Player()
        # Can't swap with own piece in end zone
        self.assertFalse(x.is_jump_valid(-1, -1, 4, 5, [[4, 5]]))

        x.board = swapboard = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', 'B', 'x', 'x', ], ['x', '.', ' ', '.', ' ', 'R', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', 'R', ' ', '.', ' ', 'B', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.assertFalse(x.is_jump_valid(1, -1, 6, 3, [[6, 3]]))

    def test_is_end(self):
        '''Checks the end conditions in boards is_end method'''
        x=board.board()
        starting = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
        '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'R', 'x', 'x', 'x', ]]
        x.board=starting
        self.assertEqual(1,x.is_end())

        starting = [['x', 'x', 'x', 'B', 'x', 'x', 'x', ], ['x', 'x', 'B', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
        '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        x.board=starting
        self.assertEqual(4,x.is_end())

        starting = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'O', ' ', 'O', ' ', 'O', ' ', 'O'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'O', ' ', 'O', ' ', 'O', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'O', ' ', 'O', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'O', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        x.swap_board("full")

        x.board=starting

        self.assertEqual(5,x.is_end())

        starting = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', ' ', 'G'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'G', ' ', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['G', ' ', 'G', ' ', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        x.board=starting
        self.assertEqual(2,x.is_end())


        starting = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', ' ', 'G'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'O', ' ', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['G', ' ', 'O', ' ', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        x.board=starting
        self.assertNotEqual(2,x.is_end())


        starting = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', ' ', 'G'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'G', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'O', ' ', 'O', ' ', 'G', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['G', ' ', 'O', ' ', 'G', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        x.board=starting
        self.assertNotEqual(2,x.is_end())

    def test_swap_player(self):
        x=board.board()
        self.assertEqual('R',x.player)
        self.assertEqual(['R','B'],x.playerList)

        x.next_Player()
        self.assertEqual('B',x.player)
        
        x.next_Player()
        self.assertEqual('R',x.player)
        
        x.next_Player()
        self.assertEqual('B',x.player)

        #Checking swap for full board
        x.swap_board("full")
        self.assertEqual('R',x.player)
        x.next_Player()
        self.assertEqual('G',x.player)
        x.next_Player()
        self.assertEqual('P',x.player)
        x.next_Player()
        self.assertEqual('B',x.player)
        x.next_Player()
        self.assertEqual('O',x.player)
        x.next_Player()
        self.assertEqual('Y',x.player)
        x.next_Player()
        self.assertEqual('R',x.player)

    def test_move_piece(self):
        x=board.board()
        x.board=[['x', 'x', 'x', 'R', 'x', 'x', 'x', ], 
                 ['x', 'x', '.', ' ', '.', 'x', 'x', ], 
                 ['x', '.', ' ', '.', ' ', '.', 'x', ], 
                 ['.', ' ', '.', ' ', 'R', ' ', 'B', ],
                 ['x', '.', ' ', '.', ' ', '.', 'x', ],
                 ['x', 'x', '.', ' ', '.', 'x', 'x', ],
                 ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        
        x.move(1,-1,3,6)
        postMove=[['x', 'x', 'x', 'R', 'x', 'x', 'x', ], 
                 ['x', 'x', '.', ' ', '.', 'x', 'x', ], 
                 ['x', '.', ' ', '.', ' ', 'B', 'x', ], 
                 ['.', ' ', '.', ' ', 'R', ' ', '.', ],
                 ['x', '.', ' ', '.', ' ', '.', 'x', ],
                 ['x', 'x', '.', ' ', '.', 'x', 'x', ],
                 ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.assertEqual(x.board,postMove)

    def test_evaluation(self):
        x=board.board()
        y=evaluation.evaluator(x,x.player,x.mode)
        print("evaluations:")
        print(y.evaluatePosition(x.player,x))

        x.board=[['x', 'x', 'x', '.', 'x', 'x', 'x', ], 
                 ['x', 'x', '.', ' ', '.', 'x', 'x', ], 
                 ['x', 'R', ' ', 'R', ' ', 'B', 'x', ], 
                 ['R', ' ', '.', ' ', '.', ' ', '.', ],
                 ['x', '.', ' ', '.', ' ', '.', 'x', ],
                 ['x', 'x', '.', ' ', 'B', 'x', 'x', ],
                 ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]

        print("evaluations:")
        print(y.evaluatePosition(x.player,x))

        test = board.board()
        test.swap_board("full")

        evaluate = evaluation.evaluator(test, test.player, test.mode)

        print(evaluate.evaluatePosition(test.player,test))
        #G
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))
        #P
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))

        #B
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))

        #O
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))

        #Y
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))

        #R
        test.next_Player()
        print(test.player)
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))
        self.assertEqual(30,evaluate.evaluatePosition(test.player,test))


        test.swap_board("small")
        evaluate = evaluation.evaluator(test, test.player, test.mode)
        print(evaluate.evaluatePosition(test.player,test))

if __name__ == '__main__':
    unittest.main()
