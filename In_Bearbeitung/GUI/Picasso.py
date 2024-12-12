"""
Random Ellipse Generator
Phillip
12.12.2024
"""

import customtkinter as ctk
import random


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Random Ellipse Generator")
        self.geometry("800x600")
        self.resizable(False, False)

        self.forms = []

        self.create_widgets()

    def create_widgets(self):

        self.canvas = ctk.CTkCanvas(self, bg="white")
        self.canvas.place(relx=0, rely=0, relwidth=1, relheight=0.9)

        self.create_button = ctk.CTkButton(self, text="Create a Picasso", command=self.create_forms,
                                           font=("Monotype Corsiva", 45))
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.destroy, font=("Monotype Corsiva", 45),
                                         fg_color="red")

        self.create_button.place(anchor="sw", relx=0, rely=1)
        self.exit_button.place(anchor="se", relx=1, rely=1)

    def create_forms(self):
        if self.forms:
            for forms in self.forms:
                self.canvas.delete(forms)
        for _ in range(random.randint(5, 30)):
            x0 = random.randint(0, 980)
            y0 = random.randint(0, 650)
            x1 = random.randint(0, 980)
            y1 = random.randint(0, 650)

            #color = random.choice(["red", "green", "blue", "yellow", "black", "white"])
            color = "#" + "%06x" % random.randint(0, 0xFFFFFF)

            if _ % 3 == 0:
                self.forms.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=color))
            else:
                self.forms.append(self.canvas.create_oval(x0, y0, x1, y1, fill=color))


if __name__ == "__main__":
    app = App()
    app.mainloop()
