import argparse


def handle_ls(session, *args):
    parser = argparse.ArgumentParser(prog="ls")
    parsed = parser.parse_args(args)

    for file in session.cwd.children:
        print(file.name)
