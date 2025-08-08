import argparse


def handle_upload(session, *args):
    parser = argparse.ArgumentParser(prog="upload")
    parser.add_argument("local_path")
    parsed = parser.parse_args(args)

    session.drive_tree.upload(parsed.local_path)
