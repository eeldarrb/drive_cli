import argparse
from drive_tree.drive_node import DriveNode


def handle_mkdir(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    directory_name = parsed.directory_name
    client = session.client
    curr_dir = session.cwd

    created_folder = client.create_dir(directory_name, curr_dir.id)
    new_dir = DriveNode(
        created_folder.get("id"),
        created_folder.get("name"),
        created_folder.get("mimeType"),
    )
    curr_dir.add_child(new_dir)
