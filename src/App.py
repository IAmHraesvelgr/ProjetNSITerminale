import customtkinter

"""
return 10 if colonne - 1 == 3 or colonne == 6 or colonne - 1 == 9 else 0
return 10 if ligne -1 == 3 or ligne == 6 or ligne - 1 == 9 else 0
"""
class App:

    def __init__(self) -> None:
        pass

    @staticmethod
    def gridPaddingX(column) -> int:
        return 10 if (column - 1 == 3 or column + 3 == 9) else 0
    
    @staticmethod
    def gridPaddingY(row) -> int:
        return 10 if (row - 1 == 3 or row + 3 == 9) else 0 

    @staticmethod
    def createGrid(panel) -> None:
        global input
        input = []
        
        for ligne in range(1, 10):
            for colonne in range(1, 10):
                inputField = customtkinter.CTkEntry(panel, width=70, height=70, font=customtkinter.CTkFont("Arial", 50, 'bold'), border_width=2.5, corner_radius=0).grid(row=ligne, column=colonne, padx=App.gridPaddingX(colonne), pady=App.gridPaddingY(ligne))

                input.append(inputField)
                print(f"Row : {ligne}\nColomn : {colonne}\n")
        

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