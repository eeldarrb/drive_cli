import argparse


def handle_ls(session, *args):
    parser = argparse.ArgumentParser(prog="ls")
    parsed = parser.parse_args(args)

    for item in session.cwd.children:
        print(item.name)
