def handle_cd(session, *args):
    folder_name = args[0]
    for item in session.cwd.children:
        if (
            item.name == folder_name
            and item.mime_type == "application/vnd.google-apps.folder"
        ):
            session.cwd = item
