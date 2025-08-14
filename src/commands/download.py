import argparse


def handle_download(session, *args):
    parser = argparse.ArgumentParser(prog="download")
    parser.add_argument("path")
    parsed = parser.parse_args(args)

    session.vfs.download(parsed.path)
