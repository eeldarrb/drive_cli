import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    directory_name = parsed.directory_name
    for item in session.cwd.children:
        if (
            item.name == directory_name
            and item.mime_type == "application/vnd.google-apps.folder"
        ):
            session.cwd = item
            return
    raise FileNotFoundError(directory_name)
