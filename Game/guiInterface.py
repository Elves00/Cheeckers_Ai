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

        if (player != self.currentBoard.player):
            return False

        if (self.currentBoard.is_move_valid(dy, dx, startPosY, startPosX)):
            if (self.currentBoard.is_jump_valid(dy, dx, startPosY, startPosX, self.moveList)):
                (tempRow, tempCol) = self.currentBoard.jump(
                    dy, dx, startPosY, startPosX, self.moveList)
                self.currentBoard.human_jump(tempRow, tempCol)
                self.currentBoard.next_Player()
                return True
            else:
                self.currentBoard.move(dy, dx, startPosY, startPosX)
                self.currentBoard.next_Player()
                return True
        else:
            return False

    def ai_move(self):
        self.miniMax.setGameBoard(self.currentBoard)
        
        turn=self.currentBoard.turn
        (winLoss, upOrDown, leftOrRight,
         posRow, posCol) = self.miniMax.max(-2,self.miniMax.maxValue+2)

        
        print("Max Returned:", winLoss, upOrDown,
              leftOrRight, posRow, posCol , "Player:",self.currentBoard.player)
        
        # If the AI move is a jump call the ai can move again
        if (self.currentBoard.is_jump(upOrDown, leftOrRight, posRow, posCol)):

            # Lets the ai jump again using peice it just moved
            moveList = []
            while (self.currentBoard.is_jump(upOrDown, leftOrRight, posRow, posCol) and not self.currentBoard.is_end()):
                self.currentBoard.display()
                # Performs the first jump
                (moveList, tempRow, tempCol) = self.currentBoard.jump(
                    upOrDown, leftOrRight, posRow, posCol, moveList)

                # update game baord for mini max
                self.miniMax.setGameBoard(self.currentBoard)

                # Runs jumping max with previous move list
                (winLoss, upOrDown, leftOrRight,
                    posRow, posCol) = self.miniMax.jumping_max(tempRow, tempCol, moveList,-2,self.miniMax.maxValue+2)
                # If the AI retuned none it means there is no moves for the jumping piece without doubling back
                if (posRow == None or posCol == None or winLoss != 16):
                    break
        else:
            # Perform a regular move
            self.currentBoard.move(upOrDown, leftOrRight, posRow, posCol)

        #Hard resets the turn
        self.currentBoard.turn=turn
        self.currentBoard.next_Player()
    def getCurrentBoard(self):
        return self.currentBoard

    def setCurrentBoard(self, board):
        self.currentBoard = board


x = guiInterface()
if (x.is_player_move_valid(5, 4, 6, 3, 'R')):
    print("Works for small board")
x.currentBoard.display()
# print(x.currentBoard.player)
# print(x.currentBoard.board[3][13])
# if (x.is_player_move_valid(4, 14, 3, 13, 'R')):
#     print("Works for full board")
# x.currentBoard.display()
# if (x.is_player_move_valid(4, 14, 3, 13, 'R')):
#     raise Exception("Doesn't work here")
# else:
#     print("No longer the player so returns false")

x.currentBoard.display()
#R
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#G
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()
#P
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#B
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()
#O
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#Y
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#R
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#G
print("layer:",x.currentBoard.player)
input()
x.ai_move()
x.currentBoard.display()
input()

#P
x.ai_move()
x.currentBoard.display()
#B
input()
x.ai_move()
input()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
print("layer:",x.currentBoard.player)
input()
x.ai_move()
input()
print("layer:",x.currentBoard.player)
input()
x.ai_move()
input()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()

x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()
x.ai_move()
x.currentBoard.display()