import argparse


def handle_mkdir(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    input_path = parsed.directory_name
    session.drive_tree.mkdir(input_path)
