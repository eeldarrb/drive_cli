from drive_tree.drive_node import DriveNode


def handle_mkdir(session, *args):
    client = session.client
    folder_name = args[0]
    curr_dir = session.cwd

    created_folder = client.create_dir(folder_name, curr_dir.id)
    if created_folder:
        new_dir = DriveNode(
            created_folder.get("id"),
            created_folder.get("name"),
            created_folder.get("mimeType"),
        )
        curr_dir.add_child(new_dir)
