import board


class miniMax:
    
    def setGameBoard(self,board):
        self.gameBoard=board
    #maximiser
    def max(self):
      
        

        #possible values 
        # 1 player 1 wins 2 player 2 wins
        maxv = -2
        mx = None
        my = None
        px=None
        py=None
        result = self.gameBoard.is_end()


        #Player 1 wins
        if(result == 1):
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0,0,0)

        #if the game hasn't ended cycle through all possible moves
        for posRow in range(0,self.gameBoard.boardHeight):
            for posCol in range (0,self.gameBoard.boardWidth):
                #It's the max players piece
                if(self.gameBoard.board[posRow][posCol]=='R'):
                    #list of possible movment directions
                    direction = [-1,0,1]
                    #cycle all move directions
                    for i in direction:
                        for j in direction:
                            #if the move is possible investigate
                            if(self.gameBoard.is_move_possible(i,j,posRow,posCol)):
                                
                                #Check if the move being attempted is a jump
                                if(self.gameBoard.is_jump(i,j,posRow,posCol)):
                                    # print("jump")
                                    #Tracks moves taken
                                    moveList = [[posRow,posCol]]
                                    #Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m,max_y,max_x) = self.jumping_max(posRow,posCol,moveList)
                                    #Checks if we have a better move and set it 
                                    if m > maxv:
                                        maxv=m
                                        my=i
                                        mx=j
                                        px=posRow
                                        py=posCol
                                    #remove move from list after checking
                                    moveList.remove([posRow,posCol])
                                else:
                                    # print("move i,j:",i," ",j,"row,col",posRow,posCol)
                                    #Check current position value
                                    currentValue=self.gameBoard.position_evaluator()
                                    (tempRow,tempCol)=self.gameBoard.move(i,j,posRow,posCol)
                                    #Evaluate the position only if its better for R
                                    if(self.gameBoard.position_evaluator()>currentValue):
                                        self.gameBoard.turn+=1
                                        print(self.gameBoard.turn)
                                        self.gameBoard.swap_Player()
                                        print(maxv,mx,my,px,py)
                                        #Call min
                                        (m,max_y,max_x,pos_x,pos_y)=self.min()
                                        if m > maxv:
                                            maxv=m
                                            my=i
                                            mx=j
                                            px=posRow
                                            py=posCol
                                    #remove move
                                    # print("max swap [",tempRow,"][",tempCol,"] with [",posRow,"][",posCol,"]")
                                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)
                                    
        print("returning:",maxv,mx,my,px,py)
        return (maxv,my,mx,px,py)

    #maximises the jumping cycle
    def jumping_max(self,posRow,posCol,moveList):
        # print("jumping max")
        
        # print(moveList)
        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        maxv = -2
        mx = None
        my = None
        
        result = self.gameBoard.is_end()

        #Player 1 wins
        if(result == 1):
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0,0,0)

        #Posible directions a piece can move
        direction =[-1,0,1]

        #For all directions in x and y
        for i in direction:
            for j in direction:
                #Check if there is a valid jump and explore it 
                if(self.gameBoard.is_jump_valid(i,j,posRow,posCol,moveList)):
                    # print()
                    # print("checking: i ",i," j ",j,"posRow ",posRow,"posCol ",posCol,"moveList ",moveList)
                    # print()

                    #gets value before move
                    currentValue=self.gameBoard.position_evaluator()

                    #Stores the new move position and moves piece
                    moveList,tempRow,tempCol=self.gameBoard.jump(i,j,posRow,posCol,moveList)
                    
                    #maximises for the new position if it is a greater value
                    if(self.gameBoard.position_evaluator()>currentValue):
                        (m,max_i,max_j)=self.jumping_max(tempRow,tempCol,moveList)
                        if m > maxv:
                            maxv=m
                            my=i
                            mx=j
                        self.gameBoard.turn+=1
                        print(self.gameBoard.turn)
                        #Move the peice back to previous position
                        self.gameBoard.swap_Player()
                        (m,min_i,min_j,pos_x,pos_y)=self.min()

                        if m > maxv:
                            maxv=m
                            my=i
                            mx=j
                    
                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)       
        
        

        return (maxv,my,mx)


    def min(self):
        # print("min")
        
        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        minv = 2
        mx = None
        my = None
        px=None
        py=None
        result = self.gameBoard.is_end()

        #Player 1 wins
        if(result == 1):
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            return (-1,0,0,0,0)

        #if the game hasn't ended cycle through all possible moves
        for posRow in range(0,self.gameBoard.boardHeight):
            for posCol in range (0,self.gameBoard.boardWidth):
            
                #It's the max players piece
                if(self.gameBoard.board[posRow][posCol]=='B'):
                    #list of possible movment directions
                    direction = [1,0,-1]
                    #cycle all move directions
                    for i in direction:
                        for j in direction:
                            #if the move is valid
                            if(self.gameBoard.is_move_possible(i,j,posRow,posCol)):
                                #Check if the move being attempted is a jump
                                if(self.gameBoard.is_jump(i,j,posRow,posCol)):
                                    # print("jump")
                                    #Tracks moves taken
                                    moveList = [[posRow,posCol]]
                                    #Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m,min_y,min_x)=self.jumping_min(posRow,posCol,moveList)
                                    #Checks if we have a better move and set it 
                                    if m < minv:
                                        minv=m
                                        my=i
                                        mx=j
                                        px=posRow
                                        py=posCol
                                    #remove move from list after checking
                                    moveList.remove([posRow,posCol])
                                else:
                                    #move is not possible? swaping 21,with 12 #########MAKE TEST CASE
                                    # print("move i,j:",i," ",j,"row,col",posRow,posCol)
                                    currentValue=self.gameBoard.position_evaluator()
                                    # print("Current value=",board.position_evaluator())
                                    (tempRow,tempCol)=self.gameBoard.move(i,j,posRow,posCol)
                                    # print("Post move value=",board.position_evaluator())
                                    
                                    #evaluate the position only if it's less then the current value
                                    if(self.gameBoard.position_evaluator()<currentValue):
                                        # print("Post move value=",board.position_evaluator())
                                        self.gameBoard.turn+=1
                                        print(self.gameBoard.turn)
                                        self.gameBoard.swap_Player()
                                        print(minv,mx,my,px,py)
                                        (m,max_y,max_x,pos_x,pos_y)=self.max()
                                        if m < minv:
                                            minv=m
                                            my=i
                                            mx=j
                                            px=posRow
                                            py=posCol
                                        
                                        #remove move
                                        # print("min swap [",tempRow,"][",tempCol,"] with [",posRow,"][",posCol,"]")
                                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)
        print("returning:",minv,mx,my,px,py)
        return (minv,my,mx,px,py)
        
    def jumping_min(self,posRow,posCol,moveList):
        # print("minimizing jump")

        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        minv = 2
        my = None
        mx = None
        result = self.gameBoard.is_end()

        #Player 1 wins
        if(result == 1):
            self.gameBoard.display()
            return (1,0,0)
        #The other player wins 
        elif(result == 2):
            self.gameBoard.display()
            return (-1,0,0)

        #Posible directions a piece can move
        direction =[1,0,-1]

        #For all directions in x and y
        for i in direction:
            for j in direction:
                #Check if there is a valid jump and explore it 
                if(self.gameBoard.is_jump_valid(i,j,posRow,posCol,moveList)):
                    # print()
                    # print("jumping min:")
                    # board.display()
                    currentValue=self.gameBoard.position_evaluator()
                    #Stores the new move position
                    moveList,tempRow,tempCol=self.gameBoard.jump(i,j,posRow,posCol,moveList)
                    # print()
                    #maximises for the new position
                    if(self.gameBoard.position_evaluator() < currentValue):
                        # print()
                        # print("Jump was lower previous value:",currentValue," new value:",board.position_evaluator())
                        # board.display()
                        (m,min_i,min_j)=self.jumping_min(tempRow,tempCol,moveList)
                        if m < minv:
                            minv=m
                            mx=i
                            my=j
                        self.gameBoard.turn+=1
                        self.gameBoard.swap_Player()    
                        (m,min_i,min_j,pos_row,pos_col)=self.max()
                        
                        if m < minv:
                            minv=m
                            mx=i
                            my=j
                        
                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)

        
        return (minv,mx,my)

# x=board.board()
# mini=miniMax()
# mini.setGameBoard(x)
# print(mini.max())