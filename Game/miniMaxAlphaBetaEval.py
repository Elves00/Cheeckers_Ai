from pyrsistent import v
from evaluation import evaluator


class miniMaxAlphaBeta:

    def setGameBoard(self, board):
        self.gameBoard = board
        self.evaluator = evaluator(
            self.gameBoard, self.gameBoard.player, self.gameBoard.mode)
        self.maxPlayer = self.gameBoard.player
        self.depth = 0
        self.turn = self.gameBoard.turn

    # maximiser
    def max(self, alpha, beta):

        if (self.turn != self.gameBoard.turn):
            raise Exception("TURN IS WRONG")
        if (self.gameBoard.player != self.maxPlayer):
            raise Exception("Max has the wrong player")

        if (self.depth > 3):
            evaluation = int(self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)/16)
            return (evaluation, None, None, None, None)

        print("Max", alpha, beta)
        maxv = - 2
        mx = None
        my = None
        px = None
        py = None

        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                print("end 16")
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                print("end 0")
                return (0, 0, 0, 0, 0)

        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)
        currentPlayer = self.gameBoard.player
        currentTurn = self.gameBoard.turn

        if (currentPlayer != self.maxPlayer):
            raise Exception("Max has the wrong player")

        validMove = False
        # if the game hasn't ended cycle through all possible moves
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):

                # It's the max players piece
                if (self.gameBoard.board[posRow][posCol] == self.maxPlayer):
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
                                    self.depth += 1
                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, max_y, max_x, pos_x, pos_y) = self.jumping_max(
                                        posRow, posCol, moveList, alpha, beta)
                                    print("jumping max returned", m)
                                    self.depth -= 1

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
                                            print("returning maxv>beta")
                                            moveList.remove([posRow, posCol])
                                            self.gameBoard.player = currentPlayer
                                            self.gameBoard.turn = currentTurn

                                            return (maxv, my, mx, px, py)

                                        # Raises the value of alpha
                                        if maxv > alpha:
                                            alpha = maxv
                                    #
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
                                        self.gameBoard.next_Player()
                                        self.depth += 1
                                        # Call min
                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.min(alpha, beta)
                                        print("min returned", m)
                                        self.depth -= 1
                                        if (m != None):
                                            if m > maxv:
                                                maxv = m
                                                my = i
                                                mx = j
                                                px = posRow
                                                py = posCol

                                            if maxv >= beta:
                                                # Swap back to current player
                                                self.gameBoard.player = currentPlayer
                                                # remove move
                                                self.gameBoard.swap_Piece(
                                                    tempRow, tempCol, posRow, posCol)
                                                self.gameBoard.turn = currentTurn
                                                # Return with current player
                                                print("maxv>beta")
                                                return (maxv, my, mx, px, py)

                                            if maxv > alpha:
                                                alpha = maxv
                                        # Swap back to current player
                                        self.gameBoard.player = currentPlayer
                                        self.gameBoard.turn = currentTurn

                                    # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            # Swap back to current player
            self.gameBoard.player = currentPlayer
            self.gameBoard.turn = currentTurn

        print(self.gameBoard.player, self.maxPlayer)
        return (maxv, my, mx, px, py)

    # maximises the jumping cycle
    def jumping_max(self, posRow, posCol, moveList, alpha, beta):
        print("Jumping Max", alpha, beta)
        if (self.depth > 3):
            evaluation = int(self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)/16)
            return (evaluation, None, None, None, None)

        maxv = -2
        mx = None
        my = None
        px = None
        py = None

        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                print("end 16")
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                print("end 0")
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
                        self.depth += 1

                        (m, max_i, max_j, pos_x, pos_y) = self.jumping_max(
                            tempRow, tempCol, moveList, alpha, beta)
                        self.depth -= 1

                        if (m != None):
                            if m > maxv:
                                maxv = m
                                my = i
                                mx = j
                                px = posCol
                                py = posRow

                            if maxv >= beta:
                                print("jumpingmaxv>beta")
                                self.gameBoard.swap_Piece(
                                    tempRow, tempCol, posRow, posCol)

                                return (maxv, my, mx, px, py)

                            if maxv > alpha:
                                alpha = maxv

                        # Swap to next player and evaluate postion regardless if m returned was None
                        self.gameBoard.next_Player()
                        self.depth += 1

                        (m, min_i, min_j, pos_x, pos_y) = self.min(alpha, beta)
                        self.depth -= 1

                        if (m != None):
                            if m > maxv:
                                maxv = m
                                my = i
                                mx = j
                                px = posCol
                                py = posRow

                            if maxv >= beta:
                                # Swap back to current player
                                self.gameBoard.player = currentPlayer
                                self.gameBoard.swap_Piece(
                                    tempRow, tempCol, posRow, posCol)
                                print("jumpingmaxv>beta")
                                return (maxv, my, mx, px, py)

                            if maxv > alpha:
                                alpha = maxv

                        # Swap back to current player
                        self.gameBoard.player = currentPlayer

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
           # Swap back to current player
            self.gameBoard.player = currentPlayer
            maxv = 8

        print("returning from jumping max with :", maxv, my, mx, px, py)
        return (maxv, my, mx, px, py)

    def min(self, alpha, beta):
        if (self.depth > 3):
            evaluation = int(self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)/16)
            return (16-evaluation, None, None, None, None)
        print("Min", alpha, beta)

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
                print("end 16")
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                print("end 0")
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
                                validMove = True
                                # Check if the move being attempted is a jump
                                if (self.gameBoard.is_jump(i, j, posRow, posCol)):

                                    # Tracks moves taken
                                    moveList = [[posRow, posCol]]
                                    print("Caling jumping min with beta=", beta)
                                    # Minimizes jumping (Minmising occurs inside the jumping_min)
                                    self.depth += 1

                                    (m, min_y, min_x, pos_x, pos_y) = self.jumping_min(
                                        posRow, posCol, moveList, alpha, beta)
                                    self.depth -= 1

                                    if (m != None):
                                        print("m:", m, "minv:", minv)
                                        print(posCol, posRow)
                                        # Checks if we have a better move and set it
                                        if m < minv:
                                            minv = m
                                            my = i
                                            mx = j
                                            px = posCol
                                            py = posRow

                                        if minv <= alpha:
                                            print("min returned cause <= alpha")
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

                                        self.gameBoard.next_Player()
                                        # Maximise if it's the max players turn otherwise minimize again
                                        if (self.gameBoard.player != self.maxPlayer):
                                            self.depth += 1

                                            (m, max_y, max_x, pos_x,
                                             pos_y) = self.min(alpha, beta)
                                            self.depth -= 1

                                            if (m != None):
                                                if m < minv:
                                                    print("m:", m)
                                                    print("alpha", alpha)
                                                    print("beta", beta)
                                                    minv = m
                                                    my = i
                                                    mx = j
                                                    px = posCol
                                                    py = posRow

                                                if minv <= alpha:

                                                    print(alpha, beta)
                                                    self.gameBoard.display()
                                                    # Swap back to current player
                                                    self.gameBoard.player = currentPlayer
                                                    self.gameBoard.swap_Piece(
                                                        tempRow, tempCol, posRow, posCol)
                                                    print("minv<beta in min")
                                                    print(minv, my, mx, py, px)
                                                    return (minv, my, mx, px, py)

                                                if minv < beta:
                                                    beta = minv

                                            # Swap back to current player
                                            self.gameBoard.player = currentPlayer
                                        else:
                                            print(
                                                "caling max with alpha beta =", alpha, beta)
                                            self.depth += 1

                                            (m, max_y, max_x, pos_x,
                                             pos_y) = self.max(alpha, beta)
                                            self.depth -= 1

                                            if (m != None):
                                                if m < minv:
                                                    print("m:", m)
                                                    print("alpha", alpha)
                                                    print("beta", beta)
                                                    minv = m
                                                    my = i
                                                    mx = j
                                                    px = posCol
                                                    py = posRow

                                                if minv <= alpha:
                                                    print(alpha, beta)
                                                    self.gameBoard.display()
                                                    # Swap back to current player
                                                    self.gameBoard.player = currentPlayer
                                                    self.gameBoard.swap_Piece(
                                                        tempRow, tempCol, posRow, posCol)
                                                    print("minv<beta in min")
                                                    print(minv, my, mx, py, px)
                                                    return (minv, my, mx, px, py)

                                                if minv < beta:
                                                    beta = minv

                                            # Swap back to current player
                                            self.gameBoard.player = currentPlayer

                                        # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            print(self.gameBoard.player)
            self.gameBoard.display()
            # Swap back to current player
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
            # There where no valid moves so the current move is deemed as one better then not moving
        return (minv, my, mx, px, py)

    def jumping_min(self, posRow, posCol, moveList, alpha, beta):
        if (self.depth > 3):
            evaluation = int(self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)/16)
            return (16-evaluation, None, None, None, None)
        print("Jumping Min", alpha, beta)

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
                print("end 16")
                return (16, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                print("end 0")
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
                    print("Jump is valid for the move ",
                          i, j, posRow, posCol, moveList)
                    # Stores the new move position
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)
                    self.gameBoard.display()
                    # maximises for the new position
                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                        currentValue = self.evaluator.evaluatePosition(
                            self.gameBoard.player, self.gameBoard)
                        validMove = True
                        self.depth += 1

                        (m, min_i, min_j, pos_x, pos_y) = self.jumping_min(
                            tempRow, tempCol, moveList, alpha, beta)
                        self.depth -= 1

                        # Valid m was returned from jumping min. Evaluate
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

                        self.gameBoard.next_Player()
                        if (self.gameBoard.player != self.maxPlayer):
                            self.depth += 1

                            (m, max_y, max_x, pos_x,
                                pos_y) = self.min(alpha, beta)
                            self.depth -= 1

                            if (m != None):
                                if m < minv:
                                    print("m:", m)
                                    print("alpha", alpha)
                                    print("beta", beta)
                                    minv = m
                                    my = i
                                    mx = j
                                    px = posCol
                                    py = posRow

                                if minv <= alpha:

                                    print(alpha, beta)
                                    self.gameBoard.display()
                                    # Swap back to current player
                                    self.gameBoard.player = currentPlayer
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    print("minv<beta in min")
                                    print(minv, my, mx, py, px)
                                    return (minv, my, mx, px, py)

                                if minv < beta:
                                    beta = minv

                            # Swap back to current player
                            self.gameBoard.player = currentPlayer

                        # If the next player is the max player max again
                        else:
                            print(
                                "caling max with alpha beta =", alpha, beta)
                            self.depth += 1

                            (m, max_y, max_x, pos_x,
                                pos_y) = self.max(alpha, beta)
                            self.depth -= 1

                            if (m != None):
                                if m < minv:
                                    print("m:", m)
                                    print("alpha", alpha)
                                    print("beta", beta)
                                    minv = m
                                    my = i
                                    mx = j
                                    px = posCol
                                    py = posRow

                                if minv <= alpha:

                                    print(alpha, beta)
                                    self.gameBoard.display()
                                    # Swap back to current player
                                    self.gameBoard.player = currentPlayer
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    print("minv<beta in min")
                                    print(minv, my, mx, py, px)

                                    return (minv, my, mx, px, py)

                                if minv < beta:
                                    beta = minv

                            # Swap back to current player
                        self.gameBoard.player = currentPlayer
                    print("Un swapping")
                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)
                    self.gameBoard.display()

        if (not (validMove)):
            # Swap back to current player
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
            # minv = self.evaluator.evaluatePosition(self.gameBoard.player,self.gameBoard)
            minv = 8

        return (minv, mx, my, px, py)
