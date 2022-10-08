# from Game import board
import board
class evaluator():
    def __init__(self, currentBoard, currentPlayer, currentMode):
        self.board = currentBoard
        self.player = currentPlayer
        self.mode = currentMode
        self.rb = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
                       2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3,
                       0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0,
                       4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 5, 0, 5,
                       0, 5, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9],
                   [0, 9, 0, 8, 0, 7, 0, 6, 0, 6, 0, 6, 0,
                    6, 0, 6, 0, 6, 0, 7, 0, 8, 0, 9, 0],
                   [0, 0, 9, 0, 8, 0, 7, 0, 7, 0, 7, 0, 7,
                    0, 7, 0, 7, 0, 7, 0, 8, 0, 9, 0, 0],
                   [0, 0, 0, 9, 0, 8, 0, 8, 0, 8, 0, 8, 0,
                    8, 0, 8, 0, 8, 0, 8, 0, 9, 0, 0, 0],
                   [0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9,
                    0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0],
                   [0, 0, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0,
                    10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 0, 0],
                   [0, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11,
                    0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 0],
                   [0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0,
                    12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0],
                   [13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13,
                    0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 14, 0,
                    14, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15,
                    0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0,
                    16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.go = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0,
                       5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 6,
                       0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 0,
                       6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 8, 0, 7,
                       0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
                   [0, 10, 0, 10, 0, 10, 0, 10, 0, 9, 0, 8,
                    0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0],
                   [0, 0, 11, 0, 11, 0, 11, 0, 10, 0, 9, 0,
                    8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 0],
                   [0, 0, 0, 12, 0, 12, 0, 11, 0, 10, 0, 9,
                    0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 13, 0, 12, 0, 11, 0, 10, 0,
                    9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0],
                   [0, 0, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10,
                    0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0],
                   [0, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0,
                    10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0],
                   [0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11,
                    0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0],
                   [17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0,
                    11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 11, 0,
                    10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 10,
                    0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0,
                    9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.py = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9],
                   [0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 10, 0, 10, 0, 10, 0],
                   [0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 11, 0, 11, 0, 0],
                   [0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 12, 0, 0, 0],
                   [0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 0, 0, 0],
                   [0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 0, 0],
                   [0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 0],
                   [0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11,  0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0],
                   [5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def evaluatePosition(self,player,board):
        self.player=player
        self.board=board
        value = 0
        if (self.mode == "full"):
            value = self.evaluateFull()
        else:
            value = self.evaluateSmall()
        return value

    def evaluateSmall(self):
        '''
        For a small board returns the value of the sum of row position the current players pieces occupy. If the player is B this is calculated by
        subtracting the current pieces row from 6 and summing these
        '''
        value = 0
        if (self.player == 'R'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += i
        else:
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += 6 - i
        return value

    def evaluateFull(self):
        value = 0
        if (self.player == 'R'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.rb[i][j]
        elif (self.player == 'B'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += 18 - self.rb[i][j]
        elif (self.player == 'G'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.go[i][j]
        elif (self.player == 'O'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += 18 - self.go[i][j]
        elif (self.player == 'Y'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.py[i][j]
        elif (self.player == 'P'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += 18 - self.py[i][j]

        return value

    def print_evaluation_matrix(self,player):
        print("here")
        if((player=='R' or player =='B') and self.mode =="full"):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    print('{} '.format(self.rb[i][j]), end=" ")
                print()
        print("   ",end='')

test = board.board()
test.swap_board("full")
test.display()

evaluate = evaluator(test, test.player, test.mode)

print(evaluate.evaluatePosition(test.player,test))
#G
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))
#P
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))
#B
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))
#O
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))
#Y
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))
#R
test.swap_Player()
print(test.player)
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))

test.swap_board("small")
evaluate = evaluator(test, test.player, test.mode)
print(evaluate.evaluatePosition(test.player,test))

test.swap_board("full")
evaluate = evaluator(test, test.player, test.mode)

evaluate.print_evaluation_matrix('R')
