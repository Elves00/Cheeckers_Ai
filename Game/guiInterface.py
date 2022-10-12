import board
import evaluation
from miniMaxAlphaBetaEval import miniMaxAlphaBeta


class guiInterface():

    def __init__(self):
        '''Sets up the interface'''
        self.currentBoard = board.board()
        self.currentBoard.swap_board("full")

        self.miniMax = miniMaxAlphaBeta()
        self.miniMax.setGameBoard(self.currentBoard)

        self.moveList = []

    def move(self, endPosY, endPosX, startPosY, startPosX, player):
        '''Performs a move'''
        dy = startPosY-endPosY
        dx = endPosX-startPosX

        if (dy > 2 or dy < -2):
            return False
        if (dx > 4 or dx < -4 or dx == 0 or dx == 3 or dx == -3):
            return False

        self.currentBoard.move(dy, dx, startPosY, startPosX)
        self.currentBoard.next_Player()

    def jump(self, endPosY, endPosX, startPosY, startPosX, player):
        '''Performs a jump'''
        dy = startPosY-endPosY
        dx = endPosX-startPosX
        if (dy > 2 or dy < -2):
            return (False,0)
        if (dx > 4 or dx < -4 or dx == 0 or dx == 3 or dx == -3):
            return (False,0)
        
        (movelist, tempRow, tempCol) = self.currentBoard.jump(
            dy, dx, startPosY, startPosX, self.moveList)
        self.currentBoard.next_Player()
        #Returns the position the piece has moved to.
        return (tempRow,tempCol)

    def is_jump(self, endPosY, endPosX, startPosY, startPosX, player):
        '''Is the move a jump'''
        dy = startPosY-endPosY
        dx = endPosX-startPosX

        if (dy > 2 or dy < -2):
            return False
        if (dx > 4 or dx < -4 or dx == 0 or dx == 3 or dx == -3):
            return False

        if (self.currentBoard.is_jump_valid(dy, dx, startPosY, startPosX, self.moveList)):
            return True
        else:
            return False

    def is_player_move_valid(self, endPosY, endPosX, startPosY, startPosX, player):
        '''
        Checks if a clicked player move is valid
        '''
        # most methods run of a direction based thing so we subtract to get direction
        # dx change in x
        # dy change in y
        # Note that dy is flipped cause it's weird
        dy = startPosY-endPosY
        dx = endPosX-startPosX

        if (dy > 2 or dy < -2):
            return False
        if (dx > 4 or dx < -4 or dx == 0 or dx == 3 or dx == -3):
            return False

        if (player != self.currentBoard.player):
            return False

        if (self.currentBoard.is_move_valid(dy, dx, startPosY, startPosX)):

            return True
        else:
            return False

    def ai_move(self):

        self.miniMax.setGameBoard(self.currentBoard)

        turn = self.currentBoard.turn

        (winLoss, upOrDown, leftOrRight,
         posRow, posCol) = self.miniMax.max(-2, self.miniMax.maxValue+2)
        initalRow=posRow
        initalCol=posCol
        print("Max Returned:", winLoss, upOrDown, leftOrRight, posRow, posCol, "Player:", self.currentBoard.player)

        # If the AI move is a jump call the ai can move again
        if (self.currentBoard.is_jump(upOrDown, leftOrRight, posRow, posCol)):

            # Lets the ai jump again using peice it just moved
            moveList = []
            while (self.currentBoard.is_jump(upOrDown, leftOrRight, posRow, posCol) and not self.currentBoard.is_end()):
                self.currentBoard.display()
                print(leftOrRight, upOrDown, posRow, posCol)
                input()

                # Performs the first jump
                (moveList, tempRow, tempCol) = self.currentBoard.jump(
                    upOrDown, leftOrRight, posRow, posCol, moveList)

                # update game baord for mini max
                self.miniMax.setGameBoard(self.currentBoard)

                # Runs jumping max with previous move list
                (winLoss, upOrDown, leftOrRight,
                    posRow, posCol) = self.miniMax.jumping_max(tempRow, tempCol, moveList, -2, self.miniMax.maxValue+2)
                # If the AI retuned none it means there is no moves for the jumping piece without doubling back
                if (posRow == None or posCol == None):
                    posRow=tempRow
                    posCol=tempCol
                    break
        else:
            (posRow,posCol)=self.currentBoard.move(upOrDown, leftOrRight, posRow, posCol)

        # Hard resets the turn
        self.currentBoard.turn = turn
        self.currentBoard.next_Player()
        finalRow=posRow
        finalCol=posCol
        return (finalRow,finalCol,initalRow,initalCol)

    def getCurrentBoard(self):
        return self.currentBoard

    def setCurrentBoard(self, board):
        self.currentBoard = board

