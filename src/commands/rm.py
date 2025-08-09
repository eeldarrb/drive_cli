import argparse


def handle_rm(session, *args):
    parser = argparse.ArgumentParser(prog="rm")
    parser.add_argument("path")
    parsed = parser.parse_args(args)

    session.drive_tree.rm(parsed.path)
