import board


class miniMax:
    
    def setGameBoard(self,board):
        self.gameBoard=board

    #maximiser
    def max(self):
        print("max")
        
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
            print("max victory player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            print("max victory player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (-1,0,0,0,0)

        if(self.gameBoard.player=='B'):
            print("we were called from one of two mins")
            raise Exception("Player B is playing max")   

        validMove=False
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
                                validMove=True
                                #Check if the move being attempted is a jump
                                if(self.gameBoard.is_jump(i,j,posRow,posCol)):
                                    #Tracks moves taken
                                    moveList = [[posRow,posCol]]
                                    #Maximises jumping (Minmising occurs inside the jumping_max)
                                    (m,max_y,max_x,px,py) = self.jumping_max(posRow,posCol,moveList)
                                    
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
                                    
                                    #Check current position value
                                    currentValue=self.gameBoard.position_evaluator()
                                    (tempRow,tempCol)=self.gameBoard.move(i,j,posRow,posCol)
                                    #Evaluate the position only if its better for R
                                    if(self.gameBoard.position_evaluator()>currentValue):
                                        self.gameBoard.turn+=1
                                        # print(self.gameBoard.turn)
                                        self.gameBoard.swap_Player()
                                        #Call min
                                        (m,max_y,max_x,pos_x,pos_y)=self.min()
                                        if m > maxv:
                                            maxv=m
                                            my=i
                                            mx=j
                                            px=posRow
                                            py=posCol

                                    #remove move
                                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)

        '''
        What to think about
        so we only assign px py my mx if we have a better move..
        we should probably set a default which means we never return none.
        
        2 ways to do this. Simple way we just set my mx px py at the start or each move 

        Thoughts valid move returns none which shouldn't be a thing there should always be a move?

        Note it's returning B so we have an exception cause it should be R
        '''

       

        # print("returning max:",maxv,mx,my,px,py," player:",self.gameBoard.player)
        return (maxv,my,mx,px,py)

    #maximises the jumping cycle
    def jumping_max(self,posRow,posCol,moveList):
        print("jumping max")
        if(self.gameBoard.player=='B'):
            raise Exception("Player B is playing jumping min")
        
        # print(moveList)
        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        maxv = -2
        mx = None
        my = None
        px = None
        py = None
        
        result = self.gameBoard.is_end()

        #Player 1 wins
        if(result == 1):
            print("jumping max victory player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            print("jumping max victory player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (-1,0,0,0,0)

        #Posible directions a piece can move
        direction =[-1,0,1]

        #For all directions in x and y
        for i in direction:
            for j in direction:
                #Check if there is a valid jump and explore it 
                if(self.gameBoard.is_jump_valid(i,j,posRow,posCol,moveList)):
                    
                    #gets value before move
                    currentValue=self.gameBoard.position_evaluator()

                    #Stores the new move position and moves piece
                    moveList,tempRow,tempCol=self.gameBoard.jump(i,j,posRow,posCol,moveList)
                    
                    #maximises for the new position if it is a greater value
                    if(self.gameBoard.position_evaluator()>currentValue):
                        (m,max_i,max_j,px,py)=self.jumping_max(tempRow,tempCol,moveList)
                        if m > maxv:
                            maxv=m
                            my=i
                            mx=j
                        self.gameBoard.turn+=1
                        # print(self.gameBoard.turn)
                        #Move the peice back to previous position
                        self.gameBoard.swap_Player()
                        (m,min_i,min_j,pos_x,pos_y)=self.min()

                        if m > maxv:
                            maxv=m
                            my=i
                            mx=j

                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)      
        
        
        # print("returning jumping max player:",self.gameBoard.player)
        return (maxv,my,mx,px,px)


    def min(self):
        print("min")
       
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
            print("returning min:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            print("returning min:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (-1,0,0,0,0)

        if(self.gameBoard.player=='R'):

            raise Exception("Player R is playing max")

        validMove=False

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
                                    (m,min_y,min_x,px,py)=self.jumping_min(posRow,posCol,moveList)
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
                                    currentValue=self.gameBoard.position_evaluator()

                                    (tempRow,tempCol)=self.gameBoard.move(i,j,posRow,posCol)
                                    
                                    #evaluate the position only if it's less then the current value
                                    if(self.gameBoard.position_evaluator()<currentValue):

                                        self.gameBoard.turn+=1
                                        # print(self.gameBoard.turn)

                                        self.gameBoard.swap_Player()
                                        (m,max_y,max_x,pos_x,pos_y)=self.max()
                                        if m < minv:
                                            minv=m
                                            my=i
                                            mx=j
                                            px=posRow
                                            py=posCol
                                        
                                        #remove move
                                    self.gameBoard.swap_Piece(tempRow,tempCol,posRow,posCol)

        # print("returning min:",minv,mx,my,px,py," player:",self.gameBoard.player)
        return (minv,my,mx,px,px)
        
    def jumping_min(self,posRow,posCol,moveList):
        print("minimizing jump")

        #possible values 
        # 1 player 1 wins 2 player 2 wins
        
        minv = 2
        my = None
        mx = None
        px = None
        py = None
        result = self.gameBoard.is_end()

        #Player 1 wins
        if(result == 1):
            print("jumping min player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (1,0,0,0,0)
        #The other player wins 
        elif(result == 2):
            print("jumping min player:",self.gameBoard.player)
            self.gameBoard.swap_Player()
            return (-1,0,0,0,0)
        
        
        if(self.gameBoard.player=='R'):
            raise Exception("Player R is playing jumping min")


        #Posible directions a piece can move
        direction =[1,0,-1]

        #For all directions in x and y
        for i in direction:
            for j in direction:
                #Check if there is a valid jump and explore it 
                if(self.gameBoard.is_jump_valid(i,j,posRow,posCol,moveList)):

                    currentValue=self.gameBoard.position_evaluator()

                    #Stores the new move position
                    moveList,tempRow,tempCol=self.gameBoard.jump(i,j,posRow,posCol,moveList)

                    #maximises for the new position
                    if(self.gameBoard.position_evaluator() < currentValue):

                        (m,min_i,min_j,px,py)=self.jumping_min(tempRow,tempCol,moveList)
                        
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

        # print("returning jumping min player:",self.gameBoard.player)
        return (minv,mx,my,px,px)