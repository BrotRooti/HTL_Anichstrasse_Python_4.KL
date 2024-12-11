import customtkinter as ctk
import CTkMessagebox


class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"
        self.reset_game()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False

    def make_move(self, i, j):
        if self.game_over or self.board[i][j] != "":
            return False

        self.board[i][j] = self.current_player
        if self.check_winner():
            self.game_over = True
            return f"Player {self.current_player} wins!"
        elif self.check_draw():
            self.game_over = True
            return "It's a draw!"
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            return f"Player {self.current_player}'s turn"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True


class TicTacToeUI(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.game = TicTacToeGame()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[ctk.CTkButton for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = ctk.CTkButton(self, text="", width=100, height=100, command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = ctk.CTkButton(self, text="Reset", command=self.reset_game, font=("Arial", 24))
        self.reset_button.grid(row=3, column=0, columnspan=3)

        self.status_label = ctk.CTkLabel(self, text="Player X's turn", font=("Arial", 24))
        self.status_label.grid(row=4, column=0, columnspan=3)

    def reset_game(self):
        self.game.reset_game()
        self.status_label.configure(text="Player X's turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state=ctk.NORMAL)

    def on_button_click(self, i, j):
        old_player = self.game.current_player
        result = self.game.make_move(i, j)
        if result:
            self.buttons[i][j].configure(text=old_player, state=ctk.DISABLED, font=("Arial", 72))

            if result.endswith("wins!") or result.endswith("draw!"):
                CTkMessagebox.CTkMessagebox(message=result, title="Game Over")

            else:
                self.status_label.configure(text=result)

            if self.game.game_over:
                self.disable_buttons()

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(state=ctk.DISABLED)







if __name__ == "__main__":
    root = ctk.CTk()
    app = TicTacToeUI(master=root)
    root.mainloop()

