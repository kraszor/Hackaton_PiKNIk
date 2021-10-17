from tkinter import *
from tkinter import font as tkFont


class TicTacToe:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x290")
        self.root.title("TicTacToe")
        helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
        x = 3
        y = 1
        self.buttons = {
            "1": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("1"), font=helv36),
            "2": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("2"), font=helv36),
            "3": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("3"), font=helv36),
            "4": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("4"), font=helv36),
            "5": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("5"), font=helv36),
            "6": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("6"), font=helv36),
            "7": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("7"), font=helv36),
            "8": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("8"), font=helv36),
            "9": Button(self.root, width=x, height=y, text=" ", command=lambda: self.on_click("9"), font=helv36),
        }
        for i in range(9):
            self.buttons[str(i + 1)].grid(row=i // 3, column=i % 3)

        self.current_sign = "X"

    def on_click(self, number):
        self.buttons[number]["text"] = self.current_sign
        self.buttons[number]["state"] = "disabled"
        if self.current_sign == "X":
            self.current_sign = "O"
        else:
            self.current_sign = "X"
        self.update()

    def update(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonals()

    def check_rows(self):
        for i in range(3):
            row = [self.buttons[str(1 + 3 * i)]["text"], self.buttons[str(2 + 3 * i)]["text"],
                   self.buttons[str(3 + 3 * i)]["text"]]
            if row == ["X", "X", "X"]:
                self.end_game("X")
            if row == ["O", "O", "O"]:
                self.end_game("O")

    def check_columns(self):
        for i in range(3):
            row = [self.buttons[str(1 + i)]["text"], self.buttons[str(4 + i)]["text"], self.buttons[str(7 + i)]["text"]]
            if row == ["X", "X", "X"]:
                self.end_game("X")
            if row == ["O", "O", "O"]:
                self.end_game("O")

    def check_diagonals(self):
        for i in range(2):
            row = [self.buttons[str(1 + 6 * i)]["text"], self.buttons[str(5)]["text"],
                   self.buttons[str(9 - 6 * i)]["text"]]
            if row == ["X", "X", "X"]:
                self.end_game("X")
            if row == ["O", "O", "O"]:
                self.end_game("O")

    def end_game(self, winner):
        for i in self.buttons:
            if self.buttons[i]["text"] == winner:
                self.buttons[i]["bg"] = "#45e322"
            self.buttons[i]["state"] = "disabled"


if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
