# root.geometry("500x500")
# root.config(bg="#d2b48c")

# # pack() makes it show
# myLabel = Label(root, text= 'Hi Tui!', fg="brown").pack()
# myLabel2 = Label(root, text= 'What\'s your favourite food?').pack()
# myLabel3 = Label(root, text= 'From Gherkin').pack()

# textInput = Entry(root, width=50, fg="#281e10")
# textInput.pack()

# def my_click():
#     myLabel4 = Label(root, text= "It's " + textInput.get()).pack() 
# myButton = Button(root, text= 'Answer', command= my_click, padx=30, pady=30).pack()

import tkinter as tk
from tkinter import DISABLED, font
from board import board
# from tkinter import Label

class ChineseCheckersBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chinese Checkers")
        self.iconbitmap('tear-laugh.ico')
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
        gameboard = board()
        gameboard.swap_board("full")
        board_row = gameboard.row
        board_col = gameboard.col
        board_structure = gameboard.board
        for row in range(board_row):
            self.rowconfigure(row, weight=1, minsize=25)
            self.columnconfigure(row, weight=1, minsize=25)
            for col in range(board_col):
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
                        state = DISABLED,
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
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )


def main():
    board = ChineseCheckersBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
