import os


def handle_clear(session):
	os.system("cls" if os.name == "nt" else "clear")
