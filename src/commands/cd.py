def handle_cd(session, folder_name):
    try:
        for item in session.cwd.children:
            if (
                item.name == folder_name
                and item.mime_type == "application/vnd.google-apps.folder"
            ):
                session.cwd = item
                return
        print(f"No such directory: {folder_name}")
    except Exception as e:
        print(f"[Unexpected Error] Command 'cd' failed: {e}")
