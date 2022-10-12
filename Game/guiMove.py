import tkinter as tk
from tkinter import DISABLED, Button, font
from board import board
from guiInterface import guiInterface
    

class ChineseCheckersBoard(tk.Tk):
    clickedButtonPlace = (0,0)
    clickedButton = Button
    jumpButton = Button
    moved = False
    endTurn = False
    playerList = ('G', 'P', 'B', 'O', 'Y')
    def __init__(self):
        super().__init__()
        self.title("Chinese Checkers")
        self.iconbitmap('tear-laugh.ico')
        self.interface = guiInterface()
        self.gameboard = self.interface.getCurrentBoard()
        self.gameboard.swap_board("full")
        self.gameboard.player = 'R'
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()
   
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Chinese Checkers",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()
    

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        board_rows = self.gameboard.row
        board_cols = self.gameboard.col
        board_structure = self.gameboard.board

        def OnButtonClick(button):
            if not self.moved:
                row, col = self._cells.get(button)
                print('Current Button ' , str(row) , str(col))
                (posRow, posCol) = self.clickedButtonPlace
                if(self.clickedButton == button):
                    self.clickedButtonPlace = (0, 0)
                elif(self.clickedButtonPlace == (0,0)):
                    self.clickedButton = button
                    self.clickedButtonPlace = (row,col)
                else:
                    if(self.interface.is_player_move_valid(row,col, posRow,posCol, self.gameboard.player)):
                        swapButtons(button, self.clickedButton)
                        self.clickedButtonPlace = (0,0)
                        if(self.interface.is_jump(row,col, posRow,posCol, self.gameboard.player)):
                            self.jumpButton = button
                            self.interface.jump(row,col, posRow,posCol, self.gameboard.player)
                            self.gameboard = self.interface.getCurrentBoard()
                            self.gameboard.display()
                        else:
                            self.interface.move(row,col, posRow,posCol, self.gameboard.player)
                            self.gameboard = self.interface.getCurrentBoard()
                            self.gameboard.display()
                            self.moved = True  
                    else:
                        self.clickedButtonPlace = (0, 0)
                print('Clicked Button: ', self.clickedButtonPlace)

        def endPlayerTurn():
            self.endTurn = True
            for player in self.playerList:
                (row1, col1, row2, col2) = self.interface.ai_move(player) 
                swapButtons(getButton(row1, col1), getButton(row2,col2))
            self.moved = False

        def getButton(row, col):
            for button, coordinate in self._cells.items():
                if coordinate == (row,col):
                    return button

        def swapButtons(button1, button2):
            colour1 = button1.cget('bg')
            colour2 = button2.cget('bg')  
            button1.configure(bg=colour2)
            button2.configure(bg=colour1)
              
        def displayButtons():
            for row in range(board_rows):
                self.rowconfigure(row, weight=1, minsize=25)
                self.columnconfigure(row, weight=1, minsize=25)
                for col in range(board_cols):
                    if board_structure[row][col] == 'x':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bd=0,
                        )
                    elif board_structure[row][col] == ' ':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bd=0,
                        )
                    elif board_structure[row][col] == 'R':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Red",
                        )
                    elif board_structure[row][col] == 'B':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Blue",
                        )

                    elif board_structure[row][col] == 'Y':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Yellow",
                        )
                    elif board_structure[row][col] == 'G':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Green",
                        )
                    elif board_structure[row][col] == 'P':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Pink",
                        )
                    elif board_structure[row][col] == 'O':
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Orange",
                        )             
                    else:
                        button = tk.Button(
                            master=grid_frame,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            fg="black",
                            width=3,
                            height=2,
                            highlightbackground="lightblue",                    
                        )
                    button.configure(command=lambda button=button: OnButtonClick(button))
                    self._cells[button] = (row, col)
                    button.grid(
                        row=row,
                        column=col,
                        padx=5,
                        pady=5,
                        sticky="nsew",
                    )
        displayButtons()
        endButton = tk.Button(
            master=self,
            text='END TURN',
            font=font.Font(size=10, weight="bold"),
            width=10,
            height=3,
            bg="Purple",
            command=endPlayerTurn
        ).pack()
    

def main():
    board = ChineseCheckersBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
