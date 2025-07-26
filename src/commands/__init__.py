from .download import handle_download
from .upload import handle_upload
from .rm import handle_rm
from .ls import handle_ls
from .clear import handle_clear
from .mkdir import handle_mkdir
from .cd import handle_cd

command_map = {
	"cd": {"handler": handle_cd, "args": ["folder_name"], "usage": "<folder_name>"},
	"ls": {"handler": handle_ls, "args": [], "usage": ""},
	"clear": {"handler": handle_clear, "args": [], "usage": ""},
	"mkdir": {
		"handler": handle_mkdir,
		"args": ["folder_name"],
		"usage": "<folder_name>",
	},
	"rm": {"handler": handle_rm, "args": ["item_name"], "usage": "<item_name>"},
	"download": {
		"handler": handle_download,
		"args": ["item_name"],
		"usage": "<item_name>",
	},
	"upload": {"handler": handle_upload, "args": ["file_path"], "usage": "<file_path>"},
}
