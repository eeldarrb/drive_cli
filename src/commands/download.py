import argparse
from drive_tree import tree_utils


def handle_download(session, *args):
    parser = argparse.ArgumentParser(prog="download")
    parser.add_argument("item_name")
    parsed = parser.parse_args(args)

    item_name = parsed.item_name
    client = session.client

    item = tree_utils.get_item_by_name(session, item_name)
    if not item:
        raise FileNotFoundError(item_name)

    client.download_file(item.id, item.name, item.mime_type)
