from drive_tree.drive_node import DriveNode
from googleapiclient.http import HttpError


def handle_upload(session, file_path):
    client = session.client
    curr_dir = session.cwd

    try:
        uploaded_item = client.upload_file(file_path, curr_dir.id)
        uploaded_item_node = DriveNode(
            uploaded_item.get("id"),
            uploaded_item.get("name"),
            uploaded_item.get("mimeType"),
        )
        curr_dir.add_child(uploaded_item_node)
        print(f"Successfully uploaded: {uploaded_item.get('name')}")
    except HttpError as e:
        print(f"Failed to upload: {e}")
