import shlex
from http import HTTPStatus

from google.auth.exceptions import GoogleAuthError
from googleapiclient.http import HttpError
from rapidfuzz import process

from auth.google_auth import get_auth_service
from autocomplete import create_completer, setup_autocomplete
from commands import command_map
from services.drive_client import DriveClient
from vfs.drive_node import DriveNode
from vfs.vfs import VFS


class Session:
    INPUT_FUZZY_MATCH_THRESHOLD = 80

    def __init__(self):
        try:
            self.client = DriveClient(get_auth_service)
            self.vfs = VFS(self.client, DriveNode)
        except GoogleAuthError:
            raise GoogleAuthError("Drive authentication failed.")
        except Exception:
            raise RuntimeError("Session initialization failed.")

    def cli_loop(self):
        setup_autocomplete(create_completer(self.vfs, command_map))
        try:
            while True:
                user_line = input(f"{self.vfs.cwd.get_path()} > ").strip()
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

                try:
                    handler = cmd_info.get("handler")
                    if handler:
                        handler(self, *args)
                except FileNotFoundError as e:
                    print(
                        f"[Not Found] Command '{cmd}': No such file or directory: {e}"
                    )
                except NotADirectoryError as e:
                    print(f"[Error] Command '{cmd}': Not a directory: {e}")
                except HttpError as e:
                    error_code = e.status_code
                    print(
                        f"[API Error] Command '{cmd}': Server responded with an error: {error_code} {HTTPStatus(error_code).phrase}"
                    )
                except SystemExit:
                    continue
                except Exception as e:
                    print(f"[Unexpected Error] Command '{cmd}': {e}")

        except Exception:
            raise RuntimeError("Encountered an issue during runtime")
