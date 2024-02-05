import os
import numpy
import pygame
import customtkinter
from tkinter import messagebox


class App:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.title = title
        self.width = width
        self.height = height

    def runApp(self) -> None:
        app: customtkinter.CTk = customtkinter.CTk()
        self.font: customtkinter.CTkFont = customtkinter.CTkFont("Helvetica", 25, "bold")

        gridPanel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            app, bg_color="transparent"
        )

        self.createGrid(gridPanel)
        self.chunkSize: int = 9
        self.grid = self.getGrid()
        self.grid = [array.tolist() for array in self.grid]
        self.calls: int = 0
        self.breakSolve: int = 0

        self.runResolve = lambda: self.runGridSolver(self.grid)

        resolveGrid: customtkinter.CTkButton = customtkinter.CTkButton(
            app,
            text="Résoudre la Grille",
            corner_radius=32,
            width=300,
            height=50,
            font=self.font,
            command=self.runResolve,
        )

        playMusic: customtkinter.IntVar = customtkinter.IntVar(app, 1)
        self.playBackgroundMusic(playMusic)
        musicButton: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(
            app,
            text="Musique",
            onvalue=1,
            offvalue=0,
            variable=playMusic,
            command=lambda shouldPlayMusic=playMusic: self.playBackgroundMusic(
                shouldPlayMusic
            ),
        )

        self.grid: list = []

        app.minsize(self.width, self.height)
        app.title(self.title)
        app.resizable(False, False)

        inputLabel: customtkinter.CTkLabel = customtkinter.CTkLabel(
            app, font=self.font, text="Entrez la grille de Sudoku à résoudre : "
        )

        inputLabel.pack(pady=15)
        gridPanel.pack(pady=35)

        resolveGrid.pack(pady=20, side=customtkinter.BOTTOM)
        musicButton.pack(side=customtkinter.RIGHT)

        if os.name == "nt":
            import pywinstyles

            pywinstyles.apply_style(app, "optimised")

        app.mainloop()

    def playBackgroundMusic(self, playMusic: customtkinter.IntVar) -> None:
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

    def isEntryValid(self, entry: customtkinter.CTkEntry) -> bool:
        if entry.get().isdigit() and int(entry.get()) > 0 and int(entry.get()) < 10:
            return True
        return False

    def getGrid(self) -> list:
        grid: list = []
        entry: customtkinter.CTkEntry
        for entry in self.entries:
            if self.isEntryValid(entry):
                grid.append(int(entry.get()))
            elif entry.get() == "":
                grid.append(0)
            else:
                messagebox.showerror(
                    "Erreur",
                    "ERREUR : Vous ne pouvez rentrer que des nombres "
                    + "entre 1 et 9 !",
                )
                return []

        grid = self.splitGrid(grid)
        return grid

    def splitGrid(self, grid: list) -> list:
        return numpy.array_split(grid, int(len(grid) / self.chunkSize))

    def checkGrid(self, row: int, column: int, number: int, board: list) -> bool:
        if self.getGrid() is None:
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

    def resolveGrid(self, grid: list) -> None:
        self.calls += 1

        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    self.breakSolve = 1
                    self.row: int = i
                    self.column: int = j
                    break

        if self.breakSolve == 0:
            for element in grid:
                print(element)
            exit(0)

        for i in range(10):
            if self.checkGrid(self.row, self.column, i, grid):
                grid[self.row][self.column] = i
                if self.resolveGrid(grid):
                    print(self.grid)
                    return
                grid[self.row][self.column] = 0
        print(self.grid)
        return

    def createGrid(self, panel: customtkinter.CTkFrame) -> None:
        self.entries: list = []

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
                    row=row, column=column, ipadx=5, ipady=5, padx=pad_x, pady=pad_y
                )

                self.entries.append(entry)

    def runGridSolver(self, grid: list) -> None:
        try:
            self.grid: list = self.getGrid()
            self.grid: list = [array.tolist() for array in grid]

        except Exception:
            messagebox.showerror("ERREUR", "Votre grille est invalide !")

        print(self.grid)

        try:
            self.resolveGrid(self.grid)

        except Exception:
            messagebox.showerror("ERREUR", "Impossible de résoudre votre " + "grille !")
