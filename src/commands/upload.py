import os
import argparse
from drive_tree.drive_node import DriveNode


def handle_upload(session, *args):
    parser = argparse.ArgumentParser(prog="upload")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_path = parsed.file_name
    client = session.client
    curr_dir = session.drive_tree.cwd

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    uploaded_file = client.upload_file(file_path, curr_dir.id)
    uploaded_file_node = DriveNode(
        uploaded_file.get("id"),
        uploaded_file.get("name"),
        uploaded_file.get("mimeType"),
    )
    curr_dir.add_child(uploaded_file_node)
    print(f"Successfully uploaded: {uploaded_file.get('name')}")
