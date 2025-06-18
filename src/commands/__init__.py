from .ls import handle_ls
from .clear import handle_clear

command_map = {"ls": handle_ls, "clear": lambda _: handle_clear()}
