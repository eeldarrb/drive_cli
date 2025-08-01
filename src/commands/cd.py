import argparse


def handle_cd(session, *args):
    parser = argparse.ArgumentParser(prog="mkdir")
    parser.add_argument("directory_name")
    parsed = parser.parse_args(args)

    directory_name = parsed.directory_name
    for file in session.cwd.children:
        if (
            file.name == directory_name
            and file.mime_type == "application/vnd.google-apps.folder"
        ):
            session.cwd = file
            return
    raise FileNotFoundError(directory_name)
