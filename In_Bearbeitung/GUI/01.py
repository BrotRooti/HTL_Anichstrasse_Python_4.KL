"""
First custom tkinter Frame
Nov. 24
Phillip
"""

import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=40, pady=20, sticky="nsew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=40, pady=(0, 20), sticky="sw")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=2, column=0, padx=90, pady=(0, 90), sticky="sw")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()