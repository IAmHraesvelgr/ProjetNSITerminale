from App import *

def main():
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")
    
    App.new("Projet NSI Terminale", "1080x720")
    App.createGrid()

if __name__ == '__main__':
    main()