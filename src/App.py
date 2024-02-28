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
        self.font: customtkinter.CTkFont = customtkinter.CTkFont(
            "Helvetica", 25, "bold"
        )

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
            command=lambda: self.runSolver(),
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

                entry.grid(
                    row=row, column=column, ipadx=5, ipady=5, padx=pad_x, pady=pad_y
                )

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
                    "Vous ne pouvez rentrer que des nombres " + "entre 1 et 9 !",
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

    def printGrid(self, grid: list) -> None:
        for i in range(len(grid)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(len(grid[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(grid[i][j])

                else:
                    print(str(grid[i][j]) + " ", end="")

    def findEmptyCell(self, grid: list) -> tuple | None: 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def resolveGrid(self, grid: list) -> bool:
        find: tuple | None = self.findEmptyCell(grid)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.isGridValid(self.grid, i, (row, col)):
                self.grid[row][col] = i

                if self.resolveGrid(self.grid):
                    return True

                self.grid[row][col] = 0

        return False

    def isGridValid(self, grid: list, number: int, pos: tuple) -> bool:
        for i in range(len(grid[0])):
            if grid[pos[0]][i] == number and pos[1] != i:
                return False

        for i in range(len(grid)):
            if grid[i][pos[1]] == number and pos[0] != i:
                return False

        box_x: int = pos[1] // 3
        box_y: int = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if grid[i][j] == number and (i, j) != pos:
                    return False
        return True

    def runSolver(self):
        self.getGrid()
        self.printGrid(self.grid)
        self.resolveGrid(self.grid)
        print("___________________")
        self.printGrid(self.grid)
