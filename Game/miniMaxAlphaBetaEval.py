from pyrsistent import v
from evaluation import evaluator
import random


class miniMaxAlphaBeta:

    def setGameBoard(self, board):
        self.gameBoard = board
        self.evaluator = evaluator(
            self.gameBoard, self.gameBoard.player, self.gameBoard.mode)
        self.maxPlayer = self.gameBoard.player
        self.depth = 0
        self.minValue = 0
        self.maxValue = 200
        #Reset max value based on board size
        if (self.gameBoard.mode == "full"):
            self.maxValue = 150
        elif (self.gameBoard.mode == "small"):
            self.maxValue = 6
        elif (self.gameBoard.mode == "small two"):
            self.maxValue = 11
        elif (self.gameBoard.mode == "small full"):
            self.maxValue = 16

    

    def max(self, alpha, beta):
        '''
        Maximises the value of a move
        Alpha and Beta used for prunning
        '''
        # print("Max", alpha, beta)
        #Depth limit prevents searching to long
        if (self.depth > 3):
            return (-2,None,None,None,None)

        #Set values to be returned to default. Max is set to minimum possible value
        #mx my: movment of a piece px py position of a piece
        maxv = - 2
        mx = None
        my = None
        px = None
        py = None

        #Checks if the game has ended
        result = self.gameBoard.is_end()

        #If the game has ended as the result of a move retunr either 0 for other players winning or maxValue for current player
        if (result != None):
            # Max player wins
            if (result == 1):
                return (self.maxValue, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                return (0, 0, 0, 0, 0)

        #Get the evaluated value of the current position the higher the value the better the position
        currentValue = self.evaluator.evaluatePosition(
            self.gameBoard.player, self.gameBoard)
        #Save the current player
        currentPlayer = self.gameBoard.player
        #Particulay in jumping max there may be no possible moves so this boolean tracks wether there was a valid move
        validMove = False

        # if the game hasn't ended cycle through all board pieces
        for posRow in range(0, self.gameBoard.boardHeight):
            for posCol in range(0, self.gameBoard.boardWidth):

                #Check moves only for the max players piece
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

                                # Checks wether the move was a jump or a regular move. 
                                # If it was a jump we call jumping max as the players turn is semi reset as they can take aditional jumps
                                # otherwise if its a regular move we want to just move and then minimise for the next player
                                if (self.gameBoard.is_jump(i, j, posRow, posCol)):

                                    # Tracks which jumps have been taken
                                    moveList = [[posRow, posCol]]
                                    #Increments the depth of the possible moves we are investigating
                                    self.depth += 1
                                    # Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m, max_y, max_x, pos_x, pos_y) = self.jumping_max(
                                        posRow, posCol, moveList, alpha, beta)
                                    #As it exits we reduce the level of depth
                                    self.depth -= 1

                                    # If the value returned wasn't null a move was possible which increased the value of the current position so it is investigated
                                    if (m != None):

                                        # Checks if the jumping max returned move is better then the current stored move
                                        if m > maxv:
                                            #Stores the variables of the move 
                                            maxv = m
                                            my = i
                                            mx = j
                                            px = posRow
                                            py = posCol

                                        # if maxv > beta then we can prune the tree which is done by retunring (we don't look at other values)
                                        if maxv > beta:
                                            moveList.remove([posRow, posCol])
                                            self.gameBoard.player = currentPlayer
                                            return (maxv, my, mx, px, py)

                                        # Raises the value of alpha 
                                        if maxv > alpha:
                                            alpha = maxv

                                    # remove move from list after completion so it doesn't affect jumping max for next move
                                    moveList.remove([posRow, posCol])

                                #The move is a regular move not a jump 
                                else:
                                    #Perform the move 
                                    (tempRow, tempCol) = self.gameBoard.move(
                                        i, j, posRow, posCol)
                                    
                                    # Evaluate the position only if the move produced a higher rated position
                                    if (self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard) > currentValue):
                                        #save the current position as the best best value
                                        currentValue = self.evaluator.evaluatePosition(
                                            self.gameBoard.player, self.gameBoard)
                                        
                                        #progress to the next players turn so min may be called
                                        self.gameBoard.next_Player()
                                        #Tree depth (recursion depth actually) increases
                                        self.depth += 1
                                        #Finds the minimums best move and returns it 
                                        (m, max_y, max_x, pos_x,
                                         pos_y) = self.min(alpha, beta)
                                        # print("min returned", m)
                                        self.depth -= 1
                                        #Evaluates the minimums best move as long as it was not None
                                        if (m != None):
                                            if m > maxv:
                                                maxv = m
                                                my = i
                                                mx = j
                                                px = posRow
                                                py = posCol

                                            if maxv > beta:
                                                self.gameBoard.player = currentPlayer
                                                #If the move was better then stored beta we want to remove the move before returning so we don't double move
                                                self.gameBoard.swap_Piece(
                                                    tempRow, tempCol, posRow, posCol)
                                                #return the value movment and position
                                                return (maxv, my, mx, px, py)

                                            if maxv > alpha:
                                                alpha = maxv

                                        # Swap back to current player
                                        self.gameBoard.player = currentPlayer

                                    # remove move so it doesn't affect checking other moves
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
        
        #No moves where valid is not a compulsury check but helps for trouble shooting if an error pops up
        if (not (validMove)):
            # Swap back to current player
            self.gameBoard.player = currentPlayer

        #In the case that there was a valid move however no valid moves where deemed as increasing the position we still need to move a piece
        # This section takes a random valid move and executes it even if it wasn't the best        
        if(validMove and my==None):
            # if the game hasn't ended cycle through all possible moves
            for posRow in range(0, self.gameBoard.boardHeight):
                for posCol in range(0, self.gameBoard.boardWidth):

                    # It's the max players piece
                    if (self.gameBoard.board[posRow][posCol] == self.maxPlayer):
                        # list of possible movment directions
                        direction = [-1, 0, 1]
                        random.shuffle(direction)

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
                                        moveList, tempRow, tempCol = self.gameBoard.jump(i, j, posRow, posCol, moveList)
                                        self.depth -= 1

                                        maxv = self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard)
                                        my = i
                                        mx = j
                                        px = posRow
                                        py = posCol
                                        self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)
                                        # remove move from list after checking
                                        moveList.remove([posRow, posCol])
                                        break

                                    else:
                                        # Check current position value
                                        (tempRow, tempCol) = self.gameBoard.move(
                                            i, j, posRow, posCol)

                                    
                                        maxv = self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard)
                                        my = i
                                        mx = j
                                        px = posRow
                                        py = posCol

                                        self.gameBoard.player = currentPlayer

                                        # remove move
                                        self.gameBoard.swap_Piece(
                                            tempRow, tempCol, posRow, posCol)
                                        break

        
        #Finally return the value movement and positon of the maximum move
        # print("position evaluation",self.evaluator.evaluatePosition(self.gameBoard.player, self.gameBoard))
        return (maxv, my, mx, px, py)

    # maximises the jumping cycle
    def jumping_max(self, posRow, posCol, moveList, alpha, beta):
        # print("Jumping Max", alpha, beta)
        if (self.depth > 3):
            return (-2,None,None,None,None)

        maxv = -2
        mx = None
        my = None
        px = None
        py = None

        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                return (self.maxValue, 0, 0, 0, 0)
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

                            if maxv > beta:
                                # print("jumpingmaxv>beta")
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

                            if maxv > beta:
                                # Swap back to current player
                                self.gameBoard.player = currentPlayer
                                self.gameBoard.swap_Piece(
                                    tempRow, tempCol, posRow, posCol)
                                # print("jumpingmaxv>beta")

                                return (maxv, my, mx, px, py)

                            if maxv > alpha:
                                alpha = maxv

                        # Swap back to current player
                        self.gameBoard.player = currentPlayer

                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
           # Swap back to current player
            self.gameBoard.player = currentPlayer
            maxv=self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)

            # maxv=self.evaluator.evaluatePosition(
            # self.gameBoard.player, self.gameBoard)
        

        # print("returning from jumping max with :", maxv, my, mx, px, py)
        return (maxv, my, mx, px, py)

    def min(self, alpha, beta):
        if (self.depth > 3):
            return (self.maxValue+2,None,None,None,None)
        # print("Min", alpha, beta)

        # possible values
        # 1 player 1 wins 2 player 2 wins
        minv = self.maxValue+2
        mx = None
        my = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                # print("end 16")
                return (self.maxValue, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                # print("end 0")
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
                                    # print("Caling jumping min with beta=", beta)
                                    # Minimizes jumping (Minmising occurs inside the jumping_min)
                                    self.depth += 1
                                    (m, min_y, min_x, pos_x, pos_y) = self.jumping_min(
                                        posRow, posCol, moveList, alpha, beta)
                                    self.depth -= 1

                                    if (m != None):
                                        # print("m:", m, "minv:", minv)
                                        # print(posCol, posRow)
                                        # Checks if we have a better move and set it
                                        if m < minv:
                                            minv = m
                                            my = i
                                            mx = j
                                            px = posCol
                                            py = posRow

                                        if minv < alpha:
                                            # print("min returned cause <= alpha")
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
                                                    # print("m:", m)
                                                    # print("alpha", alpha)
                                                    # print("beta", beta)
                                                    minv = m
                                                    my = i
                                                    mx = j
                                                    px = posCol
                                                    py = posRow

                                                if minv < alpha:

                                                    # print(alpha, beta)
                                                    # Swap back to current player
                                                    self.gameBoard.player = currentPlayer
                                                    self.gameBoard.swap_Piece(
                                                        tempRow, tempCol, posRow, posCol)
                                                    # print("minv<beta in min")
                                                    # print(minv, my, mx, py, px)
                                                    return (minv, my, mx, px, py)

                                                if minv < beta:
                                                    beta = minv

                                            # Swap back to current player
                                            self.gameBoard.player = currentPlayer
                                        else:
                                            # print(
                                            #     "caling max with alpha beta =", alpha, beta)
                                            self.depth += 1

                                            (m, max_y, max_x, pos_x,
                                             pos_y) = self.max(alpha, beta)
                                            self.depth -= 1

                                            if (m != None):
                                                if m < minv:
                                                    # print("m:", m)
                                                    # print("alpha", alpha)
                                                    # print("beta", beta)
                                                    minv = m
                                                    my = i
                                                    mx = j
                                                    px = posCol
                                                    py = posRow

                                                if minv < alpha:
                                                    # print(alpha, beta)
                                                    # Swap back to current player
                                                    self.gameBoard.player = currentPlayer
                                                    self.gameBoard.swap_Piece(
                                                        tempRow, tempCol, posRow, posCol)
                                                    # print("minv<beta in min")
                                                    # print(minv, my, mx, py, px)
                                                    return (minv, my, mx, px, py)

                                                if minv < beta:
                                                    beta = minv

                                            # Swap back to current player
                                            self.gameBoard.player = currentPlayer

                                        # remove move
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            # print(self.gameBoard.player)
            # Swap back to current player
            self.gameBoard.player = currentPlayer
            # No valid move so return worst case for parent
            # There where no valid moves so the current move is deemed as one better then not moving
        return (minv, my, mx, px, py)

    def jumping_min(self, posRow, posCol, moveList, alpha, beta):
        if (self.depth > 3):
            return (self.maxValue+2,None,None,None,None)

        # print("Jumping Min", alpha, beta)

        # possible values
        # 1 player 1 wins 2 player 2 wins

        minv = self.maxValue+2
        my = None
        mx = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        if (result != None):
            # Player 1 wins
            if (result == 1):
                # print("end 16")
                return (self.maxValue, 0, 0, 0, 0)
            # The other player wins
            elif (result > 1):
                # print("end 0")
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
                    # print("Jump is valid for the move ",
                    #       i, j, posRow, posCol, moveList)
                    # Stores the new move position
                    moveList, tempRow, tempCol = self.gameBoard.jump(
                        i, j, posRow, posCol, moveList)
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

                            if minv < alpha:
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
                                    # print("m:", m)
                                    # print("alpha", alpha)
                                    # print("beta", beta)
                                    minv = m
                                    my = i
                                    mx = j
                                    px = posCol
                                    py = posRow

                                if minv < alpha:

                                    # print(alpha, beta)
                                    # Swap back to current player
                                    self.gameBoard.player = currentPlayer
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    # print("minv<beta in min")
                                    # print(minv, my, mx, py, px)
                                    return (minv, my, mx, px, py)

                                if minv < beta:
                                    beta = minv

                            # Swap back to current player
                            self.gameBoard.player = currentPlayer

                        # If the next player is the max player max again
                        else:
                            # print(
                            #     "caling max with alpha beta =", alpha, beta)
                            self.depth += 1

                            (m, max_y, max_x, pos_x,
                                pos_y) = self.max(alpha, beta)
                            self.depth -= 1

                            if (m != None):
                                if m < minv:
                                    # print("m:", m)
                                    # print("alpha", alpha)
                                    # print("beta", beta)
                                    minv = m
                                    my = i
                                    mx = j
                                    px = posCol
                                    py = posRow

                                if minv < alpha:

                                    # print(alpha, beta)
                                    # Swap back to current player
                                    self.gameBoard.player = currentPlayer
                                    self.gameBoard.swap_Piece(
                                        tempRow, tempCol, posRow, posCol)
                                    # print("minv<beta in min")
                                    # print(minv, my, mx, py, px)

                                    return (minv, my, mx, px, py)

                                if minv < beta:
                                    beta = minv

                            # Swap back to current player
                        self.gameBoard.player = currentPlayer
                    # print("Un swapping")
                    self.gameBoard.swap_Piece(tempRow, tempCol, posRow, posCol)

        if (not (validMove)):
            # Swap back to current player
            self.gameBoard.player = currentPlayer
            minv=self.evaluator.evaluatePosition(
                self.gameBoard.player, self.gameBoard)
            # No valid move so return worst case for parent
            # minv = self.evaluator.evaluatePosition(self.gameBoard.player,self.gameBoard)
            # minv=self.evaluator.evaluatePosition(
            # self.gameBoard.player, self.gameBoard)

        return (minv, mx, my, px, py)
