import os


def handle_clear():
    os.system("cls" if os.name == "nt" else "clear")
