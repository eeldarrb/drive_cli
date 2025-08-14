import os
import argparse


def handle_upload(session, *args):
    parser = argparse.ArgumentParser(prog="upload")
    parser.add_argument("local_path")
    parsed = parser.parse_args(args)

    if not os.path.exists(parsed.local_path):
        raise FileNotFoundError(parsed.local_path)

    file_node = session.vfs.upload(parsed.local_path)
    print(f"Successfully uploaded: {file_node.name}")
