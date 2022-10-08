import board
from evaluation import evaluator


class miniMaxAlphaBeta:

    def setGameBoard(self, board):
        self.gameBoard = board
        self.evaluator = evaluator(
            self.gameBoard, self.gameBoard.player, self.gameBoard.mode)
        self.maxPlayer = self.gameBoard.player

    # maximiser
    def max(self, alpha, beta):

        # possible values
        # 1 player 1 wins 2 player 2 wins
        maxv = - 2
        mx = None
        my = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                return (0, 0, 0, 0, 0)

        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)
        currentPlayer = self.gameBoard.player
        validMove = False
        # if the game hasn't ended cycle through all possible moves
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):

                # It's the max players piece
                if (self.gameBoard.board[posRow][posCol] == self.maxPlayer):
                    print("MAX PLAYER:", self.maxPlayer)
                    # list of possible movment directions
                    direction = [-1, 0, 1]

                    # Search all move directions for current piece
                    for i in direction:
                        for j in direction:

                            # if the move is possible investigate
                            if (self.gameBoard.is_move_valid(i, j, posRow, posCol)):

                                # There was a valid move
                                validMove = True

                                # Check if the move being attempted is a jump
                                if (self.gameBoard.is_jump(i, j, posRow, posCol)):

                                    # Tracks which jumps have been taken
                                    moveList = [[posRow, posCol]]

                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, max_y, max_x, pos_x, pos_y) = self.jumping_max(
                                        posRow, posCol, moveList, alpha, beta)

                                    # If the value returned was not null (a move was possible)
                                    if (m != None):

                                        # Checks if the end position is greater then current max value setting accordingly
                                        if m > maxv:
                                            maxv = m
                                            my = i
                                            mx = j
                                            px = posRow
                                            py = posCol

                                        # if maxv >= beta (starts at 2) then we return
                                        if maxv >= beta:
                                            moveList.remove([posRow, posCol])
                                            return (maxv, my, mx, px, py)

                                        # Raises the value of alpha
                                        if maxv > alpha:
                                            alpha = maxv

                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])

                                else:
                                    # Check current position value
                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)
                                    # Evaluate the position only if its better for R
                                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                                        currentValue = self.evaluator.evaluatePosition(
                                            self.gameBoard.player, self.gameBoard)
                                        self.gameBoard.swap_Player()
                                        # Call min
                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.min(alpha, beta)
                                        if (m != None):
                                            if m > maxv:
                                                maxv = m
                                                my = i
                                                mx = j
                                                px = posRow
                                                py = posCol

                                            if maxv >= beta:
                                                # Swap back to current player
                                                self.gameBoard.swap_Player()
                                                # remove move
                                                self.gameBoard.swap_Piece(
                                                    tempRow, tempCol, posRow, posCol)
                                                return (maxv, my, mx, px, py)

                                            if maxv > alpha:
                                                alpha = maxv
                                            # Swap back to current player
                                        self.gameBoard.swap_Player()

                                    # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            print("no valid moves")

            # No valid move so return worst case for parent
        self.gameBoard.display()
        return (maxv, my, mx, px, py)

    # maximises the jumping cycle
    def jumping_max(self, posRow, posCol, moveList, alpha, beta):

        maxv = -2
        mx = None
        my = None
        px = None
        py = None

        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                return (0, 0, 0, 0, 0)

        # gets value before move
        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)

        currentPlayer = self.gameBoard.player
        validMove = False

        # Posible directions a piece can move
        direction = [-1, 0, 1]

        # For all directions in x and y
        for i in direction:
            for j in direction:
                # Check if there is a valid jump and explore it
                if (self.gameBoard.is_jump_valid(i, j, posRow, posCol, moveList)):

                    # Stores the new move position and moves piece
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)

                    # maximises for the new position if it is a greater value
                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                        currentValue = self.evaluator.evaluatePosition(
                            self.gameBoard.player, self.gameBoard)

                        validMove = True

                        (m, max_i, max_j, pos_x, pos_y) = self.jumping_max(
                            tempRow, tempCol, moveList, alpha, beta)
                        if (m != None):
                            if m > maxv:
                                maxv = m
                                my = i
                                mx = j
                                px = posCol
                                py = posRow

                            if maxv >= beta:
                                self.gameBoard.swap_Piece(
                                    tempRow, tempCol, posRow, posCol)

                                return (maxv, my, mx, px, py)

                            if maxv > alpha:
                                alpha = maxv
                            # Move the peice back to previous position
                            self.gameBoard.swap_Player()

                            (m, min_i, min_j, pos_x, pos_y) = self.min(alpha, beta)
                            if (m != None):
                                if m > maxv:
                                    maxv = m
                                    my = i
                                    mx = j
                                    px = posCol
                                    py = posRow

                                if maxv >= beta:

                                    self.gameBoard.swap_Player()
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    return (maxv, my, mx, px, py)

                                if maxv > alpha:
                                    alpha = maxv

                            self.gameBoard.swap_Player()

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent

        return (maxv, my, mx, px, py)

    def min(self, alpha, beta):

        # possible values
        # 1 player 1 wins 2 player 2 wins
        minv = 17
        mx = None
        my = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                return (0, 0, 0, 0, 0)

        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)
        validMove = False
        currentPlayer = self.gameBoard.player
        # if the game hasn't ended cycle through all possible moves
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):

                # It's the max players piece
                if (self.gameBoard.board[posRow][posCol] == self.gameBoard.player and self.gameBoard.board[posRow][posCol] != self.maxPlayer):
                    # list of possible movment directions
                    direction = [1, 0, -1]
                    # cycle all move directions
                    for i in direction:
                        for j in direction:
                            # if the move is valid
                            if (self.gameBoard.is_move_valid(i, j, posRow, posCol)):

                                # Check if the move being attempted is a jump
                                if (self.gameBoard.is_jump(i, j, posRow, posCol)):
                                    # Tracks moves taken
                                    moveList = [[posRow, posCol]]
                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, min_y, min_x, pos_x, pos_y) = self.jumping_min(
                                        posRow, posCol, moveList, alpha, beta)
                                    if (m != None):
                                        # Checks if we have a better move and set it
                                        if m < minv:
                                            minv = m
                                            my = i
                                            mx = j
                                            px = posCol
                                            py = posRow

                                        if minv <= alpha:
                                            moveList.remove([posRow, posCol])
                                            return (minv, my, mx, px, py)

                                        if minv < beta:
                                            beta = minv

                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])

                                else:

                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)

                                    # evaluate the position only if it's less then the current value
                                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                                        currentValue = self.evaluator.evaluatePosition(
                                            self.gameBoard.player, self.gameBoard)

                                        self.gameBoard.swap_Player()

                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.max(alpha, beta)
                                        if (m != None):
                                            if m < minv:
                                                minv = m
                                                my = i
                                                mx = j
                                                px = posCol
                                                py = posRow

                                            if minv <= alpha:
                                                self.gameBoard.swap_Player()
                                                self.gameBoard.swap_Piece(
                                                    tempRow, tempCol, posRow, posCol)
                                                return (minv, my, mx, px, py)

                                            if minv < beta:
                                                beta = minv
                                            # Swap back to current player
                                        self.gameBoard.swap_Player()

                                        # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
        return (minv, my, mx, px, py)

    def jumping_min(self, posRow, posCol, moveList, alpha, beta):

        # possible values
        # 1 player 1 wins 2 player 2 wins

        minv = 17
        my = None
        mx = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                return (0, 0, 0, 0, 0)

        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)

        validMove = False
        currentPlayer = self.gameBoard.player
        # Posible directions a piece can move
        direction = [1, 0, -1]

        # For all directions in x and y
        for i in direction:
            for j in direction:
                # Check if there is a valid jump and explore it
                if (self.gameBoard.is_jump_valid(i, j, posRow, posCol, moveList)):

                    # Stores the new move position
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)

                    # maximises for the new position
                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                        currentValue = self.evaluator.evaluatePosition(
                            self.gameBoard.player, self.gameBoard)
                        validMove = True
                        (m, min_i, min_j, pos_x, pos_y) = self.jumping_min(
                            tempRow, tempCol, moveList, alpha, beta)
                        if (m != None):

                            if m < minv:
                                minv = m
                                mx = i
                                my = j
                                px = posCol
                                py = posRow

                            if minv <= alpha:

                                self.gameBoard.swap_Piece(
                                    tempRow, tempCol, posRow, posCol)

                                return (minv, my, mx, px, py)

                            if minv < beta:
                                beta = minv
                            # Swap player to play min
                            self.gameBoard.swap_Player()
                            (m, min_i, min_j, pos_x, pos_y) = self.max(alpha, beta)
                            if (m != None):
                                if m < minv:
                                    minv = m
                                    mx = i
                                    my = j
                                    posCol
                                    py = posRow

                                if minv <= alpha:
                                    self.gameBoard.swap_Player()
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

                                    return (minv, my, mx, px, py)

                                if minv < beta:
                                    beta = minv

                                # Swap back to current player
                            self.gameBoard.swap_Player()

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent

        return (minv, mx, my, px, py)
