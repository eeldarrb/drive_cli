from .download import handle_download
from .upload import handle_upload
from .rm import handle_rm
from .ls import handle_ls
from .clear import handle_clear
from .mkdir import handle_mkdir
from .cd import handle_cd

command_map = {
    "cd": {"handler": handle_cd},
    "ls": {"handler": handle_ls},
    "clear": {"handler": handle_clear},
    "mkdir": {"handler": handle_mkdir},
    "rm": {"handler": handle_rm},
    "download": {"handler": handle_download},
    "upload": {"handler": handle_upload},
}
