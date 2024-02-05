from App import App
import customtkinter


def main():
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    app = App("Résolveur de Sudoku", 1080, 720)
    app.runApp()


if __name__ == "__main__":
    main()
