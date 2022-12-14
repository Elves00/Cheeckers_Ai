'''
This file contains the evaluation matrixs of different players for a game of chineese checkers
'''

# from Game import board
class evaluator():
    def __init__(self, currentBoard, currentPlayer, currentMode):
        self.board = currentBoard
        self.player = currentPlayer
        self.mode = currentMode
        self.r  =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
            [0, 2, 0, 3, 0, 4, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 4, 0, 3, 0, 2, 0],
            [0, 0, 3, 0, 4, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 4, 0, 3, 0, 0],
            [0, 0, 0, 4, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0],
            [0, 0, 0, 8, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 8, 0, 0, 0],
            [0, 0, 7, 0, 8, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 8, 0, 7, 0, 0],
            [0, 6, 0, 7, 0, 8, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 8, 0, 7, 0, 6, 0],
            [5, 0, 6, 0, 7, 0, 8, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 8, 0, 7, 0, 6, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 14, 0, 14, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        #Old evaluation    
        # self.r  =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5],
        #     [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0],
        #     [0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 0],
        #     [0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0],
        #     [0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0],
        #     [0, 0, 0, 9, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 9, 0, 0, 0],
        #     [0, 0, 9, 0, 10, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 10, 0, 9, 0, 0],
        #     [0, 9, 0, 10, 0, 11, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 11, 0, 10, 0, 9, 0],
        #     [9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 14, 0, 14, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

 
        self.b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 14, 0, 14, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 6, 0, 7, 0, 8, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 8, 0, 7, 0, 6, 0, 5],
            [0, 6, 0, 7, 0, 8, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 8, 0, 7, 0, 6, 0],
            [0, 0, 7, 0, 8, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 8, 0, 7, 0, 0],
            [0, 0, 0, 8, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 4, 0, 0, 0],
            [0, 0, 3, 0, 4, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 4, 0, 3, 0, 0],
            [0, 2, 0, 3, 0, 4, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 4, 0, 3, 0, 2, 0],
            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        # self.b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 15, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 14, 0, 14, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 13, 0, 13, 0, 13, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9],
        #     [0, 9, 0, 10, 0, 11, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 12, 0, 11, 0, 10, 0, 9, 0],
        #     [0, 0, 9, 0, 10, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 11, 0, 10, 0, 9, 0, 0],
        #     [0, 0, 0, 9, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 9, 0, 0, 0],
        #     [0, 0, 0, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0],
        #     [0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0],
        #     [0, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 0],
        #     [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0],
        #     [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
                   [0, 6, 0, 7, 0, 8, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0],
                   [0, 0, 7, 0, 8, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 0],
                   [0, 0, 0, 8, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0],
                   [0, 0, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 4, 0, 0, 0],
                   [0, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 4, 0, 3, 0, 0],
                   [0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 4, 0, 3, 0, 2, 0],
                   [17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 4, 0, 3, 0, 2, 0, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # self.g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
        #            [0, 10, 0, 10, 0, 10, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0],
        #            [0, 0, 11, 0, 11, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 0],
        #            [0, 0, 0, 12, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 0, 0],
        #            [0, 0, 0, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0],
        #            [0, 0, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0],
        #            [0, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0],
        #            [0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0],
        #            [17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 11, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


        self.y = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5],
                   [0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 8, 0, 7, 0, 6, 0],
                   [0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 8, 0, 7, 0, 0],
                   [0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 8, 0, 0, 0],
                   [0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 0, 0, 0],
                   [0, 0, 0, 4, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 0, 0],
                   [0, 0, 3, 0, 4, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 0],
                   [0, 2, 0, 3, 0, 4, 0, 8, 0, 9, 0, 10, 0, 11,  0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0],
                   [1, 0, 2, 0, 3, 0, 4, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # self.y = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9],
        #            [0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 10, 0, 10, 0, 10, 0],
        #            [0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 11, 0, 11, 0, 0],
        #            [0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 12, 0, 0, 0],
        #            [0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 0, 0, 0],
        #            [0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 0, 0],
        #            [0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 0],
        #            [0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11,  0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0],
        #            [5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.o=   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 2, 0, 3, 0, 4, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17],
                   [0, 2, 0, 3, 0, 4, 0, 8, 0, 9, 0, 10, 0, 11,  0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0],
                   [0, 0, 3, 0, 4, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 0],
                   [0, 0, 0, 4, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 0, 0],
                   [0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 0, 0, 0],
                   [0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 8, 0, 0, 0],
                   [0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 8, 0, 7, 0, 0],
                   [0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 8, 0, 7, 0, 6, 0],
                   [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # self.o=   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 10, 0, 11, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17],
        #            [0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11,  0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0],
        #            [0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 0],
        #            [0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 0, 0],
        #            [0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 0, 0, 0],
        #            [0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 12, 0, 0, 0],
        #            [0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 11, 0, 11, 0, 0],
        #            [0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 10, 0, 10, 0, 10, 0],
        #            [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.p=   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 4, 0, 3, 0, 2, 0, 1],
                   [0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 4, 0, 3, 0, 2, 0],
                   [0, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 4, 0, 3, 0, 0],
                   [0, 0, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 4, 0, 0, 0],
                   [0, 0, 0, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0],
                   [0, 0, 0, 8, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 0, 0],
                   [0, 0, 7, 0, 8, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 0],
                   [0, 6, 0, 7, 0, 8, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0],
                   [5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                   
        # self.p=   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 11, 0, 10, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [17, 0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5],
        #            [0, 16, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0],
        #            [0, 0, 15, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0],
        #            [0, 0, 0, 14, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0],
        #            [0, 0, 0, 0, 13, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0],
        #            [0, 0, 0, 12, 0, 12, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 0, 0],
        #            [0, 0, 11, 0, 11, 0, 11, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 0],
        #            [0, 10, 0, 10, 0, 10, 0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0],
        #            [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

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
                        value += self.r[i][j]
        elif (self.player == 'B'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.b[i][j]
        elif (self.player == 'G'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.g[i][j]
        elif (self.player == 'O'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.o[i][j]
        elif (self.player == 'Y'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.y[i][j]
        elif (self.player == 'P'):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    if (self.board.board[i][j] == self.player):
                        value += self.p[i][j]

        return value

    def print_evaluation_matrix(self,player):
        if((player=='R' or player =='B') and self.mode =="full"):
            for i in range(0, self.board.boardHeight):
                for j in range(0, self.board.boardWidth):
                    print('{} '.format(self.rb[i][j]), end=" ")
                print()
        print("   ",end='')

# test = board.board()
# test.swap_board("full")
# test.display()

# evaluate = evaluator(test, test.player, test.mode)

# print(evaluate.evaluatePosition(test.player,test))
# #G
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))
# #P
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))
# #B
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))
# #O
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))
# #Y
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))
# #R
# test.next_Player()
# print(test.player)
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))

# test.swap_board("small")
# evaluate = evaluator(test, test.player, test.mode)
# print(evaluate.evaluatePosition(test.player,test))

# test.swap_board("full")
# evaluate = evaluator(test, test.player, test.mode)

# evaluate.print_evaluation_matrix('R')
