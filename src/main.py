import sys
from session import Session


if __name__ == "__main__":
    try:
        session = Session()
        session.cli_loop()
    except Exception as e:
        print(f"[Fatal] Failed to start app: {e}")
        print("Exiting.")
