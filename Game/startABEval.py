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
        self.miniMax.setGameBoard(self.gameBoard)
        self.gameBoard.swap_board("small full")

    def play(self):
        while (not (self.gameBoard.is_end())):
            #Player controls B in two player
            self.gameBoard.player = 'B'
            self.gameBoard.turn = 1
            #Save current player
            currentPlayer = self.gameBoard.player

            #Display the board
            self.gameBoard.display()
            #Make player move
            self.gameBoard.select_piece()

            #If the player has changed
            if (currentPlayer != self.gameBoard.player):
                print("mini maxing...")

                #Updates the board with the players move
                self.miniMax.setGameBoard(self.gameBoard)
                #Start timer for evaluation
                start=time.time()

                #Get Ai move
                (winLoss, upOrDown, leftOrRight,
                 posRow, posCol) = self.miniMax.max(-2, 2)
                print("max Returned:", winLoss, upOrDown,
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

                        # Runs jumping max with previous move list
                        (winLoss, upOrDown, leftOrRight,
                         posRow, posCol) = self.miniMax.jumping_max(tempRow, tempCol, moveList, -2, 2)

                        #If the AI retuned none it means there is no moves for the jumping piece without doubling back
                        if (posRow == None or posCol == None):
                            break
                else:
                    #Perform a regular move
                    self.gameBoard.move(upOrDown, leftOrRight, posRow, posCol)
                
                #Print ai thinking time
                end=time.time()
                print('Evaluation time: {}s'.format(round(end-start,7)))



x = game()
x.play()
