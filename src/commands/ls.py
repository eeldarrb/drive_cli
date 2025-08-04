import argparse


def handle_ls(session, *args):
    parser = argparse.ArgumentParser(prog="ls")
    parser.add_argument("path", nargs="?", default=".")
    parsed = parser.parse_args(args)

    path = parsed.path
    resolved_path = session.drive_tree.get_node_by_path(session.cwd, path)

    for file in resolved_path.children:
        print(file.name)
