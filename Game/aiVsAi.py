import time
from board import board
from miniMaxAlphaBetaEval import miniMaxAlphaBeta


class game:
    def __init__(self) -> None:
        self.gameSetUp()

    def gameSetUp(self):
        self.gameBoard = board()
        self.gameBoard.display()
        self.miniMax = miniMaxAlphaBeta()
        self.gameBoard.swap_board("small two")
        self.miniMax.setGameBoard(self.gameBoard)
        self.d=0

    def play(self):
        while (not (self.gameBoard.is_end())):
                self.gameBoard.display()
                #Updates the board with the players move
                self.miniMax.setGameBoard(self.gameBoard)
                #Start timer for evaluation
                start=time.time()
                currentTurn=self.gameBoard.turn
                if(self.miniMax.maxValue==0):
                    raise Exception("0 error")
                #Get Ai move
                (winLoss, upOrDown, leftOrRight,
                 posRow, posCol) = self.miniMax.max(-2,self.miniMax.maxValue+2)
                print("Max Returned:", winLoss, upOrDown,
                      leftOrRight, posRow, posCol)

                #If the AI move is a jump call the ai can move again
                if (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol)):
                    
                    #Lets the ai jump again using peice it just moved
                    moveList = []
                    while (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol) and not self.gameBoard.is_end()):
                        #Performs the first jump
                        (moveList, tempRow, tempCol) = self.gameBoard.jump(
                            upOrDown, leftOrRight, posRow, posCol, moveList)

                        #update game baord for mini max
                        self.miniMax.setGameBoard(self.gameBoard)
                        self.gameBoard.display()
                        print(self.gameBoard.player)
                        
                        # Runs jumping max with previous move list
                        (winLoss, upOrDown, leftOrRight,
                         posRow, posCol) = self.miniMax.jumping_max(tempRow, tempCol, moveList, -2,self.miniMax.maxValue+2)
                        
                        #If the AI retuned none it means there is no moves for the jumping piece without doubling back
                        if (posRow == None or posCol == None):
                            break
                else:
                    #Perform a regular move
                    self.gameBoard.move(upOrDown, leftOrRight, posRow, posCol)

                #Print ai thinking time
                end=time.time()
                print('Evaluation time: {}s'.format(round(end-start,7)))
                self.gameBoard.turn=currentTurn
                self.gameBoard.next_Player()
        self.gameBoard.display()




x = game()
x.play()
