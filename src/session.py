from commands import command_map
from auth.google_auth import get_auth_service
from services.drive_client import DriveClient


def cli_loop():
    try:
        client = DriveClient(get_auth_service)
        while True:
            user_line = input("> ").strip()
            if not user_line:
                continue

            cmd, *args = user_line.split()
            if cmd in command_map:
                handler = command_map[cmd]
                handler(client, *args)
            else:
                print(f"drive_cli: command not found: {cmd}")
    except KeyboardInterrupt:
        print("\nExiting...")
