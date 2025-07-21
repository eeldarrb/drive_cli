import sys
from session import Session


if __name__ == "__main__":
    try:
        session = Session()
        session.cli_loop()
    except KeyboardInterrupt:
        print("\nExiting.")
    except Exception as e:
        print(f"[Fatal] Application failed unexpectedly: {e}")
        print("Exiting.")
