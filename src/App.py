import customtkinter
import tkinter

class App:
    def __init__(self) -> None:
       pass

    @staticmethod
    def new() -> None:
        app = customtkinter.CTk()
        
        app.geometry("1080x720")
        app.title("Projet NSI Terminale")
        app.resizable(False, False)
        
        app.mainloop()