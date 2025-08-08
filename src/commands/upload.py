import argparse


def handle_upload(session, *args):
    parser = argparse.ArgumentParser(prog="upload")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_path = parsed.file_name
    session.drive_tree.upload(file_path)
