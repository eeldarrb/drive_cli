import argparse
from drive_tree.drive_node import DriveNode


def handle_mkdir(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    client = session.client
    input_path = parsed.directory_name.rstrip("/")

    *parent_path_segments, dir_name = input_path.split("/")
    parent_path = "/".join(parent_path_segments) if parent_path_segments else "."

    parent_node = session.drive_tree.get_node_by_path(session.cwd, parent_path)

    created_folder = client.create_dir(dir_name, parent_node.id)
    new_dir = DriveNode(
        created_folder.get("id"),
        created_folder.get("name"),
        created_folder.get("mimeType"),
    )
    parent_node.add_child(new_dir)
