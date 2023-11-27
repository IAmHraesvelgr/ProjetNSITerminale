import tkinter
import customtkinter

class App:

    def __init__(self) -> None:
        pass

    @staticmethod
    def resolveGrid() -> None:
        pass

    @staticmethod
    def createGrid(panel) -> None:
        App.entries = []
        
        for row in range(9):
            for column in range(9):
                entry = customtkinter.CTkEntry(panel, width=55, height=55, font=customtkinter.CTkFont("Helvetica", 50, 'bold'), border_width=2.5, corner_radius=0, justify="center")
            
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
        gridPanel = customtkinter.CTkFrame(app, bg_color="transparent")
        resolveGrid = customtkinter.CTkButton(app, text="Résoudre la Grille", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", width=300, height=50, font=customtkinter.CTkFont("Helvetica", 25,'bold'), command=App.resolveGrid)

        App.title = title
        App.width = width
        App.height = height
        
        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel = customtkinter.CTkLabel(app, font=customtkinter.CTkFont("Helvetica", 25, 'bold'), text="Entrez la grille de Sudoku à résoudre : ")  
    
        App.createGrid(gridPanel)

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=35)

        resolveGrid.pack(pady=20, side=customtkinter.BOTTOM)

        app.mainloop()