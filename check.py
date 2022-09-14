from pickle import FALSE


class board:
    

    def __init__(self):
        self.boardSetUp()

    def boardSetUp(self):
        self.board = [['x','x','x','R','x','x','x',],['x','x','R',' ','R','x','x',],['x','.',' ','.',' ','.','x',]]

    def display(self):
        for i in range(0,3):
            for j in range(0,7):
                print('{} '.format(self.board[i][j]), end= " ")
            print()
        print()

    def is_piece_valid(self,px,py):
        return True

    #Checks a location on the board for a piece
    def contains_piece(self,locx,locy):
        if self.board[locx][locy] != "x" or self.board[locx][locy] != " " or self.board[locx][locy] != ".":
         return True
        else:
            return False

    #Checks if a move is possible mx =move to x px = peice is at x
    def is_valid(self, mx,my ,px,py):

        if mx< 0 or mx>7 or my<0 or my>7:
            return False

        #moving down left
        if mx > -1 and my >-1:
            #Check there is piece occupying jump spot
            if self.contains_piece(px-2,py-2):
                return False
            else:
                #check there is a piece to jump in the adjacent spot
                return self.contains_piece(px-1,py-1)

        #moving up right
        elif mx < 0 and my < 0:
             if self.contains_piece(px+2,py+2):
                return False
             else:
                return self.contains_piece(px+1,py+1)

        #moving down right 
        elif mx > -1 and my <0:
            if self.contains_piece(px-2,py+2):
                return False
            else:
                return self.contains_piece(px-1,py+1)
                
        #moving up left 
        elif mx < 0  and my>-1:
             if self.contains_piece(px+2,py-2):
                return False
             else:
                return self.contains_piece(px+1,py-1)
        #Jumping right
        elif mx >0 or my ==0:
            if self.contains_piece(px,px-2):
                return False
            else:
                return self.contains_piece(px,px-1)

        #Jumping left


        #Moving to adjacent hole
        elif (mx==px+1 or mx==px-1) and (my==px+1 or my==px-1):
            if self.board[mx][my] != ' ':
                return False
            else:
                return True
        #Making a jump to another hole
        elif (mx==px +2 or mx==px-2) and (my==py+2 or my==py-2):
            
            if self.board[mx][my] != " ":
                return False
            #Checking hole is occupied
            elif():
                return True
        else:
            return False
        

x= board()
x.display()