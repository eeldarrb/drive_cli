import argparse


def handle_mkdir(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("path")
    parsed = parser.parse_args(args)

    session.vfs.mkdir(parsed.path)
