import os
import numpy
import pygame
import customtkinter
from tkinter import messagebox


class App:
    def __init__(self) -> None:
        pass

    @staticmethod
    def new(title: str, width: int, height: int) -> None:
        app: customtkinter.CTk = customtkinter.CTk()
        App.font: customtkinter.CTkFont = customtkinter.CTkFont("Helvetica",
                                                                25, "bold")

        gridPanel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            app, bg_color="transparent"
        )

        App.createGrid(gridPanel)
        App.chunkSize: int = 9
        App.grid = App.getGrid()
        App.grid = [array.tolist() for array in App.grid]
        App.calls: int = 0
        App.breakSolve: int = 0

        App.runResolve = lambda: App.runGridSolver(App.grid)

        resolveGrid: customtkinter.CTkButton = customtkinter.CTkButton(
            app,
            text="Résoudre la Grille",
            corner_radius=32,
            width=300,
            height=50,
            font=App.font,
            command=App.runResolve,
        )

        playMusic: customtkinter.IntVar = customtkinter.IntVar(app, 1)
        App.playBackgroundMusic(playMusic)
        musicButton: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(
            app,
            text="Musique",
            onvalue=1,
            offvalue=0,
            variable=playMusic,
            command=lambda shouldPlayMusic=playMusic: App.playBackgroundMusic(
                shouldPlayMusic
            ),
        )

        App.title: str = title
        App.width: int = width
        App.height: int = height
        App.grid: list = []

        app.minsize(App.width, App.height)
        app.title(App.title)
        app.resizable(False, False)

        inputLabel: customtkinter.CTkLabel = customtkinter.CTkLabel(
            app, font=App.font, text="Entrez la grille de Sudoku à résoudre : "
        )

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=35)

        resolveGrid.pack(pady=20, side=customtkinter.BOTTOM)
        musicButton.pack(side=customtkinter.RIGHT)

        if os.name == "nt":
            import pywinstyles

            pywinstyles.apply_style(app, "optimised")

        app.mainloop()

    @staticmethod
    def playBackgroundMusic(playMusic: customtkinter.IntVar) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(
            os.path.dirname(os.path.relpath(__file__))
            + "/../resources/backgroundmusic.mp3"
        )
        if playMusic.get():
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
        else:
            pygame.mixer.music.stop()

    @staticmethod
    def isEntryValid(entry: customtkinter.CTkEntry) -> bool:
        if (entry.get().isdigit() and int(entry.get()) > 0
                and int(entry.get()) < 10):
            return True
        return False

    @staticmethod
    def getGrid() -> list:
        grid: list = []
        entry: customtkinter.CTkEntry
        for entry in App.entries:
            if App.isEntryValid(entry):
                grid.append(int(entry.get()))
            elif entry.get() == "":
                grid.append(0)
            else:
                messagebox.showerror(
                    "Erreur",
                    "ERREUR : Vous ne pouvez rentrer que des nombres " +
                    "entre 1 et 9 !",
                )
                return []

        grid = App.splitGrid(grid)
        return grid

    @staticmethod
    def splitGrid(grid: list) -> list:
        return numpy.array_split(grid, int(len(grid) / App.chunkSize))

    @staticmethod
    def checkGrid(row: int, column: int, number: int, board: list) -> bool:
        if App.getGrid() is None:
            messagebox.showerror("Erreur", "Votre grille est vide !")
            return False

        for i in range(9):
            if board[row][i] == number:
                return False

        for i in range(9):
            if board[i][column] == number:
                return False

        row = row - row % 3
        column = column - column % 3

        for i in range(3):
            for j in range(3):
                if board[row + i][column + j] == number:
                    return False
        return True

    @staticmethod
    def resolveGrid(grid: list) -> None:
        App.calls += 1

        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    App.breakSolve = 1
                    App.row: int = i
                    App.column: int = j
                    break

        if App.breakSolve == 0:
            for element in grid:
                print(element)
            exit(0)

        for i in range(10):
            if App.checkGrid(App.row, App.column, i, grid):
                grid[App.row][App.column] = i
                if App.resolveGrid(grid):
                    print(App.grid)
                    return
                grid[App.row][App.column] = 0
        print(App.grid)
        return

    @staticmethod
    def createGrid(panel: customtkinter.CTkFrame) -> None:
        App.entries: list = []

        for row in range(9):
            for column in range(9):
                entry: customtkinter.CTkEntry = customtkinter.CTkEntry(
                    panel,
                    width=30,
                    height=30,
                    font=customtkinter.CTkFont("Helvetica", 30, "bold"),
                    border_width=2,
                    corner_radius=0,
                    justify="center",
                )

                pad_x: tuple = (0, 0)
                pad_y: tuple = (0, 0)

                if (column + 1) % 3 == 0 and (column + 1) < 9:
                    pad_x = (0, 10)

                if (row + 1) % 3 == 0 and (row + 1) < 9:
                    pad_y = (0, 10)

                entry.grid(
                    row=row, column=column, ipadx=5, ipady=5, padx=pad_x,
                    pady=pad_y
                )

                App.entries.append(entry)

    @staticmethod
    def runGridSolver(grid: list) -> None:
        try:
            App.grid: list = App.getGrid()
            App.grid: list = [array.tolist() for array in grid]

        except Exception:
            messagebox.showerror("ERREUR", "Votre grille est invalide !")

        print(App.grid)

        try:
            App.resolveGrid(App.grid)

        except Exception:
            messagebox.showerror("ERREUR", "Impossible de résoudre votre " +
                                 "grille !")
