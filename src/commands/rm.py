import argparse
from drive_tree import tree_utils


def handle_rm(session, *args):
    parser = argparse.ArgumentParser(prog="rm")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_name = parsed.file_name
    client = session.client
    curr_dir = session.cwd

    file = tree_utils.get_file_by_name(session, file_name)
    if not file:
        raise FileNotFoundError(file_name)

    client.delete_file(file.id)

    for node in curr_dir.children:
        if node.name == file_name:
            curr_dir.remove_child(node)
            break
