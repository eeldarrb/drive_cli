from .download import handle_download
from .upload import handle_upload
from .rm import handle_rm
from .ls import handle_ls
from .clear import handle_clear
from .mkdir import handle_mkdir
from .cd import handle_cd

command_map = {
    "cd": handle_cd,
    "ls": handle_ls,
    "clear": lambda _: handle_clear(),
    "mkdir": handle_mkdir,
    "rm": handle_rm,
    "download": handle_download,
    "upload": handle_upload,
}
