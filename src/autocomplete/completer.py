import os
import shlex
import gnureadline as readline


def create_completer(vfs, command_map):
    completions = []

    def completer(text, state):
        nonlocal completions

        if state == 0:
            completions = []
            line_buffer = readline.get_line_buffer().lstrip()
            cmd, *args = shlex.split(line_buffer) if line_buffer else [""]

            if not (args or line_buffer.endswith(" ")):
                completions = [
                    f"{command_name} "
                    for command_name in command_map.keys()
                    if command_name.startswith(text)
                ]

            else:
                path = text
                dirname = os.path.dirname(path) or "."
                basename = os.path.basename(path)

                try:
                    require_dir = cmd == "cd"

                    resolved_node = vfs._resolve_node_by_path(dirname)
                    candidate_nodes = resolved_node.children

                    for candidate_node in candidate_nodes:
                        if require_dir and not candidate_node.is_folder():
                            continue
                        elif candidate_node.name.startswith(basename):
                            if os.path.dirname(path) == "":
                                completion = candidate_node.name
                            else:
                                completion = os.path.join(dirname, candidate_node.name)
                            completions.append(
                                completion
                                + ("/" if candidate_node.is_folder() else " ")
                            )

                except (FileNotFoundError, NotADirectoryError):
                    completions = []

        try:
            return completions[state]
        except IndexError:
            return None

    return completer
