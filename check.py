from pickle import FALSE
from turtle import up

#Note UP and DOWN are INVERTED but not left and right when moving things on the board using [row][col] ie row-1 moves a piece up one not down one
class board:
    

    def __init__(self):
        self.boardSetUp()

    def boardSetUp(self):
        self.board = [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',],['.',' ','.',' ','.',' ','.',],['x','.',' ','.',' ','.','x',],['x','x','B',' ','B','x','x',],['x','x','x','B','x','x','x',]]

    def display(self):
        for i in range(0,7):
            for j in range(0,7):
                print('{} '.format(self.board[i][j]), end= " ")
            print()
        print()

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
            
    def swap_Piece(self,moveRow,moveCol,posRow,posCol):
        #Swaps two pieces on a board 
        temp= self.board[posRow][posCol]
        print("Temp=",temp)
        self.board[posRow][posCol]=self.board[moveRow][moveCol]
        self.board[moveRow][moveCol]=temp
        print(moveRow)


    #Checks if a move is possible mx =move to x px = peice is at x
    def is_move_valid(self, upOrDown,leftOrRight ,posRow,posCol):
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
                    self.swap_Piece(posRow+2,posCol-2,posRow,posCol)
                    return True
            else:
                self.swap_Piece(posRow+1,posCol-1,posRow,posCol)
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
                    return True
            else:
                self.swap_Piece(posRow+1,posCol+1,posRow,posCol)
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
                    return True
            else:
                self.swap_Piece(posRow-1,posCol-1,posRow,posCol)
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
                    return True
            else:
                self.swap_Piece(posRow-1,posCol+1,posRow,posCol)
                return True
         #moving left
        if upOrDown == 0 and leftOrRight < 0:
            print("down left")
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol-1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol-2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow,posCol-2,posRow,posCol)
                    return True
            else:
                self.swap_Piece(posRow,posCol-1,posRow,posCol)
                return True
        #moving left
        if upOrDown == 0 and leftOrRight > 0:
            print("down left")
            #check for adjacent piece
            if(self.contains_piece(posRow,posCol+1)):
                #Check for empty spot after adjacent piece
                 if not(self.is_clear(posRow,posCol+2)):
                    print("Jummping space is not clear")
                    return False
                 else:
                    self.swap_Piece(posRow,posCol+2,posRow,posCol)
                    return True
            else:
                self.swap_Piece(posRow,posCol+1,posRow,posCol)
                return True
        
        else:
            print("Check conditions we shouldn't reach here")


    def selectPiece(self):

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
            print("here")
            self.display()
        else:
            print("Not a valid move")

       
    def play(self):
        end=False
        while(not(end)):
            self.display
            self.selectPiece()

       

x= board()
x.display()
x.play()