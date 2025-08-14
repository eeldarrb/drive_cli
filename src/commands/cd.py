import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="cd")
    parser.add_argument("path", nargs="?", default="/")
    parsed = parser.parse_args(args)

    session.vfs.cd(parsed.path)
