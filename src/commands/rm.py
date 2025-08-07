import argparse


def handle_rm(session, *args):
    parser = argparse.ArgumentParser(prog="rm")
    parser.add_argument("file_name")
    parsed = parser.parse_args(args)

    client = session.client
    file_path = parsed.file_name

    file = session.drive_tree.get_node_by_path(session.drive_tree.cwd, file_path)

    client.delete_file(file.id)
    file.detach()
