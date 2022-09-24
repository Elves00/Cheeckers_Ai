from pickle import FALSE
from re import M
from turtle import left, up

'''
                                So theres a lot going on if you make a jump it kinda restarts the turn so you need to create
                                a jumping max to then maximise that jump or the next jump afterwards. Each jump then needs to cal min once
                                it finishes jumping.

                                The reverse will be come true for min where min will have a jump chain with jumping_min and min functions which
                                call max after it finishes jumping.

                                To acomplish this a few functions have been added move which performs a move a returns the new position of the moved piece
                                And jump whihc does the same thing but for jump

                                There is also a new function for checking a jump is valid which returns true or false only whihc is seprate to the palyer input one
                                

                                To do tests in python  

                                def test_sum():
                                    assert sum([1,2,3]) == 6 "should be 6"
                                
                                if __name__ == "__main__":
                                    test_sum()
                                    print("everything passed")
                                '''



#Note UP and DOWN are INVERTED but not left and right when moving things on the board using [row][col] ie row-1 moves a piece up one not down one
class board:
    

    def __init__(self):
        self.boardSetUp()

    def boardSetUp(self):
        self.board = [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','.',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]
        self.player = 'R'
    def display(self):
        for i in range(0,7):
            for j in range(0,7):
                print('{} '.format(self.board[i][j]), end= " ")
            print()
        print()
    
    #maximiser
    def max(self):
        

        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        maxv = -2
        px = None
        py = None
        result = self.is_end

        #Player 1 wins
        if(result == 1):
            return (1,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0)

        #if the game hasn't ended cycle through all possible moves
        for posRow in range(0,6):
            for posCol in range (0,6):
                #It's the max players piece
                if(self.board[posRow][posCol]=='R'):
                    #list of possible movment directions
                    direction = [1,0,-1]
                    #cycle all move directions
                    for upOrDown in direction:
                        for leftOrRight in direction:
                            #if the move is valid
                            if(self.is_move_possible(upOrDown,leftOrRight,posRow,posCol)):
                                #Check if the move being attempted is a jump
                                if(self.is_jump(upOrDown,leftOrRight,posRow,posCol)):
                                    print("jump")
                                    #Tracks moves taken
                                    moveList = [[posRow,posCol]]
                                    #Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m,max_y,max_x)=self.jumping_max(posRow,posCol,moveList)
                                    #Checks if we have a better move and set it 
                                    if m > maxv:
                                        maxv=m
                                        py=upOrDown
                                        px=leftOrRight
                                    #remove move from list after checking
                                    moveList.remove([posRow,posCol])
                                else:
                                    print("move")
                                    (tempRow,tempCol)=self.move(upOrDown,leftOrRight,posRow,posCol)

                                    #Call min
                                    self.min()
                                    #remove move
                                    self.swap_Piece(tempRow,tempCol,posRow,posCol)
                                
        return (maxv,px,py)
    
    #maximises the jumping cycle
    def jumping_max(self,posRow,posCol,moveList):
        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        maxv = -2
        px = None
        py = None
        result = self.is_end()

        #Player 1 wins
        if(result == 1):
            return (1,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0)

        #Posible directions a piece can move
        direction =[1,0,-1]

        #For all directions in x and y
        for i in direction:
            for j in direction:
                #Check if there is a valid jump and explore it 
                if(self.is_jump_valid(i,j,posRow,posCol,moveList)):
                    #Stores the new move position
                    tempRow,tempCol=self.jump(i,j,posRow,posCol,moveList)
                    #maximises for the new position
                    (m,max_i,max_j)=self.jumping_max(tempRow,tempCol,moveList)

                    if m > maxv:
                        maxv=m
                        py=i
                        px=j
                    #Move the peice back to previous position
                    self.swap_Piece(tempRow,tempCol,posRow,posCol)

        #if there are no valid moves then we do a minimise
        self.min()

        return (maxv,py,px)

    def min(self):
        print("min")
        self.display()
    def min_jump(self):
        print("minimizing jump")
        
 
              
    #Checks if a move is a jump 
    def is_jump(self,upOrDown,leftOrRight,posRow,posCol):
         #jump down left
        if upOrDown < 0 and leftOrRight < 0:
            if(self.contains_piece(posRow+1,posCol-1)):
                 if not(self.is_clear(posRow+2,posCol-2)):
                    #space not clear or move is in movelist
                    return False
                 else:
                    #jump possible
                    return True
            
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if(self.contains_piece(posRow+1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol+2) ):
                    return False
                 else:
                    return True

        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            if(self.contains_piece(posRow-1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol-2) ):
                    return False
                 else:
                    return True
                

        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            if(self.contains_piece(posRow-1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol+2)):
                    return False
                 else:
                    return True

        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            if(self.contains_piece(posRow,posCol-2)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol-4) ):
                    return False
                 else:
                    return True
                
        
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
             #check for adjacent piece
            if(self.contains_piece(posRow,posCol+2)):
                #Check for empty spot after adjacent piece
                 if (not(self.is_clear(posRow,posCol+4) )):
                    return False
                 else:
                    return True
        if(upOrDown==0 and leftOrRight==0):
            return False

    #returns False if jump is invalid otherwise returns position
    def is_jump_valid(self,upOrDown,leftOrRight,posRow,posCol,moveList):

        #if the jump co-ordinates have not been reached before allowed to jump

        #jump down left
        if upOrDown < 0 and leftOrRight < 0:
            if(self.contains_piece(posRow+1,posCol-1)):
    
                 if not(self.is_clear(posRow+2,posCol-2) and not([posRow + 2,posCol-2]in(moveList))):
                    #space not clear or move is in movelist
                    return False
                 else:
                    #jump possible
                    return (True)
            
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if(self.contains_piece(posRow+1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol+2) and not([posRow+2,posCol+2]in(moveList))):
                    return False
                 else:
                    return True

        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            if(self.contains_piece(posRow-1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol-2) and not([posRow-2,posCol-2]in(moveList))):
                    return False
                 else:
                    return True
                

        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            if(self.contains_piece(posRow-1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol+2) and not([posRow-2,posCol+2]in(moveList))):
                    return False
                 else:
                    return True

        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            if(self.contains_piece(posRow,posCol-2)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol-4) and not([posRow,posCol-4]in(moveList))):
                    return False
                 else:
                    return True
                
        
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
             #check for adjacent piece
            if(self.contains_piece(posRow,posCol+2)):
                #Check for empty spot after adjacent piece
                 if (not(self.is_clear(posRow,posCol+4) and not([posRow,posCol+4]in(moveList)))):
                    return False
                 else:
                    return True
        if(upOrDown==0 and leftOrRight==0):
            return False

    #checks the game has ended
    def is_end(self):

        if(self.board[6][3]=='R' and self.board[5][2]=='R' and self.board[5][4]=='R'):
            return 1
        elif(self.board[0][3]=='B' and self.board[0][2]=='B' and self.board[0][4]=='B'):
            return 2
        return None

    #Checks a location on the board has no piece and is on the board false place is occupied true place is not
    def is_clear(self,row,col):

        #Out of board range 
        if(row>6 or row<0 or col>6 or col<0):
            return False
                   
        if(self.board[row][col] =='.'):
            return True
        else:
            return False

    #Checks a location on the board for a piece false it does not contain a piece true it does
    def contains_piece(self,row,col):
        if(row>6 or row<0 or col>6 or col<0):
            print("no piece as board is out of range")
            return False
        
        if self.board[row][col] != "x" and self.board[row][col] != " " and self.board[row][col] != ".":
            
         return True
        else:
            return False
            

    def swap_Player(self):
        if(self.player=='R'):
            self.player='B'
        else:
            self.player='R'

    #Moves a piece one space
    def move(self,upOrDown,leftOrRight,posRow,posCol):
        #moving down left
        if upOrDown < 0 and leftOrRight < 0:
            self.swap_Piece(posRow+1,posCol+1,posRow,posCol)
            return (posRow+1,posCol+1)
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            self.swap_Piece(posRow+1,posCol-1,posRow,posCol)
            return (posRow+1,posCol-1)
        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            self.swap_Piece(posRow-1,posCol-1,posRow,posCol)
            return (posRow-1,posCol-1)
        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            self.swap_Piece(posRow-1,posCol+1,posRow,posCol)
            return (posRow-1,posCol+1)
        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            self.swap_Piece(posRow,posCol-2,posRow,posCol)
            return (posRow,posCol-2)
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
            self.swap_Piece(posRow,posCol+2,posRow,posCol)
            return (posRow,posCol+2)

    def jump(self,upOrDown,leftOrRight,posRow,posCol,moveList):

        #moving down left
        if upOrDown < 0 and leftOrRight < 0:
            moveList.append([posRow+2,posCol+2])
            self.swap_Piece(posRow+2,posCol+2,posRow,posCol)
            return (posRow+2,posCol+2)
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            moveList.append([posRow+2,posCol-2])
            self.swap_Piece(posRow+2,posCol-2,posRow,posCol)
            return (posRow+2,posCol-2)
        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            moveList.append([posRow-2,posCol-2])
            self.swap_Piece(posRow-2,posCol-2,posRow,posCol)
            return (posRow-2,posCol-2)
        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            moveList.append([posRow-2,posCol+2])
            self.swap_Piece(posRow-2,posCol+2,posRow,posCol)
            return (posRow-2,posCol+2)
        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            moveList.append([posRow,posCol-4])
            self.swap_Piece(posRow,posCol-4,posRow,posCol)
            return (posRow,posCol-4)
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
            moveList.append([posRow,posCol+4])
            self.swap_Piece(posRow,posCol+4,posRow,posCol)
            return (posRow,posCol+4)
        
   

    def swap_Piece(self,moveRow,moveCol,posRow,posCol):
        #Swaps two pieces on a board 
        temp= self.board[posRow][posCol]
        # print("prev:[",posRow,"][",posCol,"]")
        self.board[posRow][posCol]=self.board[moveRow][moveCol]
        self.board[moveRow][moveCol]=temp
        # print("now:[",moveRow,"][",moveCol,"]")

        
    def is_move_possible(self, upOrDown,leftOrRight ,posRow,posCol):
  #Checks the piece belongs to the current player
        if(self.player == 'R' and self.board[posRow][posCol] != 'R'):
            return False
        elif(self.player == 'B' and self.board[posRow][posCol]!='B'):
            return False
      
        if posRow==7 and upOrDown<0 or posRow==0 and upOrDown>0 or posCol==7 and leftOrRight>0 or posCol==0 and leftOrRight<0:
           
            return False

        #moving down left
        if upOrDown < 0 and leftOrRight < 0:
          
            #check for adjacent piece
            if(self.contains_piece(posRow+1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if(self.is_clear(posRow+2,posCol-2)):
                   
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow+2,posCol-2)):
                    return True
                else:
                    return False

        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if(self.contains_piece(posRow+1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if (self.is_clear(posRow+2,posCol+2)):
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow+2,posCol+2)):
                    return True
                else:
                    return False

        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            #check for adjacent piece
            if(self.contains_piece(posRow-1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if(self.is_clear(posRow-2,posCol-2)):
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow-2,posCol-2)):
                    return True
                else:
                    return False
       
        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            #check for adjacent piece
            if(self.contains_piece(posRow-1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if (self.is_clear(posRow-2,posCol+2)):
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow-2,posCol+2)):
                    return True
                else:
                    return False

         #moving left
        if upOrDown == 0 and leftOrRight < 0:
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol-2)):
                #Check for empty spot after adjacent piece
                 if (self.is_clear(posRow,posCol-4)):
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow,posCol-2)):
                    return True
                else:
                    return False

        #moving right
        if upOrDown == 0 and leftOrRight > 0:
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol+2)):
                #Check for empty spot after adjacent piece
                 if(self.is_clear(posRow,posCol+4)):
                    return True
                 else:
                    return False
            else:
                if(self.is_clear(posRow,posCol+2)):
                    return True
                else:
                    return False
        
        else:
            return False

    
    #Checks if a move is possible mx = move to x , px = peice is at x
    def is_move_valid(self, upOrDown,leftOrRight ,posRow,posCol):
        
        #Checks the piece belongs to the current player
        if(self.player == 'R' and self.board[posRow][posCol] != 'R'):
            print("That's not your piece your ",self.player)
            return False
        elif(self.player == 'B' and self.board[posRow][posCol]!='B'):
            print("That's not your piece! your ",self.player)
            return False


        print("posRow=",posRow)
        if posRow==7 and upOrDown<0 or posRow==0 and upOrDown>0 or posCol==7 and leftOrRight>0 or posCol==0 and leftOrRight<0:
            print("Error Moving off board")
            return False

        #moving down left
        if upOrDown < 0 and leftOrRight < 0:
            print("down left")
            #check for adjacent piece
            if(self.contains_piece(posRow+1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol-2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    #Perform first jump
                    self.swap_Piece(posRow+2,posCol-2,posRow,posCol)
                    #Check if player wants to continue jumping and run jumping loop
                    moveList = [[posRow,posCol],[posRow+2,posCol-2]]
                    self.select_jump(posRow+2,posCol-2,moveList)
                    #Player turn over swap players
                    self.swap_Player()
                    return True
            else:
                self.swap_Piece(posRow+1,posCol-1,posRow,posCol)
                #Switches to the next players turn
                self.swap_Player()
                return True

        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            print("down right")
            #check for adjacent piece
            if(self.contains_piece(posRow+1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol+2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow+2,posCol+2,posRow,posCol)
                    moveList = [[posRow,posCol],[posRow+2,posCol+2]]
                    self.select_jump(posRow+2,posCol+2,moveList)
                    self.swap_Player()
                    
                    return True
            else:
                self.swap_Piece(posRow+1,posCol+1,posRow,posCol)
                self.swap_Player()
                return True

        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            print("down left")
            #check for adjacent piece
            if(self.contains_piece(posRow-1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol-2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow-2,posCol-2,posRow,posCol)
                    moveList = [[posRow,posCol],[posRow-2,posCol-2]]
                    self.select_jump(posRow-2,posCol-2,moveList)
                    self.swap_Player()
                    return True
            else:
                self.swap_Piece(posRow-1,posCol-1,posRow,posCol)
                self.swap_Player()
                return True
       
        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            print("down left")
            #check for adjacent piece
            if(self.contains_piece(posRow-1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol+2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow-2,posCol+2,posRow,posCol)
                    moveList = [[posRow,posCol],[posRow-2,posCol+2]]
                    self.select_jump(posRow-2,posCol+2,moveList)
                    self.swap_Player()
                    return True
            else:
                self.swap_Piece(posRow-1,posCol+1,posRow,posCol)
                self.swap_Player()
                return True
         #moving left
        if upOrDown == 0 and leftOrRight < 0:
            print("left")
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol-2)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol-4)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    print("jumping left ")
                    self.swap_Piece(posRow,posCol-4,posRow,posCol)
                    moveList = [[posRow,posCol],[posRow,posCol-4]]
                    self.select_jump(posRow,posCol-4,moveList)
                    self.swap_Player()
                    return True
            else:
                print("moving left")
                self.swap_Piece(posRow,posCol-2,posRow,posCol)
                self.swap_Player()
                return True

        #moving right
        if upOrDown == 0 and leftOrRight > 0:
            print("moving right")
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol+2)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol+4)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow,posCol+4,posRow,posCol)
                    moveList = [[posRow,posCol],[posRow,posCol+4]]
                    self.select_jump(posRow,posCol+4,moveList)
                    self.swap_Player()
                    return True
            else:
                self.swap_Piece(posRow,posCol+2,posRow,posCol)
                self.swap_Player()
                return True
        
        else:
            print("Check conditions we shouldn't reach here")

    def is_jump_possible(self,upOrDown,leftOrRight,posRow,posCol,moveList):

        #check a jump is possible
        print("checking jump")

        #if the jump co-ordinates have not been reached before allowed to jump

        #jump down left
        if upOrDown < 0 and leftOrRight < 0:
            if(self.contains_piece(posRow+1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol-2) and not([posRow + 2,posCol-2]in(moveList))):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow+2,posCol-2,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow+2,posCol-2,moveList)
                    
                    return True
            
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            if(self.contains_piece(posRow+1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow+2,posCol+2) and not([posRow+2,posCol+2]in(moveList))):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow+2,posCol+2,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow+2,posCol+2,moveList)
                    
                    return True

        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            if(self.contains_piece(posRow-1,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol-2) and not([posRow-2,posCol-2]in(moveList))):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow-2,posCol-2,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow-2,posCol-2,moveList)
                    
                    return True
                

        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            if(self.contains_piece(posRow-1,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow-2,posCol+2) and not([posRow-2,posCol+2]in(moveList))):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow-2,posCol+2,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow-2,posCol+2,moveList)
                    
                    return True

        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            if(self.contains_piece(posRow,posCol-2)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol-4) and not([posRow,posCol-4]in(moveList))):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow,posCol-4,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow,posCol-4,moveList)
                    
                    return True
                
        
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
             #check for adjacent piece
            if(self.contains_piece(posRow,posCol+2)):
                #Check for empty spot after adjacent piece
                 if (not(self.is_clear(posRow,posCol+4) and not([posRow,posCol+4]in(moveList)))):
                    print("You can't move to [",posRow,"][",posCol,"]")    
                    return False
                 else:
                    self.swap_Piece(posRow,posCol+4,posRow,posCol)
                   #add the move
                    moveList.append([posRow,posCol])
                    self.select_jump(posRow,posCol+4,moveList)
                    
                    return True

    
    def select_jump(self,posRow,posCol,moveList):

        on= True
        while(on):
            self.display()
            jump = input('would you like to keep jumping True or False: ')
            

            if(jump == "True"):
                #Try take input while there is a valid jump
                moveRow = int(input('Move up is 1 move down is -1 still is 0: '))
                moveCol = int(input('Move right is 1 move left is -1 still is 0: '))

                    #chose where you want to jump
                if(self.is_jump_possible(moveRow,moveCol,posRow,posCol,moveList)):
                    on = False
                else:
                    print("move is not possible")
                       
                    
            #End of turn
            elif(jump == "False"):
                print("Reached here")
                on=False
            else:
                print("incorrect input please submit True or False")

    
        

    def select_piece(self):

        print("Select a piece")
        #Take user input
        posRow = int(input('Insert the Y coordinate: '))
        posCol = int(input('Insert the X coordinate: '))

         #Check it contains a piece
        if(self.contains_piece(posRow,posCol)):
            self.select_Move(posRow,posCol)
        else:
            print("Invalid Piece")    

    def select_Move(self,posRow,posCol):
       
        print("Where would you like to move")
        #Take user input
        moveRow = int(input('Move up is 1 move down is -1 still is 0: '))
        moveCol = int(input('Move right is 1 move left is -1 still is 0: '))
        
         #Check the move is valid and perform if it is 
        if(self.is_move_valid(moveRow,moveCol,posRow,posCol)):
           
            self.display()
        else:
            print("Not a valid move")

    #Ends a test
    def end_test(self):
        self.board[6][3]='R' 
        self.board[5][2]='R' 
        self.board[5][4]='R'
     
       
    def play(self):
        while(not(self.is_end())):
            currentPlayer=self.player
           
            while(currentPlayer==self.player):
                self.display()
                self.select_piece()
            
          
            

       
# y=2

# def test(y):
#     if(y>1):
#         x=3
#         return False
# if(test(y)):
#     print("y is read")


# def test_sum():
#     assert sum([1,2,3]) == 6 #"should be 6"
                                
# if __name__ == "__main__":
#     test_sum()
#     print("everything passed")


# x= board()
# x.display()
# x.play()


'''
game cycle

#1
select piece
move piece 
swap players

#2
select piece 
move piece
if(jump)
select (same piece)
move piece or (swap player "end turn")



def is_jump(self,moveRow,moveCol,posRow,posCol):
    if(self.contains_piece(moveRow,moveCol)):
        



'''