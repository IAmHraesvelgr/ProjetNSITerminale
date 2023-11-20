import customtkinter
import tkinter
# https://stackoverflow.com/questions/68784493/show-text-or-button-for-specific-time-in-tkinter

class App:

    @staticmethod
    def new(title, size) -> None:
        app = customtkinter.CTk()

        App.title = title
        App.size = size
        
        app.title(App.title)
        app.geometry(App.size)
        app.resizable(False, False)

        inputLabel = customtkinter.CTkLabel(app, font=customtkinter.CTkFont("Arial", 18, 'bold'), text="Entrez la grille de Sudoku à résoudre : ")
        inputLabel.pack(pady=15)

        app.mainloop()   

    @staticmethod
    def createGrid():
        pass     