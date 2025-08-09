import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="cd")
    parser.add_argument("path")
    parsed = parser.parse_args(args)

    session.drive_tree.cd(parsed.path)
