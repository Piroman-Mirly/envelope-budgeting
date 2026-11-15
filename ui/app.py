import tkinter as tk
from ui.frames.menu_frame import MenuFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Расрпеделение денег")
        self.geometry("600x400")
        
        # Чтобы фреймы растягивались на всё окно
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (MenuFrame,):
            frame = F(parent=self, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("MenuFrame")
    def show_frame(self, name):
        self.frames[name].tkraise()