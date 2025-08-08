import argparse


def handle_ls(session, *args):
    parser = argparse.ArgumentParser(prog="ls")
    parser.add_argument("path", nargs="?", default=".")
    parsed = parser.parse_args(args)

    path = parsed.path
    resolved_node = session.drive_tree.ls(path)

    for file in resolved_node.children:
        print(file.name)
