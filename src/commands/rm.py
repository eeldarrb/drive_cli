from googleapiclient.http import HttpError
from drive_tree import tree_utils


def handle_rm(session, item_name):
    try:
        client = session.client
        curr_dir = session.cwd
        item = tree_utils.get_item_by_name(session, item_name)
        if not item:
            print(f"no such item: {item_name}")
            return
        client.delete_item(item.id)
        for node in curr_dir.children:
            if node.name == item_name:
                curr_dir.remove_child(node)
                break
    except HttpError as e:
        print(f"Failed to delete {item_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
