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

        grid_panel: customtkinter.CTkFrame = customtkinter.CTkFrame(
            app, bg_color="transparent"
        )

        self.create_grid(grid_panel)
        self.chunk_size: int = 9
        self.calls: int = 0
        self.break_solve: int = 0

        resolve_grid: customtkinter.CTkButton = customtkinter.CTkButton(
            app,
            text="Résoudre la Grille",
            corner_radius=32,
            width=300,
            height=50,
            font=self.font,
            command=lambda: self.run_solver(),
        )

        play_music: customtkinter.IntVar = customtkinter.IntVar(app, 1)
        self.play_background_music(play_music)
        music_button: customtkinter.CTkCheckBox = customtkinter.CTkCheckBox(
            app,
            text="Musique",
            onvalue=1,
            offvalue=0,
            variable=play_music,
            command=lambda should_play_music=play_music: self.play_background_music(
                should_play_music
            ),
        )

        reset_button: customtkinter.CTkButton = customtkinter.CTkButton(
            app,
            text="Réinitialiser",
            font=self.font,
            command=lambda: self.reset_grid()
        )

        app.minsize(self.width, self.height)
        app.title(self.title)
        app.resizable(False, False)

        input_label: customtkinter.CTkLabel = customtkinter.CTkLabel(
            app, font=self.font, text="Entrez la grille de Sudoku à résoudre : "
        )

        input_label.pack(pady=15)
        grid_panel.pack(pady=35)

        resolve_grid.pack(pady=25, side=customtkinter.BOTTOM)
        music_button.pack(side=customtkinter.RIGHT)
        reset_button.pack(side=customtkinter.LEFT, padx=5)

        if os.name == "nt":
            import pywinstyles

            pywinstyles.apply_style(app, "optimised")

        app.mainloop()

    def play_background_music(self, play_music: customtkinter.IntVar) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(
            os.path.dirname(os.path.relpath(__file__))
            + "/../resources/backgroundmusic.mp3"
        )
        if play_music.get():
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
        else:
            pygame.mixer.music.stop()

    def reset_grid(self) -> None:
        entry: customtkinter.CTkEntry
        for entry in self.entries:
            entry.delete(0, customtkinter.END)
            entry.insert(0, "")

    def create_grid(self, panel: customtkinter.CTkFrame) -> None:
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

    def get_grid(self) -> None:
        self.grid: list = []
        entry: customtkinter.CTkEntry
        for entry in self.entries:
            if self.is_entry_valid(entry):
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

        self.grid = self.split_grid(self.grid)
        self.grid = [array.tolist() for array in self.grid]

    def split_grid(self, grid: list) -> list:
        return numpy.array_split(grid, int(len(grid) / self.chunk_size))

    def is_entry_valid(self, entry: customtkinter.CTkEntry) -> bool:
        if entry.get().isdigit() and int(entry.get()) > 0 and int(entry.get()) < 10:
            return True
        return False

    def print_grid(self, grid: list) -> None:
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

    def find_empty_cell(self, grid: list) -> tuple | None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def resolve_grid(self, grid: list) -> bool:
        find: tuple | None = self.find_empty_cell(grid)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.is_grid_valid(self.grid, i, (row, col)):
                self.grid[row][col] = i

                if self.resolve_grid(self.grid):
                    return True

                self.grid[row][col] = 0

        return False

    def is_grid_valid(self, grid: list, number: int, pos: tuple) -> bool:
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

    def format_grid(self, grid: list) -> list:
        return [j for sub in grid for j in sub]

    def show_grid(self, grid: list) -> None:
        entry: customtkinter.CTkEntry
        i: int = 0
        for entry in self.entries:
            entry.delete(0, customtkinter.END)
            entry.insert(0, grid[i])
            i += 1

    def run_solver(self):
        try:
            self.get_grid()
        except:
            messagebox.showerror("Impossible de lire votre grille !")

        self.resolve_grid(self.grid)

        self.grid = self.format_grid(self.grid)
        self.show_grid(self.grid)
