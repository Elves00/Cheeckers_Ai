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



x= board()
x.display()