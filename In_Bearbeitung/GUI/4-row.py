import customtkinter as ctk
import CTkMessagebox


class TicTacToeGame:
    def __init__(self):
        self.current_player = "X"
        self.reset_game()
        self.game_over = False

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False

    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != "":
            return False

        self.board[row][col] = self.current_player
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


class TicTacToeUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.game = TicTacToeGame()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[ctk.CTkButton for _ in range(3)] for _ in range(3)]
        self.rowconfigure((0, 1, 2,), weight=8)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = ctk.CTkButton(self, text=" ", width=100, height=100 , command=lambda row=row, col=col: self.on_button_click(row, col))
                self.buttons[row][col].grid( row=row, column=col, padx=5, pady=5, sticky="nsew")

        self.reset_button = ctk.CTkButton(self, text="Reset",fg_color="red" ,command=self.reset_game, font=("Arial", 24))
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="ns")

        self.status_label = ctk.CTkLabel(self, text="Player X's turn", font=("Arial", 24))
        self.status_label.grid(row=4, column=0, columnspan=3)

    def reset_game(self):
        self.game.reset_game()
        self.status_label.configure(text="Player X's turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(text="", state=ctk.NORMAL)

    def on_button_click(self, row, col):
        old_player = self.game.current_player
        result = self.game.make_move(row, col)
        if result:
            self.buttons[row][col].configure(text=old_player, text_color_disabled="black", state=ctk.DISABLED, font=("Arial", 72, "bold"))

            if result.endswith("wins!") or result.endswith("draw!"):
                CTkMessagebox.CTkMessagebox(message=result, title="Game Over")

            else:
                self.status_label.configure(text=result)

            if self.game.game_over:
                self.disable_buttons()

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].configure(state=ctk.DISABLED)







if __name__ == "__main__":
    app = TicTacToeUI()
    app.mainloop()

