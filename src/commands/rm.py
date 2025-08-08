import argparse


def handle_rm(session, *args):
    parser = argparse.ArgumentParser(prog="rm")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    file_path = parsed.file_name
    session.drive_tree.rm(file_path)
