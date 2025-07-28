def handle_cd(session, folder_name):
    for item in session.cwd.children:
        if (
            item.name == folder_name
            and item.mime_type == "application/vnd.google-apps.folder"
        ):
            session.cwd = item
            return
    raise FileNotFoundError(folder_name)
