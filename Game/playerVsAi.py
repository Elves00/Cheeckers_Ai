'''
This file allows you to play a command line game of chineese checkers vs an ai
using a mini-max algorithim with a position evaluator and alpha beta prunning
'''
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
        self.gameBoard.swap_board("full")
        self.miniMax.setGameBoard(self.gameBoard)
        self.d = 0

    def changeMode(self, mode):
        '''
        Changes the checkers game mode
        Accepts string inputs
        "small"  : for a 6 by 6 two player game with 1 controlable piece
        "small two" : for a 6 by 6 two player game with 2 controlable pieces
        "small full" : for a 6 by 6 two player game with 3 controlable pieces
        "full" : for a full sized game with 6 players and 10 controlable pieces
        '''
        self.gameBoard = board()
        self.gameBoard.display()
        self.miniMax = miniMaxAlphaBeta()
        self.gameBoard.swap_board(mode)
        self.miniMax.setGameBoard(self.gameBoard)
        self.d = 0

    def play(self):
        '''
        Starts a game of chinese checkers
        '''
        while (not (self.gameBoard.is_end())):
            self.d += 1
            if (self.gameBoard.player == 'B'):
                currentPlayer = self.gameBoard.player
                #  Display the board
                self.gameBoard.display()
                # Make player move
                self.gameBoard.select_piece()
                print("mini maxing")

            # Updates the board with the players move
            self.miniMax.setGameBoard(self.gameBoard)
            # Start timer for evaluation
            start = time.time()
            currentTurn = self.gameBoard.turn

            # Get Ai move
            (winLoss, upOrDown, leftOrRight,
             posRow, posCol) = self.miniMax.max(-2, self.miniMax.maxValue+2)
            self.gameBoard.display()
            print(self.d)
            print(self.gameBoard.player)
            print("Max Returned:", winLoss, upOrDown,
                  leftOrRight, posRow, posCol)
            startingWinLoss = winLoss

            # If the AI move is a jump call the ai can move again
            if (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol)):

                # Lets the ai jump again using peice it just moved
                moveList = []
                while (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol) and not self.gameBoard.is_end()):
                    # Performs the first jump
                    print(upOrDown, leftOrRight, posRow, posCol)
                    (moveList, tempRow, tempCol) = self.gameBoard.jump(
                        upOrDown, leftOrRight, posRow, posCol, moveList)

                    # update game baord for mini max
                    self.miniMax.setGameBoard(self.gameBoard)
                    # self.gameBoard.display()
                    print(self.gameBoard.player)

                    # Runs jumping max with previous move list
                    (winLoss, upOrDown, leftOrRight,
                     posRow, posCol) = self.miniMax.jumping_max(tempRow, tempCol, moveList, -2, self.miniMax.maxValue+2)

                    # If the AI retuned none it means there is no moves for the jumping piece without doubling back
                    if (posRow == None or posCol == None):
                        break
            else:
                # Perform a regular move
                self.gameBoard.move(upOrDown, leftOrRight, posRow, posCol)

            # Print ai thinking time
            end = time.time()
            print('Evaluation time: {}s'.format(round(end-start, 7)))
            self.gameBoard.turn = currentTurn
            self.gameBoard.next_Player()
        print(self.gameBoard.is_end())
        self.gameBoard.display()


x = game()
x.play()
