from pickle import FALSE
from turtle import up

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
        
        maxValue = -2
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
                            if(self.is_move_valid(upOrDown,leftOrRight,posRow,posCol)):
                                #Check if its a jump
                                if(self.is_jump_valid(upOrDown,leftOrRight,posRow,posCol)):
                                    print("jump")
                                    #Tracks moves taken
                                    moveList = [[posRow,posCol]]
                                    #Maximises jumping
                                    self.jumping_max(posRow,posCol,moveList)
                                    moveList.remove([posRow,posCol])
                                    #jump
                                else:
                                    print("move")
                                    #Call min

                                #is a jump check all possible jumps
                                '''
                                Number of options here could call jumping max?


                                Brain storming 

                                is move valid returns true regardles of jump or move
                                is jump valid returns true if the move would be a jump
                                canJump = True
                                    jump max()??

                                jumpMax()
                                    for(all directions)
                                        if(is_jump_valid,direction,pos,movelist)
                                            movelist.append
                                            jump(direction,pos)

                                            #Two options end or keep jumping
                                                #keep jumping
                                                jumpMax()
                                               
                                                #end
                                                Min()
                                            movelist.remove(direction,pos)
                                       
                                    min()    
    
                                

                                jump/swap(direction ) 
                                    is jump valid(direction) note 00 = false
                                        swap piece
                                        return true
                                    else
                                        return false
                                    
    
                                '''
                                #not a jump test the move call min
    
    #maximises the jumping cycle
    def jumping_max(self,posRow,posCol,moveList):
        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        maxValue = -2
        result = self.is_end()

        #Player 1 wins
        if(result == 1):
            return (1,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0)

        direction =[1,0,-1]
        for i in direction:
            for j in direction:
                if(self.is_jump_valid(i,j,posRow,posCol,moveList)):
                    self.jump(i,j,posRow,posCol,moveList)
                    
    '''
    jumpMax()
                                    for(all directions)
                                        if(is_jump_valid,direction,pos,movelist)
                                            movelist.append
                                            jump(direction,pos)

                                            #Two options end or keep jumping
                                                #keep jumping
                                                jumpMax()
                                               
                                                #end
                                                Min()
                                            movelist.remove(direction,pos)
                                       
                                    min()    
'''
        
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
                    return True
            
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

    #Checks a location on the board has no piece and is on the board
    def is_clear(self,row,col):
        if(row>7 or row<0 or col>7 or col<0):
            print("out of range")
            return False
        
        if(self.board[row][col] !="."):
            print(self.board[row][col])
          
            print("[",row,"][",col,"]","occupied")
            return False
        else:
            return True

    #Checks a location on the board for a piece
    def contains_piece(self,row,col):
        if self.board[row][col] != "x" and self.board[row][col] != " " and self.board[row][col] != ".":
            
         return True
        else:
            return 
            

    def swap_Player(self):
        if(self.player=='R'):
            self.player='B'
        else:
            self.player='R'


    def jump(self,upOrDown,leftOrRight,posRow,posCol,moveList):

        #moving down left
        if upOrDown < 0 and leftOrRight < 0:
            moveList.append([posRow+2,posCol+2])
            self.swap_Piece(posRow+2,posCol+2,posRow,posCol)
        #moving down right
        if upOrDown < 0 and leftOrRight > 0:
            moveList.append([posRow+2,posCol-2])
            self.swap_Piece(posRow+2,posCol-2)
        #moving up left
        if upOrDown > 0 and leftOrRight < 0:
            moveList.append([posRow-2,posCol-2])
            self.swap_Piece(posRow-2,posCol-2)
        #moving up right
        if upOrDown > 0 and leftOrRight > 0:
            moveList.append([posRow-2,posCol+2])
            self.swap_Piece(posRow-2,posCol+2)
        #moving left
        if upOrDown == 0 and leftOrRight < 0:
            moveList.append([posRow,posCol-4])
            self.swap_Piece(posRow,posCol-4)
        #moving right
        if(upOrDown == 0 and leftOrRight > 0):
            moveList.append([posRow,posCol+4])
            self.swap_Piece(posRow,posCol+4)
        
   

    def swap_Piece(self,moveRow,moveCol,posRow,posCol):
        #Swaps two pieces on a board 
        temp= self.board[posRow][posCol]
        print("prev:[",posRow,"][",posCol,"]")
        self.board[posRow][posCol]=self.board[moveRow][moveCol]
        self.board[moveRow][moveCol]=temp
        print("now:[",moveRow,"][",moveCol,"]")
        
   
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
            
          
            

       
y=2

def test(y):
    if(y>1):
        x=3
        return False
if(test(y)):
    print("y is read")

x= board()
x.display()
x.play()


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