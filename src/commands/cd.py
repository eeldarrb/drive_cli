import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    directory_path = parsed.directory_name
    session.cwd = session.drive_tree.get_node_by_path(
        session.cwd, directory_path, require_directory=True
    )
    return
