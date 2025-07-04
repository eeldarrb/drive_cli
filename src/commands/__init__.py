from commands.download import handle_download
from .rm import handle_rm
from .ls import handle_ls
from .clear import handle_clear
from .mkdir import handle_mkdir

command_map = {
    "ls": handle_ls,
    "clear": lambda _: handle_clear(),
    "mkdir": handle_mkdir,
    "rm": handle_rm,
    "download": handle_download,
}
