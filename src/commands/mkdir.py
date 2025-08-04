import argparse
from drive_tree.drive_node import DriveNode


def handle_mkdir(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    client = session.client
    directory_path = parsed.directory_name
    directory_path_parts = directory_path.rstrip("/").split("/")
    path_to_dir = "/".join(directory_path_parts[0:-1])
    directory_name = directory_path_parts[-1]

    resolved_path = session.drive_tree.get_node_by_path(session.cwd, path_to_dir)

    created_folder = client.create_dir(directory_name, resolved_path.id)
    new_dir = DriveNode(
        created_folder.get("id"),
        created_folder.get("name"),
        created_folder.get("mimeType"),
    )
    resolved_path.add_child(new_dir)
