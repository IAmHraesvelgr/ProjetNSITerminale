import customtkinter
import tkinter
import datetime
# https://stackoverflow.com/questions/24374620/python-loop-to-run-for-certain-amount-of-seconds

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