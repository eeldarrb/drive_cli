import os
import argparse
from drive_tree.drive_node import DriveNode


def handle_upload(session, *args):
    parser = argparse.ArgumentParser(prog="upload")
    parser.add_argument("item_name")
    parsed = parser.parse_args(args)

    file_path = parsed.item_name
    client = session.client
    curr_dir = session.cwd

    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    uploaded_item = client.upload_file(file_path, curr_dir.id)
    uploaded_item_node = DriveNode(
        uploaded_item.get("id"),
        uploaded_item.get("name"),
        uploaded_item.get("mimeType"),
    )
    curr_dir.add_child(uploaded_item_node)
    print(f"Successfully uploaded: {uploaded_item.get('name')}")
