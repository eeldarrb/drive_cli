import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    destination_path = parsed.directory_name
    session.drive_tree.cd(destination_path)
