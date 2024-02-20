import os
import numpy
import pygame
import customtkinter
from tkinter import messagebox


class App:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.title: str = title
        self.width: int = width
        self.height: int = height

    def run(self) -> None:
        app: customtkinter.CTk = customtkinter.CTk()
        self.font: customtkinter.CTkFont = customtkinter.CTkFont("Helvetica", 25, "bold")

        gridPanel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            app, bg_color="transparent"
        )

        self.createGrid(gridPanel)
        self.chunkSize: int = 9
        self.calls: int = 0
        self.breakSolve: int = 0

        resolveGrid: customtkinter.CTkButton = customtkinter.CTkButton(
            app,
            text="Résoudre la Grille",
            corner_radius=32,
            width=300,
            height=50,
            font=self.font,
            command=lambda: self.returnGrid(),
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

                entry.grid(row=row, column=column, ipadx=5, ipady=5, padx=pad_x, pady=pad_y)

                self.entries.append(entry)

    def getGrid(self) -> None:
        self.grid: list = []
        entry: customtkinter.CTkEntry
        for entry in self.entries:
            if self.isEntryValid(entry):
                self.grid.append(int(entry.get()))
            elif entry.get() == "":
                self.grid.append(0)
            else:
                messagebox.showerror(
                    "ERREUR",
                    "Vous ne pouvez rentrer que des nombres "
                    + "entre 1 et 9 !",
                )
                
                self.grid = []
                return None

        self.grid = self.splitGrid(self.grid)
        self.grid = [array.tolist() for array in self.grid]

    def splitGrid(self, grid: list) -> list:
        return numpy.array_split(grid, int(len(grid) / self.chunkSize))

    def isEntryValid(self, entry: customtkinter.CTkEntry) -> bool:
        if entry.get().isdigit() and int(entry.get()) > 0 and int(entry.get()) < 10:
            return True
        return False

    def printGrid(self, grid: list):
        for x in range(9):
            for y in range(9):
                print(grid[x][y], end=" ")
            print("\n")

    def resolveGrid(self, grid: list, row: int, col: int, num: int) -> bool:
        for x in range(9):
            if grid[row][x] == num:
                return False

        for x in range(9):
            if grid[x][col] == num:
                return False

        startRow: float = row - row % 3
        startCol: float = col - col % 3

        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def runResolve(self, grid: list, row: int, col: int) -> bool:
        if (row == 9 - 1 and col == 9):
            return True
        if col == 9:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.runResolve(grid, row, col + 1)
        for num in range(1, 10, 1):
            if self.resolveGrid(grid, row, col, num):
                grid[row][col] = num
            if self.runResolve(grid, row, col + 1):
                return True
        return False

    def returnGrid(self) -> None:
        self.getGrid()
        if self.runResolve(self.grid, 0, 0):
            self.printGrid(self.grid)
        else:
            print("No Solution :(")
