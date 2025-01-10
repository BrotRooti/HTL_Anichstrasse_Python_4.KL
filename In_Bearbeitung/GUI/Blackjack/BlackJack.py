"""
custom tkinter Project - Blackjack
Emil & Phillip
19.12.2024

https://github.com/MOD0912/Blackjack?tab=readme-ov-file#blackjack
"""
import customtkinter as ctk
import random



class Game:
    def __init__(self):
        self.deck = []
        self.person_values = {"Player":0, "Dealer":0}
        self.colors = {"H": "Hearts", "S": "Spades", "C": "Clubs", "D": "Diamonds"}
        self.decks_shuffle()

    def decks_shuffle(self):
        types = ["H", "S", "C", "D"]
        initial_deck = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace"]

        for i in types:
            for card in initial_deck:
                self.deck.append(f"{i}{card}")
        self.deck = self.deck * 6

        random.shuffle(self.deck)

    def get_card_value(self, card, person):
        card_value = card[1:]
        if card_value in ["Jack", "Queen", "King"]:
            return 10
        elif card_value == "Ace":
            if self.person_values[person] + 11 > 21:
                return 1
            else:
                return 11
        else:
            return int(card_value)

    def pull_card(self,person):
        card = self.deck.pop(0)
        card_value = self.get_card_value(card, person)
        self.person_values[person] += card_value

        #return f"{card[1:]} of {self.colors[card[0]]}"


class GameFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Blackjack")
        self.geometry("800x800")
        self.game = Game()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.game_frame = GameFrame(master=self)
        self.game_frame.grid(row=0, column=0, rowspan=2, columnspan=3, sticky="nsew")

        self.button_hit = ctk.CTkButton(master=self, text="Hit", command=self.hit_function)
        self.button_stand = ctk.CTkButton(master=self, text="Stand", command=self.stand_function)
        self.button_quit = ctk.CTkButton(master=self, text="Quit", command=self.quit_function)

        self.button_hit.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.button_stand.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.button_quit.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    def hit_function(self):
        self.game.pull_card("Player")
        print(self.game.person_values["Player"])
        if self.game.person_values["Player"] > 21:
            print("You lost")
            self.game_frame.label.configure(text="You lost")

    def stand_function(self):
        while self.game.person_values["Dealer"] < 16:
            self.game.pull_card("Dealer")
        if self.game.person_values["Dealer"] > 21:
            self.game_frame.label.configure(text="You won")
            print("You won")
        elif self.game.person_values["Dealer"] > self.game.person_values["Player"]:
            print("You lost")
            self.game_frame.label.configure(text="You lost")
        elif self.game.person_values["Dealer"] == self.game.person_values["Player"]:
            print("It's a tie")
            self.game_frame.label.configure(text="It's a tie")
        else:
            print("You won")
            self.game_frame.label.configure(text="You lost")

    def quit_function(self):
        quit()

app = App()
app.mainloop()
