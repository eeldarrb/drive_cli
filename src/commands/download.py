import argparse
from drive_tree import tree_utils


def handle_download(session, *args):
    parser = argparse.ArgumentParser(prog="download")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_name = parsed.file_name
    client = session.client

    file = tree_utils.get_file_by_name(session, file_name)
    if not file:
        raise FileNotFoundError(file_name)

    client.download_file(file.id, file.name, file.mime_type)
