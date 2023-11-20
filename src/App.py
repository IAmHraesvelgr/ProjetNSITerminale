import customtkinter
import tkinter
# https://stackoverflow.com/questions/68784493/show-text-or-button-for-specific-time-in-tkinter

class App:

    def __init__(self) -> None:
        pass

    @staticmethod
    def createGrid(panel) -> None:
        for column in range(9):
            for row in range(9):
                inputField = customtkinter.CTkEntry(panel, width=70, height=70, font=customtkinter.CTkFont("Arial", 50, 'bold'))
                inputField.grid(row=row, column=column)

    @staticmethod
    def new(title, width, height) -> None:

        app = customtkinter.CTk()
        gridPanel = customtkinter.CTkFrame(app)

        App.title = title
        App.width = width
        App.height = height
        
        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel = customtkinter.CTkLabel(app, font=customtkinter.CTkFont("Arial", 25, 'bold'), text="Entrez la grille de Sudoku à résoudre : ")  
    
        App.createGrid(gridPanel)

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=50)
        app.mainloop()