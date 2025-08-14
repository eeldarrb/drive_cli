import argparse


def handle_rm(session, *args):
    parser = argparse.ArgumentParser(prog="rm")
    parser.add_argument("path")
    parsed = parser.parse_args(args)

    session.vfs.rm(parsed.path)
