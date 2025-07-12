import shlex
from commands import command_map
from auth.google_auth import get_auth_service
from drive_tree.drive_tree import build_drive_tree
from services.drive_client import DriveClient


class Session:
    def __init__(self):
        self.client = DriveClient(get_auth_service)
        self.drive_tree = build_drive_tree(self.client)
        self.cwd = self.drive_tree

    def cli_loop(self):
        try:
            while True:
                user_line = input("> ").strip()
                if not user_line:
                    continue

                cmd, *args = shlex.split(user_line)
                cmd_info = command_map.get(cmd)
                if not cmd_info:
                    print(f"drive_cli: command not found: {cmd}")
                    continue

                expected_args = cmd_info.get("args", [])
                handler = cmd_info.get("handler")
                if handler:
                    kwargs = dict(zip(expected_args, args))
                    handler(self, **kwargs)

        except KeyboardInterrupt:
            print("\nExiting...")
