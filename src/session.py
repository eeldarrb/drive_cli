import shlex
from commands import command_map
from auth.google_auth import get_auth_service
from drive_tree.drive_tree import build_drive_tree
from services.drive_client import DriveClient
from google.auth.exceptions import GoogleAuthError


class Session:
    def __init__(self):
        try:
            self.client = DriveClient(get_auth_service)
            self.drive_tree = build_drive_tree(self.client)
            self.cwd = self.drive_tree
        except GoogleAuthError:
            raise GoogleAuthError("Drive authentication failed.")
        except Exception:
            raise RuntimeError("Session initialization failed.")

    def cli_loop(self):
        try:
            while True:
                user_line = input("> ").strip()
                if not user_line:
                    continue

                cmd, *args = shlex.split(user_line)
                cmd_info = command_map.get(cmd)
                # TODO: add fuzzy match suggestion message for commands?
                if not cmd_info:
                    print(f"Command not found: {cmd}")
                    continue

                expected_args = cmd_info.get("args", [])

                if len(args) != len(expected_args):
                    usage = cmd_info.get("usage")
                    print(f"Usage: {cmd} {usage}")
                    continue

                handler = cmd_info.get("handler")
                if handler:
                    kwargs = dict(zip(expected_args, args))
                    handler(self, **kwargs)

        except KeyboardInterrupt:
            print("\nExiting.")
