import os


def handle_clear(session):
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception as e:
        print(f"[Unexpected Error] Command 'clear' failed: {e}")
