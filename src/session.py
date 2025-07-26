import shlex
from commands import command_map
from auth.google_auth import get_auth_service
from drive_tree.drive_tree import build_drive_tree
from services.drive_client import DriveClient
from google.auth.exceptions import GoogleAuthError
from googleapiclient.http import HttpError
from rapidfuzz import process


class Session:
    INPUT_FUZZY_MATCH_THRESHOLD = 80

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

                if not cmd_info:
                    print(f"Command not found: '{cmd}'")
                    best_match, score, _ = process.extractOne(cmd, command_map.keys())
                    if score > self.INPUT_FUZZY_MATCH_THRESHOLD:
                        print(f"Did you mean '{best_match}'?")
                    continue

                expected_args = cmd_info.get("args", [])
                if len(args) != len(expected_args):
                    usage = cmd_info.get("usage")
                    print(f"Usage: {cmd} {usage}")
                    continue

                try:
                    handler = cmd_info.get("handler")
                    kwargs = dict(zip(expected_args, args))
                    if handler:
                        handler(self, **kwargs)
                except FileNotFoundError as e:
                    print(f"[Not Found] Command '{cmd}': No such item: {e}")
                except HttpError as e:
                    print(
                        f"[Drive HTTP Error] Command '{cmd}': API responded with status: {e.status_code}"
                    )
                except Exception as e:
                    print(f"[Unexpected Error] Command '{cmd}': {e}")

        except Exception:
            raise RuntimeError("Encountered an issue during runtime")
