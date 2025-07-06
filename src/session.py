import shlex
from commands import command_map
from auth.google_auth import get_auth_service
from services.drive_client import DriveClient


class Session:
    def __init__(self):
        self.client = DriveClient(get_auth_service)

    def cli_loop(self):
        try:
            while True:
                user_line = input("> ").strip()

                if not user_line:
                    continue
                cmd, *args = shlex.split(user_line)
                if cmd in command_map:
                    handler = command_map[cmd]
                    handler(self, *args)
                else:
                    print(f"drive_cli: command not found: {cmd}")
        except KeyboardInterrupt:
            print("\nExiting...")
