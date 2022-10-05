
# Note UP and DOWN are INVERTED but not left and right when moving things on the board using [row][col] ie row-1 moves a piece up one not down one
class board:

    def __init__(self):
        self.boardSetUp()

    def boardSetUp(self):
        # self.board = [['x','x','x','R','x','x','x',],['x','x','R',' ','.','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','.',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]
        self.board = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
        self.mode="small"
        self.player = 'R'
        self.turn = 1
        self.boardWidth = len(self.board[0])
        self.boardHeight = len(self.board)
        print(len(self.board[0]))
        print(len(self.board))

    def display(self):
        for i in range(0, self.boardHeight):
            print(i," " , end = '')
            for j in range(0, self.boardWidth):
                print('{} '.format(self.board[i][j]), end=" ")
            print()
        print("   ",end='')
        for j in range(0, self.boardWidth):
            print(j, " ", end='')
        print(" ")
        
        print(" ")

    def swap_board(self,mode):
        if(mode.__contains__("small")):
            self.board = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', '.', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
            self.mode=mode
            self.boardWidth = len(self.board[0])
            self.boardHeight = len(self.board)
        elif(mode.__contains__("small two")):
            self.board = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', '.', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', '.', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
            self.mode=mode
            self.boardWidth = len(self.board[0])
            self.boardHeight = len(self.board)
            
        elif(mode.__contains__("small full")):
            self.board = [['x', 'x', 'x', 'R', 'x', 'x', 'x', ], ['x', 'x', 'R', ' ', 'R', 'x', 'x', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], [
            '.', ' ', '.', ' ', '.', ' ', '.', ], ['x', '.', ' ', '.', ' ', '.', 'x', ], ['x', 'x', 'B', ' ', 'B', 'x', 'x', ], ['x', 'x', 'x', 'B', 'x', 'x', 'x', ]]
            self.mode=mode
            self.boardWidth = len(self.board[0])
            self.boardHeight = len(self.board)
        elif(mode.__contains__("full")):
            self.board =[  
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'R', ' ', 'R', ' ', 'R', ' ', 'R', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['Y', ' ', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', ' ', 'G'],
            ['x', 'Y', ' ', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', ' ', 'G', 'x'],
            ['x', 'x', 'Y', ' ', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', ' ', 'G', 'x', 'x'],
            ['x', 'x', 'x', 'Y', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'G', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', 'x', 'x', 'x'],
            ['x', 'x', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', 'x', 'x'],
            ['x', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', 'x'],
            ['O', ' ', 'O', ' ', 'O', ' ', 'O', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', '.', ' ', 'P', ' ', 'P', ' ', 'P', ' ', 'P'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', ' ', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'B', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
            self.mode=mode
            self.boardWidth = len(self.board[0])
            self.boardHeight = len(self.board)

    # Evaluates the current postion for the active player
    def position_evaluator(self):
        postionValue = 0
        for i in range(0, self.boardHeight):
            for j in range(0, self.boardWidth):
                if (self.board[i][j] == self.player):
                    postionValue += i
        return postionValue

    def is_current_players_piece(self, posRow, posCol):
        '''
        Checks if the location has a piece controlled by the current player
        '''
        if (posRow > self.boardHeight-1 or posRow < 0 or posCol > self.boardWidth-1 or posCol < 0):
            return False

        if (self.board[posRow][posCol] == self.player):
            return True
        else:
            return False

    # Checks if a move is a jump
    def is_jump(self, upOrDown, leftOrRight, posRow, posCol):
        # jump down left
        if upOrDown < 0 and leftOrRight < 0:
            if (self.contains_piece(posRow+1, posCol-1)):
                if not (self.is_clear(posRow+2, posCol-2)):
                    # space not clear or move is in movelist
                    return False
                else:
                    # jump possible
                    return True

        # moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if (self.contains_piece(posRow+1, posCol+1)):
                # Check for empty spot after adjacent piece
                if not (self.is_clear(posRow+2, posCol+2)):
                    return False
                else:
                    return True

        # moving up left
        if upOrDown > 0 and leftOrRight < 0:
            if (self.contains_piece(posRow-1, posCol-1)):
                # Check for empty spot after adjacent piece
                if not (self.is_clear(posRow-2, posCol-2)):
                    return False
                else:
                    return True

        # moving up right
        if upOrDown > 0 and leftOrRight > 0:
            if (self.contains_piece(posRow-1, posCol+1)):

                # Check for empty spot after adjacent piece
                if not (self.is_clear(posRow-2, posCol+2)):
                    return False
                else:
                    return True

        # moving left
        if upOrDown == 0 and leftOrRight < 0:
            if (self.contains_piece(posRow, posCol-2)):
                # Check for empty spot after adjacent piece
                if not (self.is_clear(posRow, posCol-4)):
                    return False
                else:
                    return True

        # moving right
        if (upOrDown == 0 and leftOrRight > 0):
            # check for adjacent piece
            if (self.contains_piece(posRow, posCol+2)):
                # Check for empty spot after adjacent piece
                if (not (self.is_clear(posRow, posCol+4))):
                    return False
                else:
                    return True
        if (upOrDown == 0 and leftOrRight == 0):
            return False

    # returns False if jump is invalid otherwise returns position
    def is_jump_valid(self, upOrDown, leftOrRight, posRow, posCol, moveList):
        ''''
        Returns true if the selected piece is able to jump in the inputed direction 
        Move list contains all previous jumps preformed by the piece
        '''
        # Check if the piece is in the end zone done
        # Check if the piece is moving out of the end zone done
        # Check if the piece is moving to the end zone

        # jump down left
        if upOrDown < 0 and leftOrRight < 0:
            # Can we jump
            if (self.contains_piece(posRow+1, posCol-1)):

                # Condition if it's leaving the end zone normal rules apply if its in the end zone end zone applys
                if (self.is_end_or_start_zone(posRow+2, posCol-2)):
                    # Not leaving the end zone ensure the piece is not swaping with same team piece
                    if (self.is_in_bound(posRow+2, posCol-2) and not (self.is_current_players_piece(posRow+2, posCol-2)) and not ([posRow + 2, posCol-2] in (moveList))):
                        return True
                    else:
                        return False
                else:
                    # Check for empty spot after adjacent piece
                    if (self.is_clear(posRow+2, posCol-2) and not ([posRow + 2, posCol-2] in (moveList))):
                        return True
                    else:
                        return False

        # moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if (self.contains_piece(posRow+1, posCol+1)):
                if (self.is_end_or_start_zone(posRow+2, posCol-2)):
                    # Check for empty spot after adjacent piece
                    if not (self.is_in_bound(posRow+2, posCol+2) and not (self.is_current_players_piece(posRow+2, posCol+2)) and not ([posRow+2, posCol+2] in (moveList))):
                        return False
                    else:
                        return True
                else:
                    if not (self.is_clear(posRow+2, posCol+2) and not ([posRow+2, posCol+2] in (moveList))):
                        return False
                    else:
                        return True

        # moving up left
        if upOrDown > 0 and leftOrRight < 0:
            if (self.contains_piece(posRow-1, posCol-1)):
                if (self.is_end_or_start_zone(posRow-2, posCol-2)):
                    # Check for empty spot after adjacent piece
                    if not (self.is_in_bound(posRow-2, posCol-2) and not (self.is_current_players_piece(posRow-2, posCol-2)) and not ([posRow-2, posCol-2] in (moveList))):
                        return False
                    else:
                        return True
                else:
                    if not (self.is_clear(posRow-2, posCol-2) and not ([posRow-2, posCol-2] in (moveList))):
                        return False
                    else:
                        return True

        # moving up right
        if upOrDown > 0 and leftOrRight > 0:
            if (self.contains_piece(posRow-1, posCol+1)):
                if (self.is_end_or_start_zone(posRow-2, posCol+2)):
                    # Check for empty spot after adjacent piece
                    if not (self.is_in_bound(posRow-2, posCol+2) and not (self.is_current_players_piece(posRow-2, posCol+2)) and not ([posRow-2, posCol+2] in (moveList))):
                        return False
                    else:
                        return True
                else:
                    if not (self.is_clear(posRow-2, posCol+2) and not ([posRow-2, posCol+2] in (moveList))):
                        return False
                    else:
                        return True

        # moving left
        if upOrDown == 0 and leftOrRight < 0:
            if (self.contains_piece(posRow, posCol-2)):
                if (self.is_end_or_start_zone(posRow, posCol-4)):
                    # Check for empty spot after adjacent piece
                    if not (self.is_in_bound(posRow, posCol-4) and not (self.is_current_players_piece(posRow, posCol-4)) and not ([posRow, posCol-4] in (moveList))):
                        return False
                    else:
                        return True
                else:
                    if not (self.is_clear(posRow, posCol-4) and not ([posRow, posCol-4] in (moveList))):
                        return False
                    else:
                        return True

        # moving right
        if (upOrDown == 0 and leftOrRight > 0):
            if (self.contains_piece(posRow, posCol+2)):
                if (self.is_end_or_start_zone(posRow, posCol+4)):
                    # Check for empty spot after adjacent piece
                    if not (self.is_in_bound(posRow, posCol+4) and not (self.is_current_players_piece(posRow, posCol+4)) and not ([posRow, posCol+4] in (moveList))):
                        return False
                    else:
                        return True
                else:
                    if not (self.is_clear(posRow, posCol+4) and not ([posRow, posCol+4] in (moveList))):
                        return False
                    else:
                        return True

        if (upOrDown == 0 and leftOrRight == 0):
            return False

        # not a valid jump
        return False

    def is_end_or_start_zone(self, posRow, posCol):
        '''
        Returns true if the selected co-ordinates is in the current players end zone or start zone
        '''

        # red end zone
        if (self.player == 'R'):
            if (posRow < 2 and posCol > 1 and posCol < 5):
                return True
            elif (posRow > 4 and posCol > 1 and posCol < 5):
                return True
            return False
        # blue end zone
        elif (self.player == 'B'):
            if (posRow < 2 and posCol > 1 and posCol < 5):
                return True
            elif (posRow > 4 and posCol > 1 and posCol < 5):
                return True
            return False

        return False

    # checks the game has ended

    def is_end(self):
        '''Returns True if the board is in the end state for the current player'''
        print("mode=",self.mode)
        if(self.mode.__contains__("small")):
            if (self.board[0][3] == 'B'):
                return 4
            elif(self.board[6][3]=='R'):
                return 1
        elif(self.mode.__contains__("small two")):
            if (self.board[0][3] == 'B' and (self.board[1][2] == 'B' or self.board[1][4] == 'B')):
                return 4
            elif(self.board[6][3]=='R' and (self.board[5][2]=='R' or self.board[5][4]=='R')):
                return 1
        elif(self.mode.__contains__("small full")):
            if (self.board[0][3] == 'B' and self.board[1][2] == 'B' and self.board[1][4] == 'B'):
                return 4
            elif(self.board[6][3]=='R' and self.board[5][2]=='R' and self.board[5][4]=='R'):
                return 1
        elif(self.mode.__contains__("full")):
            print("checking full")

            #Red victory
            victory=True
            rows = [[0],[1],[0,2],[1,3]]
            for i in range(0,4):
                for j in rows[i]:
                    if(self.board[13+i][12-j]!='R' and self.board[13+i][12+j]!='R'):
                        victory=False
                        break
            if(victory):
                return 1

            #Green Victory
            victory=True
            for i in range(0,4):
                for j in rows[i]:
                    if(self.board[i+9][3-j]!='G' and self.board[i+9][3+j]!='G'):
                        victory=False
                        break
            
            if(victory):
                return 2

            #Green Victory
            victory=True
            for i in range(0,4):
                for j in rows[i]:
                    if(self.board[7-i][3-j]!='P' and self.board[7-i][3+j]!='P'):
                        victory=False
                        break
            
            if(victory):
                return 3

            

            #Blue victory
            victory=True
            for i in range(0,4):
                for j in rows[i]:
                    if(self.board[i][12-i]!='B' and self.board[i][12+i]!='B'):
                        victory=False
                        break
            if(victory):
                return 4
            
            

            #Orange Victory
            victory=True
            print("Here")
            self.display()
            for i in range(0,4):
                for j in rows[i]:
                    print(self.board[7-i][21-j]!='O')
                    if(self.board[7-i][21-j]!='O' and self.board[7-i][21+j]!='O'):
                       
                        print(self.board[7-i][21-j], i,j)
                        print("HERE")
                        victory=False
                        break
            if(victory):
                return 5

            #Yellow Victory
            victory=True
            for i in range(0,4):
                for j in rows[i]:
                    if(self.board[9+i][21-j]!='Y' and self.board[9+i][21+j]!='Y'):
                        victory=False
                        break
            
            if(victory):
                return 6
            


        # if(self.board[0][3]=='B' and self.board[0][2]=='B' and self.board[0][4]=='B'):
        #     return 2
        
        # elif (self.board[6][3] == 'R'):
        #     return 1
        # if(self.board[6][3]=='R' and self.board[5][2]=='R' and self.board[5][4]=='R'):
        #     return 1
        # elif(self.board[0][3]=='B' and self.board[0][2]=='B' and self.board[0][4]=='B'):
        #     return 2
        return None

    def is_in_bound(self, row, col):
        '''
        Checks a location on the board is in the playing field returning true
        '''
        # Out of board range
        if (row > self.boardHeight-1 or row < 0 or col > self.boardWidth-1 or col < 0):
            return False
        if (self.board[row][col] != 'x'):
            return True
        else:
            return False

    def is_clear(self, row, col):
        '''
        Checks location:[row],[col] on the board.
        If it is in bounds and contains '.' return true
        else return false
        '''
        # Out of board range
        if (row > self.boardHeight-1 or row < 0 or col > self.boardWidth-1 or col < 0):
            return False

        if (self.board[row][col] == '.'):
            return True
        else:
            return False

    # Checks a location on the board for a piece false it does not contain a piece true it does
    def contains_piece(self, row, col):
        if (row > self.boardHeight-1 or row < 0 or col > self.boardWidth-1 or col < 0):
            # print("no piece as board is out of range")
            return False

        if self.board[row][col] != "x" and self.board[row][col] != " " and self.board[row][col] != ".":
            # contains a piece
            return True
        else:
            # contains something else
            return False

    def swap_Player(self):
        if (self.player == 'R'):
            self.player = 'B'
        else:
            self.player = 'R'

    # Moves a piece one space
    def move(self, upOrDown, leftOrRight, posRow, posCol):
        # moving down left
        if upOrDown < 0 and leftOrRight < 0:
            self.swap_Piece(posRow+1, posCol-1, posRow, posCol)
            return (posRow+1, posCol-1)
        # moving down right
        if upOrDown < 0 and leftOrRight > 0:
            self.swap_Piece(posRow+1, posCol+1, posRow, posCol)
            return (posRow+1, posCol+1)
        # moving up left
        if upOrDown > 0 and leftOrRight < 0:
            self.swap_Piece(posRow-1, posCol-1, posRow, posCol)
            return (posRow-1, posCol-1)
        # moving up right
        if upOrDown > 0 and leftOrRight > 0:
            self.swap_Piece(posRow-1, posCol+1, posRow, posCol)
            return (posRow-1, posCol+1)
        # moving left
        if upOrDown == 0 and leftOrRight < 0:
            self.swap_Piece(posRow, posCol-2, posRow, posCol)
            return (posRow, posCol-2)
        # moving right
        if (upOrDown == 0 and leftOrRight > 0):
            self.swap_Piece(posRow, posCol+2, posRow, posCol)
            return (posRow, posCol+2)

    def jump(self, upOrDown, leftOrRight, posRow, posCol, moveList):

        # moving down left
        if upOrDown < 0 and leftOrRight < 0:
            moveList.append([posRow+2, posCol-2])
            self.swap_Piece(posRow+2, posCol-2, posRow, posCol)
            return (moveList, posRow+2, posCol-2)
        # moving down right
        if upOrDown < 0 and leftOrRight > 0:
            moveList.append([posRow-2, posCol+2])
            self.swap_Piece(posRow+2, posCol+2, posRow, posCol)
            return (moveList, posRow+2, posCol+2)
        # moving up left
        if upOrDown > 0 and leftOrRight < 0:
            moveList.append([posRow-2, posCol-2])
            self.swap_Piece(posRow-2, posCol-2, posRow, posCol)
            return (moveList, posRow-2, posCol-2)
        # moving up right
        if upOrDown > 0 and leftOrRight > 0:
            moveList.append([posRow-2, posCol+2])
            self.swap_Piece(posRow-2, posCol+2, posRow, posCol)
            return (moveList, posRow-2, posCol+2)
        # moving left
        if upOrDown == 0 and leftOrRight < 0:
            moveList.append([posRow, posCol-4])
            self.swap_Piece(posRow, posCol-4, posRow, posCol)
            return (moveList, posRow, posCol-4)
        # moving right
        if (upOrDown == 0 and leftOrRight > 0):
            moveList.append([posRow, posCol+4])
            self.swap_Piece(posRow, posCol+4, posRow, posCol)
            return (moveList, posRow, posCol+4)

    def swap_Piece(self, moveRow, moveCol, posRow, posCol):
        # print("swapping [",moveRow,"][",moveCol,"] with [",posRow,"][",posCol,"]")
        temp = self.board[posRow][posCol]
        self.board[posRow][posCol] = self.board[moveRow][moveCol]
        self.board[moveRow][moveCol] = temp

    def is_move_valid(self, upOrDown, leftOrRight, posRow, posCol):
        '''
        Checks if a move is possible returning true if it is '''
        # Checks the piece belongs to the current player
        if (not (self.is_current_players_piece)):
            return False

        # Checks the position being retrieved is in bounds and the movement will be in bounds
        if posRow == 7 and upOrDown < 0 or posRow == 0 and upOrDown > 0 or posCol == 7 and leftOrRight > 0 or posCol == 0 and leftOrRight < 0:
            return False

        # Steps moving down to the left
        # Is it in the end zone
        # If yes end zone conditions
        # if no normal
        # moving down left
        if upOrDown < 0 and leftOrRight < 0:
            # if moving into end zone handle
            if (self.is_end_or_start_zone(posRow+1, posCol-1)):
                if (self.contains_piece(posRow+1, posCol-1)):

                    if (self.is_in_bound(posRow+2, posCol-2) and not (self.is_current_players_piece(posRow+2, posCol-2))):
                        return True
                    elif (not (self.is_current_players_piece(posRow+1, posCol-1))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow+1, posCol-1)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow+1, posCol-1)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow+2, posCol-2)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow+1, posCol-1)):
                    return True
                else:
                    return False

        # moving down right
        if upOrDown < 0 and leftOrRight > 0:
            # if moving into end zone handle
            if (self.is_end_or_start_zone(posRow + 1, posCol + 1)):
                if (self.contains_piece(posRow + 1, posCol + 1)):

                    if (self.is_in_bound(posRow + 2, posCol + 2) and not (self.is_current_players_piece(posRow + 2, posCol + 2))):
                        return True
                    elif (not (self.is_current_players_piece(posRow + 1, posCol + 1))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow + 1, posCol + 1)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow + 1, posCol + 1)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow + 2, posCol + 2)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow + 1, posCol + 1)):
                    return True
                else:
                    return False

        # moving up left
        if upOrDown > 0 and leftOrRight < 0:
            # if moving into end zone handle
            if (self.is_end_or_start_zone(posRow - 1, posCol - 1)):
                if (self.contains_piece(posRow - 1, posCol - 1)):

                    if (self.is_in_bound(posRow - 2, posCol - 2) and not (self.is_current_players_piece(posRow - 2, posCol - 2))):
                        return True
                    elif (not (self.is_current_players_piece(posRow - 1, posCol - 1))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow - 1, posCol - 1)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow - 1, posCol - 1)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow - 2, posCol - 2)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow - 1, posCol - 1)):
                    return True
                else:
                    return False

        # moving up right
        if upOrDown > 0 and leftOrRight > 0:
            # if moving into end zone handle
            if (self.is_end_or_start_zone(posRow - 1, posCol + 1)):
                if (self.contains_piece(posRow - 1, posCol + 1)):

                    if (self.is_in_bound(posRow - 2, posCol + 2) and not (self.is_current_players_piece(posRow - 2, posCol + 2))):
                        return True
                    elif (not (self.is_current_players_piece(posRow - 1, posCol + 1))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow - 1, posCol + 1)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow - 1, posCol + 1)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow - 2, posCol + 2)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow - 1, posCol + 1)):
                    return True
                else:
                    return False

         # moving left
        if upOrDown == 0 and leftOrRight < 0:
            # if moving into end zone handle
            if (self.is_end_or_start_zone(posRow, posCol - 2)):
                if (self.contains_piece(posRow, posCol - 2)):

                    if (self.is_in_bound(posRow, posCol - 4) and not (self.is_current_players_piece(posRow, posCol - 4))):
                        return True
                    elif (not (self.is_current_players_piece(posRow, posCol - 2))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow, posCol - 2)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow, posCol - 2)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow, posCol - 4)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow, posCol - 2)):
                    return True
                else:
                    return False

        # moving right
        if upOrDown == 0 and leftOrRight > 0:
            if (self.is_end_or_start_zone(posRow, posCol + 2)):
                if (self.contains_piece(posRow, posCol + 2)):

                    if (self.is_in_bound(posRow, posCol + 4) and not (self.is_current_players_piece(posRow, posCol + 4))):
                        return True
                    elif (not (self.is_current_players_piece(posRow, posCol + 2))):
                        return True
                    else:
                        return False
                else:
                    if (self.is_clear(posRow, posCol + 2)):
                        return True
                    return False

            # check for adjacent piece
            elif (self.contains_piece(posRow, posCol + 2)):
                # Check for empty spot after adjacent piece
                if (self.is_clear(posRow, posCol + 4)):

                    return True
                else:
                    return False
            else:
                if (self.is_clear(posRow, posCol + 2)):
                    return True
                else:
                    return False

        else:
            return False

    def human_jump(self, posRow, posCol):
        continueJumping = True
        moveList = []
        while (continueJumping):

            self.display()
            print("Would you like to continue jumping?")
            anwser = input('Yes or No?: ')
            # Take user input
            if (anwser.__contains__("Yes")):
                moveRow = int(
                    input('Move up is 1 move down is -1 still is 0: '))
                moveCol = int(
                    input('Move right is 1 move left is -1 still is 0: '))

                # No move list as a human should be able to infinit loop if they want to waste time.
                if (self.is_jump_valid(moveRow, moveCol, posRow, posCol, moveList)):
                    moveList, tempRow, tempCol = self.jump(
                        moveRow, moveCol, posRow, posCol, moveList)
                    print(tempRow)
                    print(tempCol)
                    posRow = tempRow
                    posCol = tempCol
                else:
                    print("Selected jump is not valid")

            elif (anwser.__contains__("No")):
                continueJumping = False

    def select_Move(self, posRow, posCol):

        print("Where would you like to move")
        # Take user input
        moveRow = int(input('Move up is 1 move down is -1 still is 0: '))
        moveCol = int(input('Move right is 1 move left is -1 still is 0: '))
        moveList = []

        # Check that the move is possible
        if (self.is_move_valid(moveRow, moveCol, posRow, posCol)):
            if (self.is_jump_valid(moveRow, moveCol, posRow, posCol, moveList)):
                (moveList, tempRow, tempCol) = self.jump(
                    moveRow, moveCol, posRow, posCol, moveList)
                self.human_jump(tempRow, tempCol)
                self.swap_Player()
            else:
                self.move(moveRow, moveCol, posRow, posCol)
                self.swap_Player()

        else:
            print("Not a valid move")

    def select_piece(self):

        print("Select a piece")
        # Take user input
        posRow = int(input('Insert the Y coordinate: '))
        posCol = int(input('Insert the X coordinate: '))

        # Check it contains a piece
        if (self.contains_piece(posRow, posCol)):
            self.select_Move(posRow, posCol)
        else:
            print("Invalid selection please select a ", self.player, " piece")

    # Ends a test

    def end_test(self):
        self.board[6][3] = 'R'
        self.board[5][2] = 'R'
        self.board[5][4] = 'R'

    def play(self):
        while (not (self.is_end())):
            currentPlayer = self.player

            while (currentPlayer == self.player):
                self.display()
                self.select_piece()
