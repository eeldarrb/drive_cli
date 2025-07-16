from drive_tree import tree_utils


def handle_download(session, item_name):
    client = session.client

    item = tree_utils.get_item_by_name(session, item_name)
    if not item:
        print(f"No such item: {item_name}")
        return

    download_success = client.download_file(item.id, item.name, item.mime_type)
    if not download_success:
        print(f"Failed to download: {item_name}")
        return
