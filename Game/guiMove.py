import tkinter as tk
from tkinter import DISABLED, Button, font
from board import board
    

class ChineseCheckersBoard(tk.Tk):
    clickedButtonPlace = (0,0)
    clickedButton = Button
    def __init__(self):
        super().__init__()
        self.title("Chinese Checkers")
        self.iconbitmap('tear-laugh.ico')
        self.gameboard = board()
        self.gameboard.swap_board("full")
        self.gameboard.player = 'R'
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()
        self.moveList = []
   
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
            row, col = self._cells.get(button)
            (posRow, posCol) = self.clickedButtonPlace
            if(self.gameboard.is_move_valid(posCol-col, posRow-row, col, row)):
                if(self.clickedButton == button):
                    self.clickedButtonPlace = (0, 0)
                elif(self.clickedButtonPlace == (0,0)):
                    self.clickedButton = button
                    self.clickedButtonPlace = (row,col)
                else:
                    colour = self.clickedButton.cget('bg')
                    newMoveColour = button.cget('bg')
                    self.gameboard.swap_Piece(row,col,posRow,posCol)
                    self.gameboard.display()
                    self.clickedButton.configure(bg=newMoveColour)
                    print(self.clickedButton)
                    button.configure(bg=colour)
                    self.clickedButtonPlace = (0,0)

      
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
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Blue",
                        )

                    elif board_structure[row][col] == 'Y':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Yellow",
                        )
                    elif board_structure[row][col] == 'G':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Green",
                        )
                    elif board_structure[row][col] == 'P':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Pink",
                        )
                    elif board_structure[row][col] == 'O':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Orange",
                        )
                    elif board_structure[row][col] == 'S':
                        button = tk.Button(
                            master=grid_frame,
                            state = DISABLED,
                            text='',
                            font=font.Font(size=5, weight="bold"),
                            width=3,
                            height=2,
                            bg="Brown",
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

def main():
    board = ChineseCheckersBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
