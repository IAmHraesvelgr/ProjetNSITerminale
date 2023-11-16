import customtkinter
import tkinter

class App:
    def __init__(self) -> None:
       pass

    @staticmethod
    def new() -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        
        app = customtkinter.CTk()
        app.geometry("1080x720")
        app.title("Projet NSI Terminale")
        app.resizable(False, False)
        app.mainloop()