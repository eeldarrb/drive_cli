import argparse


def handle_download(session, *args):
    parser = argparse.ArgumentParser(prog="download")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    client = session.client
    file_path = parsed.file_name

    file = session.drive_tree.get_node_by_path(session.cwd, file_path)
    client.download_file(file.id, file.name, file.mime_type)
