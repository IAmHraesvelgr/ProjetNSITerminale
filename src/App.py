import customtkinter

class App:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def gridPaddingX(column) -> int:
        if column == 3 or column + 3 == 9:
            return 10
        return 0
    
    @staticmethod
    def gridPaddingY(row) -> int:
        if row == 3 or row == 9:
            return 10
        return 0

    @staticmethod
    def createGrid(panel) -> None:
        global input
        input = []
        
        for row in range(0, 9):
            for column in range(0, 9):
                inputField = customtkinter.CTkEntry(panel, width=70, height=70, font=customtkinter.CTkFont("Arial", 50, 'bold'), border_width=2.5, corner_radius=0).grid(row=row, column=column, padx=App.gridPaddingX(column), pady=App.gridPaddingY(row))

                input.append(inputField)
                print(f"Row : {row}\nColomn : {column}\n")
        

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