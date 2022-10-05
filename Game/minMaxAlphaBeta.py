import board


class miniMaxAlphaBeta:

    def setGameBoard(self, board):
        self.gameBoard = board

    # maximiser
    def max(self, alpha, beta):
        # print("max")
        if (self.gameBoard.player == 'B'):
            raise Exception("Player B is playing jumping min")

        # possible values
        # 1 player 1 wins 2 player 2 wins
        maxv = - 2
        mx = None
        my = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        # Player 1 wins
        if (result == 1):
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            return (-1, 0, 0, 0, 0)

        currentPlayer = self.gameBoard.player
        validMove = False
        # if the game hasn't ended cycle through all possible moves
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):
                # It's the max players piece
                if (self.gameBoard.board[posRow][posCol] == 'R'):
                    # list of possible movment directions
                    direction = [-1, 0, 1]
                    # cycle all move directions
                    for i in direction:
                        for j in direction:
                            # if the move is possible investigate
                            if (self.gameBoard.is_move_valid(i, j, posRow, posCol)):
                                validMove = True
                                # Check if the move being attempted is a jump
                                if (self.gameBoard.is_jump(i, j, posRow, posCol)):
                                    # Tracks moves taken
                                    moveList = [[posRow, posCol]]
                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, max_y, max_x, pos_x, pos_y) = self.jumping_max(
                                        posRow, posCol, moveList, alpha, beta)
                                    if (m == None):
                                        m = maxv
                                    # Checks if we have a better move and set it
                                    if m > maxv:
                                        maxv = m
                                        my = i
                                        mx = j
                                        px = posRow
                                        py = posCol

                                    if maxv >= beta:
                                        moveList.remove([posRow, posCol])
                                        return (maxv, my, mx, px, py)

                                    if maxv > alpha:
                                        alpha = maxv

                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])

                                else:
                                    # Check current position value
                                    currentValue = self.gameBoard.position_evaluator()
                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)
                                    # Evaluate the position only if its better for R
                                    if (self.gameBoard.position_evaluator() > currentValue):
                                        self.gameBoard.swap_Player()

                                        # Call min
                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.min(alpha, beta)
                                        if (m == None):
                                            m = maxv
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
            # No valid move so return worst case for parent
            maxv = None
        
        
        return (maxv, my, mx, px, py)

    # maximises the jumping cycle
    def jumping_max(self, posRow, posCol, moveList, alpha, beta):
        # print("jumping max")

        if (self.gameBoard.player == 'B'):
            raise Exception("Player B is playing jumping min")

        # possible values
        # 1 player 1 wins 2 player 2 wins

        maxv = -2
        mx = None
        my = None
        px = None
        py = None

        result = self.gameBoard.is_end()

        # Player 1 wins
        if (result == 1):
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            return (-1, 0, 0, 0, 0)

        currentPlayer = self.gameBoard.player
        validMove = False

        # Posible directions a piece can move
        direction = [-1, 0, 1]

        # For all directions in x and y
        for i in direction:
            for j in direction:
                # Check if there is a valid jump and explore it
                if (self.gameBoard.is_jump_valid(i, j, posRow, posCol, moveList)):

                    # gets value before move
                    currentValue = self.gameBoard.position_evaluator()

                    # Stores the new move position and moves piece
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)

                    # maximises for the new position if it is a greater value
                    if (self.gameBoard.position_evaluator() > currentValue):
                        validMove = True

                        (m, max_i, max_j, pos_x, pos_y) = self.jumping_max(
                            tempRow, tempCol, moveList, alpha, beta)
                        if (m == None):
                            m = maxv
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
                        if (m == None):
                            m = maxv
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
            maxv = None

        return (maxv, my, mx, px, py)

    def min(self, alpha, beta):
        # print("min")
        if (self.gameBoard.player == 'R'):
            raise Exception("Starting min with R")

        # possible values
        # 1 player 1 wins 2 player 2 wins

        minv = 2
        mx = None
        my = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        # Player 1 wins
        if (result == 1):
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            return (-1, 0, 0, 0, 0)

        validMove = False
        currentPlayer = self.gameBoard.player
        # if the game hasn't ended cycle through all possible moves
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):

                # It's the max players piece
                if (self.gameBoard.board[posRow][posCol] == 'B'):
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
                                    if (m == None):
                                        m = minv
                                    # Checks if we have a better move and set it
                                    if m < minv:
                                        minv = m
                                        my = i
                                        mx = j

                                    if minv <= alpha:
                                        moveList.remove([posRow, posCol])
                                        # if(minv==2):
                                        #     raise Exception("2 returning in jumping min")
                                        return (minv, my, mx, px, py)

                                    if minv < beta:
                                        alpha = minv
                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])

                                else:
                                    currentValue = self.gameBoard.position_evaluator()

                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)

                                    # evaluate the position only if it's less then the current value
                                    if (self.gameBoard.position_evaluator() < currentValue):

                                        self.gameBoard.swap_Player()
                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.max(alpha, beta)

                                        if m < minv:
                                            minv = m
                                            my = i
                                            mx = j

                                        if minv <= alpha:
                                            self.gameBoard.swap_Player()
                                            self.gameBoard.swap_Piece(
                                                tempRow, tempCol, posRow, posCol)
                                            # if(minv==2):
                                            #     raise Exception("2 returning in min")
                                            return (minv, my, mx, px, py)

                                        if minv < beta:
                                            alpha = minv
                                        # Swap back to current player
                                        self.gameBoard.swap_Player()

                                        # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
            minv = None
        return (minv, my, mx, px, py)

    def jumping_min(self, posRow, posCol, moveList, alpha, beta):
        if (self.gameBoard.player == 'R'):
            raise Exception("Starting jumping min with R")

        # possible values
        # 1 player 1 wins 2 player 2 wins

        minv = 2
        my = None
        mx = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        # Player 1 wins
        if (result == 1):
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            return (-1, 0, 0, 0, 0)

        if (self.gameBoard.player == 'R'):
            raise Exception("Player R is playing jumping min")

        validMove = False
        currentPlayer = self.gameBoard.player
        # Posible directions a piece can move
        direction = [1, 0, -1]

        # For all directions in x and y
        for i in direction:
            for j in direction:
                # Check if there is a valid jump and explore it
                if (self.gameBoard.is_jump_valid(i, j, posRow, posCol, moveList)):

                    currentValue = self.gameBoard.position_evaluator()

                    # Stores the new move position
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)

                    # maximises for the new position
                    if (self.gameBoard.position_evaluator() < currentValue):
                        validMove = True
                        (m, min_i, min_j, pos_x, pos_y) = self.jumping_min(
                            tempRow, tempCol, moveList, alpha, beta)
                        if (m == None):
                            m = minv
                        if m < minv:
                            minv = m
                            mx = i
                            my = j

                        if minv <= alpha:
                            self.gameBoard.swap_Piece(
                                tempRow, tempCol, posRow, posCol)
                            # if(minv==2):
                            #     raise Exception("2 returning in jumping min")
                            return (minv, my, mx, px, py)

                        if minv < beta:
                            alpha = minv
                        # Swap player to play min
                        self.gameBoard.swap_Player()
                        (m, min_i, min_j, pos_x, pos_y) = self.max(alpha, beta)

                        if m < minv:
                            minv = m
                            mx = i
                            my = j

                        if minv <= alpha:
                            self.gameBoard.swap_Player()
                            self.gameBoard.swap_Piece(
                                tempRow, tempCol, posRow, posCol)
                            # if(minv==2):
                            #     raise Exception("2 returning in jumping min")
                            return (minv, my, mx, px, py)

                        if minv < beta:
                            alpha = minv

                        # Swap back to current player
                        self.gameBoard.swap_Player()

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
            minv = None

        return (minv, mx, my, px, py)
