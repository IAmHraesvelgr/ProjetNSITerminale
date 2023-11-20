import customtkinter
import tkinter
# https://stackoverflow.com/questions/68784493/show-text-or-button-for-specific-time-in-tkinter

class App:
    def __init__(self) -> None:
        pass

    @staticmethod
    def new(title, size) -> None:
        app = customtkinter.CTk()

        App.title = title
        App.size = size
        
        app.title(App.title)
        app.geometry(App.size)
        app.resizable(False, False)
        app.mainloop()   

    @staticmethod
    def createGrid():
        pass     