import customtkinter as ctk
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.resizable(False, False)
        self.title('Tic Tac Toe')
        self.rowconfigure(list(range(5)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(5)), weight = 1, uniform = 'a')
        self.player = "X"
        self.moves = 0

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_turn = None

        self.create_buttons()
        self.mainloop()

    def create_buttons(self):
        self.player_turn = TTTLabel(
            parent = self,
            text = f'Player X turn'
        )

        self.reset_button = ResetButton(
            parent = self,
            func = lambda : self.reset(),
            text= "Reset"
        )

        for i in range(3):
            for j in range(3):
                button = TTTButton(
                    parent = self,
                    func = lambda row = i, col = j: self.click_button(row, col),
                    col = j+1,
                    row = i+1,
                    text = ''
                    )
                self.buttons[i][j] = button
                
    def click_button(self, row, col):
        if  self.buttons[row][col].cget("text") == "" and self.check_win() is False:
            self.buttons[row][col].configure(text= self.player)
            self.moves += 1
            if self.moves == 9:
                retry_bow = messagebox.askretrycancel("askretrycancel", f"Draw. Try again?")
                if retry_bow == True:
                    self.reset()
                else :
                    self.destroy()
            elif self.check_win():
                retry_bow = messagebox.askretrycancel("askretrycancel", f"Player {self.player} wins. Try again?")
                if retry_bow == True:
                    self.reset()
                else :
                    self.destroy()
            else: 
                self.player = 'O' if self.player == 'X' else 'X'
                self.player_turn.configure(text= f'Player {self.player} turn')

    def reset(self):
        self.moves = 0
        self.create_buttons()
        

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0].cget("text") == self.buttons[i][1].cget("text") == self.buttons[i][2].cget("text") != "":
                return True
            if self.buttons[0][i].cget("text") == self.buttons[1][i].cget("text") == self.buttons[2][i].cget("text") != "":
                return True
        if self.buttons[0][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][2].cget("text") != "":
            return True
        if self.buttons[0][2].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][0].cget("text") != "":
            return True
        return False
        
class TTTLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        super().__init__(master = parent, text=text, font = ("Calibri", 40))
        self.grid(row = 0, column = 1, columnspan = 3, sticky = 'nsew')

class ResetButton(ctk.CTkButton):
    def __init__(self, parent, func, text):
        super().__init__(
            master=parent,
            command = func,
            text = text,
            font = ("Calibri", 15)
            )
        self.grid(
            column = 2, 
            row = 4
            )
      

class TTTButton(ctk.CTkButton):
    def __init__(self, parent, func, text, col, row):
        super().__init__(
            master=parent,
            command = func,
            text = text,
            width=100,
            height=100,
            font = ("Calibri", 25)
            )
        self.grid(
            column = col, 
            row = row, 
            sticky = 'nswe',
            padx = 0.5,
            pady = 0.5
            )


if __name__ == "__main__":
    App()