import os
import pygame
import customtkinter
from tkinter import messagebox

class App:

    def __init__(self) -> None:
        pass  

    @staticmethod
    def playBackgroundMusic(playMusic: customtkinter.IntVar) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.dirname(os.path.relpath(__file__)) + "/../resources/backgroundmusic.mp3")
        if playMusic.get():
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
        else:
            pygame.mixer.music.stop()

    @staticmethod
    def getGrid() -> None:
        entry: customtkinter.CTkEntry
        grid: list = []
        for entry in App.entries:
            if entry.get().isdigit() and int(entry.get()) > 0 and int(entry.get()) < 10:
               grid.append(int(entry.get()))
            elif entry.get() == "":
                pass
            else:
                messagebox.showerror("Erreur", "ERREUR : Vous ne pouvez rentrer que des nombres entre 1 et 9 !")
                return
        return grid
        
           

    @staticmethod
    def checkGrid() -> None:
        if App.getGrid() != None:
            print(App.getGrid())

    @staticmethod
    def resolveGrid() -> None:
        App.checkGrid()

    @staticmethod
    def createGrid(panel: customtkinter.CTkFrame) -> None:
        App.entries: list = []
        
        for row in range(9):
            for column in range(9):
                entry: customtkinter.CTkEntry = customtkinter.CTkEntry(panel, width=55, height=55, font=customtkinter.CTkFont("Helvetica", 50,'bold'), border_width=2.5, corner_radius=0, justify="center")
            
                pad_x: tuple = (0, 0)
                pad_y: tuple = (0, 0)

                if (column + 1) % 3 == 0 and (column + 1) < 9:
                    pad_x = (0, 10)
            
                if (row + 1) % 3 == 0 and (row + 1) < 9:
                    pad_y = (0, 10)

                entry.grid(row=row, column=column, ipadx=5, ipady=5, padx=pad_x, pady=pad_y)

                App.entries.append(entry)
        

    @staticmethod
    def new(title: str, width: int, height: int) -> None:  
        app: customtkinter.CTk = customtkinter.CTk()
        App.font: customtkinter.CTkFont = customtkinter.CTkFont("Helvetica", 25,'bold')
        
        gridPanel: customtkinter.CTkFrame = customtkinter.CTkFrame(app, bg_color="transparent")
        resolveGrid: customtkinter.CTkButton = customtkinter.CTkButton(app, text="Résoudre la Grille", corner_radius=32, width=300, height=50, font=App.font, command=App.resolveGrid)
        
        playMusic: customtkinter.IntVar = customtkinter.IntVar(app, 1)
        App.playBackgroundMusic(playMusic)
        musicButton: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(app, text="Musique", onvalue=1, offvalue=0, variable=playMusic, command=lambda shouldPlayMusic=playMusic: App.playBackgroundMusic(shouldPlayMusic))

        App.title: int = title
        App.width: int = width
        App.height: int = height
        
        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel: customtkinter.CTkLabel = customtkinter.CTkLabel(app, font=App.font, text="Entrez la grille de Sudoku à résoudre : ")  
    
        App.createGrid(gridPanel)

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=35)

        resolveGrid.pack(pady=20, side=customtkinter.BOTTOM)
        musicButton.pack(side=customtkinter.RIGHT)

        if os.name == "nt":
            import pywinstyles
            pywinstyles.apply_style(app, "optimised")
            
        app.mainloop()