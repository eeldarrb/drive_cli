from drive_tree import tree_utils
from googleapiclient.http import HttpError


def handle_download(session, item_name):
    try:
        client = session.client

        item = tree_utils.get_item_by_name(session, item_name)
        if not item:
            print(f"No such item: {item_name}")
            return

        client.download_file(item.id, item.name, item.mime_type)
    except HttpError as e:
        print(f"Failed to download {item_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
