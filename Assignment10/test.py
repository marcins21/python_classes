import tkinter as tk
import random


class Gui:
    def __init__(
        self,
        window_width: int = 1000,
        window_height: int = 400,
        result_window_width: int = 1000,
        result_window_height: int = 150,
        background_color: str = "#9872b2",
        title: str = "Rzut kostka",
    ):
        self.window_width = window_width
        self.window_height = window_height
        self.result_window_height = result_window_height
        self.result_window_width = result_window_width
        self.result_background_color_hex = background_color
        self.title = title
        self.main = tk.Tk()

    def create_window(self):
        self.main.title(self.title)
        self.main.geometry(f"{self.window_width}x{self.window_height}")
        self.label = tk.Label(self.main, font=("Arial", 150))
        button_to_throw = tk.Button(
            self.main,
            text=self.title,
            height=self.result_window_height,
            width=self.result_window_width.real,
            bg=self.result_background_color_hex,
            command=self.result,
        )
        button_to_throw.pack()
        self.main.mainloop()

    def result(self):
        throw = random.randrange(1, 7)
        self.label.configure(text=f"Wynik Rzutu: {throw}")
        self.label.pack()



# pink #e172b2
# blue #6972b2
#config
game = Gui(
    window_width=1350,
    window_height=500,
    result_window_width=200,
    result_window_height=20,
    background_color="#6972b2",
    title="Rzut",
)
game.create_window()
