import argparse


def handle_download(session, *args):
    parser = argparse.ArgumentParser(prog="download")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_path = parsed.file_name
    session.drive_tree.download(file_path)
