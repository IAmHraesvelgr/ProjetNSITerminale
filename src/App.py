import customtkinter

class App:

    def __init__(self) -> None:
        pass

    @staticmethod
    def resolveGrid() -> None:
        pass

    @staticmethod
    def gridPadding(padding) -> int:
        return 10 if padding - 1 == 3 or padding + 3 == 9 else 0

    @staticmethod
    def createGrid(panel) -> None:
        App.entries = []
        
        for row in range(9):
            for column in range(9):
                entry = customtkinter.CTkEntry(panel, width=60, height=60, font=customtkinter.CTkFont("Arial", 50, 'bold'), border_width=2.5, corner_radius=0, justify="center")
            
                pad_x = (0, 0)
                pad_y = (0, 0)

                if (column + 1) % 3 == 0 and (column + 1) < 9:
                    pad_x = (0, 10)
            
                if (row + 1) % 3 == 0 and (row + 1) < 9:
                    pad_y = (0, 10)

                entry.grid(row=row, column=column, ipadx=5, ipady=5, padx=pad_x, pady=pad_y)

                App.entries.append(entry)
        

    @staticmethod
    def new(title, width, height) -> None:

        app = customtkinter.CTk()
        gridPanel = customtkinter.CTkFrame(app)
        resolveGrid = customtkinter.CTkButton(app, text="Résoudre la Grille", width=300, height=50, font=customtkinter.CTkFont("Helvetica", 25, 'bold'), command=resolveGrid)

        App.title = title
        App.width = width
        App.height = height
        
        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel = customtkinter.CTkLabel(app, font=customtkinter.CTkFont("Arial", 25, 'bold'), text="Entrez la grille de Sudoku à résoudre : ")  
    
        App.createGrid(gridPanel)

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=35)
        resolveGrid.pack(pady=25, side=customtkinter.BOTTOM)

        app.mainloop()