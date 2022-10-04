from board import board
from miniMax import miniMax


class game:
    def __init__(self) -> None:
        self.gameSetUp()

    def gameSetUp(self):
        self.gameBoard = board()
        self.gameBoard.display()
        self.miniMax = miniMax()
        self.miniMax.setGameBoard(self.gameBoard)

    def play(self):
        while (not (self.gameBoard.is_end())):
            self.gameBoard.player = 'B'
            currentPlayer = self.gameBoard.player
            self.gameBoard.display()
            self.gameBoard.select_piece()
            if (currentPlayer != self.gameBoard.player):
                print("mini maxing...")
                # updates minimax game board
                self.miniMax.setGameBoard(self.gameBoard)
                self.gameBoard.display()
                # Get move from max
                (winLoss, upOrDown, leftOrRight,
                 posRow, posCol) = self.miniMax.max()
                print("max Returned:", winLoss, upOrDown,
                      leftOrRight, posRow, posCol)
                if (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol)):

                    moveList = []
                    # ISUE WITH NONE TYPE
                    while (self.gameBoard.is_jump(upOrDown, leftOrRight, posRow, posCol) and not self.gameBoard.is_end()):

                        # Could be issue here with move list
                        (moveList, tempRow, tempCol) = self.gameBoard.jump(
                            upOrDown, leftOrRight, posRow, posCol, moveList)
                        # update game baord
                        self.miniMax.setGameBoard(self.gameBoard)
                        # run max
                        (winLoss, upOrDown, leftOrRight,
                         posRow, posCol) = self.miniMax.max()
                else:
                    print("here")
                    print(upOrDown, leftOrRight, posRow, posCol)
                    self.gameBoard.move(upOrDown, leftOrRight, posRow, posCol)
            # revert to player

                # print(self.miniMax.max())


x = game()
x.play()
