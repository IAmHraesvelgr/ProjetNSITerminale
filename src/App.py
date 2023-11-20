import customtkinter
import tkinter
# https://stackoverflow.com/questions/68784493/show-text-or-button-for-specific-time-in-tkinter

class App:

    def __init__(self) -> None:
        pass

    @staticmethod
    def createGrid(app) -> None:
        for column in range(3):
            for row in range(3):
                inputField = customtkinter.CTkEntry(app, width=3, height=3) 
                inputField.grid()  

    @staticmethod
    def new(title, width, height) -> None:

        app = customtkinter.CTk()

        App.title = title
        App.width = width
        App.height = height
        
        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel = customtkinter.CTkLabel(app, font=customtkinter.CTkFont("Arial", 18, 'bold'), text="Entrez la grille de Sudoku à résoudre : ")
        inputLabel.pack(pady=15)  

        # App.createGrid(app)
        app.mainloop()