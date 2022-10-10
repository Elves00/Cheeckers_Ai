import board


class miniMax:

    def setGameBoard(self, board):
        self.gameBoard = board

    # maximiser
    def max(self):
        print("max")
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
            print("max victory player:", self.gameBoard.player)
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            print("min victory player:", self.gameBoard.player)
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
                                        posRow, posCol, moveList)
                                    print(m, ":", maxv)
                                    print(px)
                                    # Checks if we have a better move and set it
                                    if m > maxv:
                                        print("its greater jumping max?")
                                        maxv = m
                                        my = i
                                        mx = j
                                        px = posRow
                                        py = posCol

                                    print("jumping max px:", px)

                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])
                                    print("ended in a jump")

                                else:

                                    # Check current position value
                                    currentValue = self.gameBoard.position_evaluator()
                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)
                                    # Evaluate the position only if its better for R
                                    if (self.gameBoard.position_evaluator() > currentValue):
                                        print(self.gameBoard.player)
                                        self.gameBoard.next_Player()
                                        
                                        print(self.gameBoard.player,
                                              "swap called by max")
                                        # Call min
                                        (m, max_y, max_x, pos_x, pos_y) = self.min()
                                        print(m,  ":", maxv)
                                        print(px)
                                        if m > maxv:
                                            print("its greater max?")
                                            maxv = m
                                            my = i
                                            mx = j
                                            px = posRow
                                            py = posCol

                                        # Swap back to current player
                                        self.gameBoard.next_Player()

                                        print("min px:", px)
                                    # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    print("ended in a move")

        if (not (validMove)):
            print("NO VALID MOVES MAX")
            self.gameBoard.player = currentPlayer

        print("Returned from end",maxv, my, mx, px, py)
        return (maxv, my, mx, px, py)

    # maximises the jumping cycle
    def jumping_max(self, posRow, posCol, moveList):

        print("jumping max")
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
            print("jumping max victory:", self.gameBoard.player)
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            print("jumping max victory:", self.gameBoard.player)
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
                        print("starting jumping max with: ",
                              self.gameBoard.player)
                        (m, max_i, max_j, pos_x, pos_y) = self.jumping_max(
                            tempRow, tempCol, moveList)

                        if m > maxv:
                            maxv = m
                            my = i
                            mx = j

                        # Move the peice back to previous position
                        print(self.gameBoard.player)
                        self.gameBoard.next_Player()
                        print(self.gameBoard.player,
                              "swap called by jumping max")
                        (m, min_i, min_j, pos_x, pos_y) = self.min()

                        if m > maxv:
                            maxv = m
                            my = i
                            mx = j

                        self.gameBoard.next_Player()

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            print("NO VALID MOVES ######################################## MAX")
            self.gameBoard.player = currentPlayer
        print("returning jumping max player:", self.gameBoard.player)
        return (maxv, my, mx, px, py)

    def min(self):
        print("min")
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
            print("min victory player:", self.gameBoard.player)
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            print("min victory player:", self.gameBoard.player)
            return (-1, 0, 0, 0, 0)

        print("here")

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
                                    # print("jump")
                                    # Tracks moves taken
                                    moveList = [[posRow, posCol]]
                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, min_y, min_x, pos_x, pos_y) = self.jumping_min(
                                        posRow, posCol, moveList)
                                    # Checks if we have a better move and set it
                                    if m < minv:
                                        minv = m
                                        my = i
                                        mx = j
                                        px = posRow
                                        py = posCol
                                    # remove move from list after checking
                                    moveList.remove([posRow, posCol])

                                else:
                                    currentValue = self.gameBoard.position_evaluator()

                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)

                                    # evaluate the position only if it's less then the current value
                                    if (self.gameBoard.position_evaluator() < currentValue):

                                        print(self.gameBoard.player)
                                        self.gameBoard.next_Player()
                                        print(self.gameBoard.player,
                                              "swap called by min")
                                        (m, max_y, max_x, pos_x, pos_y) = self.max()
                                        if m < minv:
                                            minv = m
                                            my = i
                                            mx = j
                                            px = posRow
                                            py = posCol
                                        # Swap back to current player
                                        self.gameBoard.next_Player()

                                        # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        # print("returning min:",minv,mx,my,px,py," player:",self.gameBoard.player)
        if (not (validMove)):
            print("NO VALID MOVES MIN", self.gameBoard.player, currentPlayer)
            self.gameBoard.player = currentPlayer
        return (minv, my, mx, px, py)

    def jumping_min(self, posRow, posCol, moveList):
        print("minimizing jump")
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
            print("jumping min player:", self.gameBoard.player)
            return (1, 0, 0, 0, 0)
        # The other player wins
        elif (result == 4):
            print("jumping min player:", self.gameBoard.player)
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
                            tempRow, tempCol, moveList)

                        if m < minv:
                            minv = m
                            mx = i
                            my = j
                        # Swap player to play min
                        self.gameBoard.next_Player()
                        print(self.gameBoard.player,
                              "swap called by jumping min")
                        (m, min_i, min_j, pos_x, pos_y) = self.max()

                        if m < minv:
                            minv = m
                            mx = i
                            my = j

                        # Swap back to current player
                        self.gameBoard.next_Player()

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            self.gameBoard.player = currentPlayer
            print("NO VALID MOVES ######################################## MIN JUMPING",
                  self.gameBoard.player)

        # print("returning jumping min player:",self.gameBoard.player)
        return (minv, mx, my, px, py)
