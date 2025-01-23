"""
custom tkinter Project - Blackjack
Emil & Phillip
19.12.2024

https://github.com/MOD0912/Blackjack?tab=readme-ov-file#blackjack
"""
import random
from http.client import responses

import customtkinter as ctk
import CTkMessagebox as msgbox
import PIL
from PIL import Image, ImageTk
import os
import pywinstyles

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
        print(card)
        card_value = self.get_card_value(card, person)
        self.person_values[person] += card_value
        return card

        #return f"{card[1:]} of {self.colors[card[0]]}"
    def reset_game(self):
        self.deck = []
        self.person_values = {"Player":0, "Dealer":0}
        self.decks_shuffle()


class GameFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Blackjack")
        self.geometry("1920x1080")
        self.game = Game()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        '''
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        '''
        self.grid_rowconfigure(0, weight=1)

        self.bgimage = PIL.Image.open("Bg.jpg")
        self.bg_image = ctk.CTkImage(self.bgimage, size=(1920, 1080))

        self.game_frame = GameFrame(master=self)
        self.game_frame.grid(row=0, column=0, rowspan=2, columnspan=6, sticky="nsew")

        self.bg_lbl = ctk.CTkLabel(master=self, text="", image=self.bg_image)
        self.bg_lbl.grid(row=0, column=0, rowspan=2, columnspan=6, sticky="nsew")

        self.button_hit = ctk.CTkButton(master=self, text="Hit", command=self.hit_function)
        self.button_stand = ctk.CTkButton(master=self, text="Stand", command=self.stand_function)
        self.button_quit = ctk.CTkButton(master=self, text="Quit", command=self.quit_function)

        self.player_frame = ctk.CTkFrame(self)
        self.dealer_frame = ctk.CTkFrame(self)
        self.player_value_label = ctk.CTkLabel(self, text="Player: 0")
        self.dealer_value_label = ctk.CTkLabel(self, text="Dealer: 0")


        self.player_value_label.grid(row=2, column=0, columnspan=3, sticky="sew")
        self.dealer_value_label.grid(row=0, column=0, columnspan=3, sticky="new")
        self.player_frame.grid(row=3, column=0, columnspan=3, sticky="new")
        self.dealer_frame.grid(row=0, column=0, columnspan=3, sticky="new", pady=28)
        #pywinstyles.set_opacity(self.player_frame, value=0.5, color="#000001")
        #pywinstyles.set_opacity(self.dealer_frame, value=0.5, color="#000001")

        self.button_hit.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.button_stand.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        self.button_quit.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

    def load_card_image(self, card):
        card_path = f"cards/{card}.png"

        if not os.path.exists(card_path):
            print(f"Warning: Image not found for card {card}")
            return None

        image = Image.open(card_path)
        #image = ctk.CTkImage(image, size=(100, 150))
        image = image.resize((300, 600))
        #return ImageTk.PhotoImage(image)
        return image

    def display_card(self, person, card):
        image = self.load_card_image(card)
        if image:
            if person == "Player":
                lbl = ctk.CTkLabel(self.player_frame, image=ctk.CTkImage(image,size=(100,150)), text="")
                self.player_value_label.configure(text=f"Player: {self.game.person_values['Player']}")

            else:
                lbl = ctk.CTkLabel(self.dealer_frame, image=ctk.CTkImage(image,size=(100,150)), text="")
                self.dealer_value_label.configure(text=f"Dealer: {self.game.person_values['Dealer']}")
            lbl.image = image
            lbl.pack(side="left")

    def hit_function(self):
        card = self.game.pull_card("Player")
        self.display_card("Player", card)
        print(self.game.person_values["Player"])

        if self.game.person_values["Player"] > 21:

            self.end_card("lose")

    def stand_function(self):
        while self.game.person_values["Dealer"] < 16:
            card = self.game.pull_card("Dealer")
            self.display_card("Dealer", card)

        if self.game.person_values["Dealer"] > 21:
            self.end_card("win")
        elif self.game.person_values["Dealer"] > self.game.person_values["Player"]:
            self.end_card("lose")
        elif self.game.person_values["Dealer"] == self.game.person_values["Player"]:
            self.end_card("tie")
        else:
            self.end_card("lose")

    def end_card(self,state):
        if state == "win":
            message = "You won, Dealer busted"
        elif state == "lose":
            message = "You lost, Dealer won"
        elif state == "tie":
            message = "It's a tie"
        else:
            print(state)
            raise ValueError("Invalid state")


        msg = msgbox.CTkMessagebox(title="Game Over", message=message, options=["Play again", "Quit"])
        response = msg.get()

        if response == "Play again":
            for c in self.player_frame.winfo_children():
                c.destroy()
            for c in self.dealer_frame.winfo_children():
                c.destroy()
            self.player_value_label.configure(text="Player: 0")
            self.dealer_value_label.configure(text="Dealer: 0")
            self.game.reset_game()
        elif response == "Quit":
            self.quit_function()

    def quit_function(self):
        quit()

app = App()
app.mainloop()
